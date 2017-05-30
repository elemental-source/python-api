#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, Response, json, make_response

app = Flask(__name__)


@app.route('/ola', methods=['GET'])
def ola():
    data = {
        'message': 'Olá Mundo'
    }
    return Response(json.dumps(data),
                    status=200,
                    content_type='application/json; charset=utf-8')


if __name__ == '__main__':
    app.run()
