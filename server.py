from flask import Flask, jsonify
from flaskext.mysql import MySQL
import json

app = Flask(__name__)

# create mysql instance and configure it
app.config['MYSQL_DATABASE_USER'] = 'ist425412'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pxfi3850'
app.config['MYSQL_DATABASE_DB'] = 'ist425412'
app.config['MYSQL_DATABASE_HOST'] = 'db.tecnico.ulisboa.pt'
mysql = MySQL(app)

mysql.init_app(app)



@app.route('/questions/<index>')
def show_question(index):
	cur = mysql.connect().cursor()
	cur.execute('''select * from quiz where id='''+index)

	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]

	return jsonify(r)

if __name__ == '__main__':
	app.run(debug = True)
