#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, Response, make_response, jsonify, request

app = Flask(__name__)


@app.route('/ola', methods=['GET'])
def ola():
    if 'nome' in request.args:
        data = {'message': 'Olá ' + request.args['nome']}
        response = jsonify(data)
        response.status_code = 200
        response.content_type = 'application/json; charset=utf-8'
        return response
    else:
        data = {'message': 'Olá Mundo'}
        response = jsonify(data)
        response.status_code = 200
        response.content_type = 'application/json; charset=utf-8'
        return response

if __name__ == '__main__':
    app.run()
