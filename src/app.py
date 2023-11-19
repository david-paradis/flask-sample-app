#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <span>Please enter your name</span>
     <form action="/echo_user_input" method="POST">
         <input name="user_input">
         <input type="submit" value="Submit!">
     </form>    
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "Welcome " + input_text + ". Nice to meet you!" + \
    '''
        <div></div><a href="/">Back to home</a>
    '''