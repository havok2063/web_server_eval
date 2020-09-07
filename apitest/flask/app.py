# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Filename: app.py
# Project: flask
# Author: Brian Cherinka
# Created: Wednesday, 1st April 2020 12:04:26 pm
# License: BSD 3-clause "New" or "Revised" License
# Copyright (c) 2020 Brian Cherinka
# Last Modified: Thursday, 2nd April 2020 11:10:12 am
# Modified By: Brian Cherinka


from __future__ import print_function, division, absolute_import
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello flask': 'world'}


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(debug=True)

