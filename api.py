from flask import Flask
from flask import render_template, jsonify
from flask import request
import requests
import bookDB


def get_func(idx):

	r = requests.get("http://127.0.0.1:5000/questions"+idx)
	print(r.status_code)
	data = r.json()
	print(data)

#!/usr/bin/env python



for i in range (1,5):
	get_func(i)


