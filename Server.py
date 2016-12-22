#!/usr/bin/env python
from flask import Flask, request
from ThinkerBot import *

tb = ThinkerBot()

app = Flask(__name__)

@app.route("/<command>/<value>")
def set(command, value):
    getattr(tb, command)(int(value))
    return command+"="+value+" Command successful."

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
