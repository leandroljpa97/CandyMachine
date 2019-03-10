from flask import Flask, jsonify
from flaskext.mysql import MySQL
import json
from flask import request
import ast

app = Flask(__name__)

# create mysql instance and configure it
app.config['MYSQL_DATABASE_USER'] = 'ist425412'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pxfi3850'
app.config['MYSQL_DATABASE_DB'] = 'ist425412'
app.config['MYSQL_DATABASE_HOST'] = 'db.tecnico.ulisboa.pt'
mysql = MySQL(app)

mysql.init_app(app)

nr_players = 0
r= []
waitingPlayer = 0
counter = 0
winner = 0
timePlayer1 = -1
rightPlayer1 = -1
timePlayer2 = -1
rightPlayer2 = -1
idPlayer1 = -1
idPlayer2 = -1

def update_results(time,correct,total,idp):
	conn = mysql.connect()
	mycursor=conn.cursor()
	mycursor.execute('''UPDATE highscore set seconds_time="%d",id=id, correct_answer="%d", total_questions="%d" where id="%s"''' %(time,correct,total,idp))
	conn.commit()

def insertPlayer(name,curso,nr,mail,tempo,corretas,total):
	conn = mysql.connect()
	mycursor=conn.cursor()
	mycursor.execute('''INSERT INTO highscore VALUES("%s","%s","%s","%s" , "%d", "%d","%d")''' %(name,curso,nr,mail,tempo,corretas,total))
	conn.commit()

def getWinner():
	global winner
	global timePlayer1 
	global rightPlayer1 
	global timePlayer2 
	global rightPlayer2 
	if timePlayer1==-1 or timePlayer2==-1:
		winner = 0
		return 
	if rightPlayer1>rightPlayer2:
		winner = 1
	elif rightPlayer2>rightPlayer1:
		winner = 2
	elif rightPlayer1 == rightPlayer2:
		if timePlayer1 < timePlayer2:
			winner = 1
		else:
			winner = 2



@app.route('/index',  methods=['POST', 'GET'] )
def playerInformation():
	global nr_players
	global waitingPlayer
	global idPlayer2
	global idPlayer1
	if request.method == "POST":
		if nr_players<2:
			nr_players = nr_players+1
			code = nr_players
			if code == 1:
				idPlayer1 = ast.literal_eval(request.form.get('id'))
			if code == 2:
				idPlayer2 = ast.literal_eval(request.form.get('id'))
			insertPlayer(request.form.get('name'),request.form.get('course'),ast.literal_eval(request.form.get('id')),request.form.get('mail'),0,0,0)
			if nr_players == 2:
				waitingPlayer = 1
			return jsonify(code)
		return jsonify(0)
	return jsonify(0)

@app.route('/wait',methods=['GET'])
def waitingFunction():
	global waitingPlayer
	return jsonify(waitingPlayer)			

@app.route('/questions',  methods=['POST', 'GET'] )
def Questions():
	global counter
	global r
	if counter ==0:
		cur = mysql.connect().cursor()
		cur.execute('''select * from quiz order by rand() limit 6''')
		r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
		counter=counter+1
	else:
		counter=0
	return jsonify(r)

@app.route('/results', methods=['POST', 'GET'])
def PlayerResult():
	global timePlayer1
	global timePlayer2
	global rightPlayer1
	global rightPlayer2
	global idPlayer2
	global idPlayer1
	if request.method =="POST":	
			if int(ast.literal_eval(request.form.get('code'))) == 1:
				timePlayer1=int(ast.literal_eval(request.form.get('time')))
				print(timePlayer1)
				rightPlayer1=int(ast.literal_eval(request.form.get('correct')))
				update_results(int(ast.literal_eval(request.form.get('time'))),int(ast.literal_eval(request.form.get('correct'))),6,idPlayer1)
			elif int(ast.literal_eval(request.form.get('code'))) == 2:
				timePlayer2= int(ast.literal_eval(request.form.get('time')))
				rightPlayer2= int(ast.literal_eval(request.form.get('correct')))
				update_results(int(ast.literal_eval(request.form.get('time'))),int(ast.literal_eval(request.form.get('correct'))),6,idPlayer2)

	return jsonify(0)



@app.route('/start', methods=['POST', 'GET'])
def StartArduino():
	global winner
	global nr_players
	global counter
	global waitingPlayer
	global timePlayer1 
	global rightPlayer1 
	global timePlayer2 
	global rightPlayer2 
	global idPlayer1 
	global idPlayer2
	getWinner()
	if winner != 0:
		nr_players = 0
		counter = 0
		waitingPlayer = 0
		timePlayer1 = -1
		rightPlayer1 = -1
		timePlayer2 = -1
		rightPlayer2 = -1
		idPlayer2 = -1
		idPlayer1 = -1
	aux = winner
	winner = 0 
	return jsonify(aux)

@app.route('/fresh', methods=['POST', 'GET'])
def fresh():
	global winner
	global nr_players
	global counter
	global waitingPlayer
	global timePlayer1 
	global rightPlayer1 
	global timePlayer2 
	global rightPlayer2 
	global idPlayer1
	global idPlayer2

	nr_players = 0
	counter = 0
	waitingPlayer = 0
	timePlayer1 = -1
	rightPlayer1 = -1
	timePlayer2 = -1
	rightPlayer2 = -1
	winner = 0 
	idPlayer2 = -1
	idPlayer1 = -1
	return jsonify(1)



if __name__ == '__main__':
	app.run(debug = True)
