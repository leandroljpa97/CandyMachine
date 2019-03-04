from flask import Flask
from flask import render_template, jsonify
from flask import request
import requests





def results():
	payload = {"time":800,"correct":21,"total":30,"id":103, "code":1}
	r = requests.post("http://127.0.0.1:5000/results", json=payload)
	payload = {"time":900,"correct":21,"total":30,"id":1001, "code":2}
	r = requests.post("http://127.0.0.1:5000/results", json=payload)
	print(r.text)

results()
