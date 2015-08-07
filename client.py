# -*- coding: utf-8 -*-

import zerorpc

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    c = zerorpc.Client(heartbeat=None)
    c.connect('tcp://127.0.0.1:7766')
    print c.ping()
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
