# -*- encoding=UTF-8 -*-

from homework3 import app

@app.route('/')
def index():
    return 'Hello'