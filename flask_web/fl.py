from flask import Flask, render_template,request


@app.route('/')
def home():
 	 return("Hello World")