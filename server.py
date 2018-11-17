from flask import Flask, jsonify
from flaskext.mysql import MySQL
import json
from flask import request

app = Flask(__name__)

# create mysql instance and configure it
app.config['MYSQL_DATABASE_USER'] = 'ist425412'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pxfi3850'
app.config['MYSQL_DATABASE_DB'] = 'ist425412'
app.config['MYSQL_DATABASE_HOST'] = 'db.tecnico.ulisboa.pt'
mysql = MySQL(app)

mysql.init_app(app)

nr_players=0
flag_available=0


def update_results(time,correct,total,idp):
	conn = mysql.connect()
	mycursor=conn.cursor()
	mycursor.execute('''UPDATE highscore set seconds_time="%d",correct_answer="%d", total_questions="%d" where id="%d"''' %(time,correct,total,int(idp)))
	conn.commit()




def insertPlayer(name,curso,nr,mail,tempo,corretas,total):
	conn = mysql.connect()
	mycursor=conn.cursor()
	mycursor.execute('''INSERT INTO highscore VALUES("%s","%s","%d","%s" , "%d", "%d","%d")''' %(name,curso,int(nr),mail,tempo,corretas,total))
	conn.commit()

@app.route('/questions/<index>')
def show_question(index):
	cur = mysql.connect().cursor()
	cur.execute('''select * from quiz order by rand() limit '''+index)

	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]

	return jsonify(r)



@app.route('/PlayerInformation',  methods=['POST', 'GET'] )
def playerInformation():
	global flag_available
	global nr_players
	if request.method == "POST":
		if flag_available==0:
			nr_players=nr_players+1
			aux = request.get_json()
			insertPlayer(aux['name'],aux['course'],aux['id'],aux['mail'],0,0,0)
			if nr_players==2:
				flag_available=1


	return str(nr_players)

@app.route('/Results', methods=['POST', 'GET'])
def PlayerResult():
	global nr_players
	if request.method =="POST":
		if nr_players>0:
			nr_players=nr_players-1
			aux= request.get_json()
			update_results(aux['time'],aux['correct'],aux['total'],aux['id'])
	return str(nr_players)


@app.route('/check',methods=['GET'])
def check_available():
	global flag_available
	return jsonify(flag_available)


if __name__ == '__main__':
	app.run(debug = True)
