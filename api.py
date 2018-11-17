from flask import Flask
from flask import render_template, jsonify
from flask import request
import requests




def login():
	payload = {"name":"andre","course":"xixixixixixi","id":2022,"mail":"ahahah","time":60,"correct":3,"total":3}
	r = requests.post("http://127.0.0.1:5000/PlayerInformation", json=payload)
	print(r.text)

def results():
	payload = {"time":900,"correct":21,"total":30,"id":2022}
	r = requests.post("http://127.0.0.1:5000/Results", json=payload)
	print(r.text)

results()
