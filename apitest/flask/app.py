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
import orjson
from flask import Flask, Response
from flask_restful import Resource, Api
from apitest.io.access import get_cube, get_header, get_data

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello flask': 'world'}


class FitsHeader(Resource):
    def get(self):
        cube = get_cube()
        hdr = get_header(cube)
        results = {'stream': cube, 'header': hdr.tostring()}
        return results


class FileExt(Resource):
    def get(self, ext):
        cube = get_cube()
        data, hdr = get_data(cube, ext.upper(), header=True)
        results = {'stream': cube, 'header': hdr.tostring(), 'data': data}
        return Response(orjson.dumps(results, option=orjson.OPT_SERIALIZE_NUMPY),
                        mimetype='application/json')


api.add_resource(HelloWorld, '/')
api.add_resource(FitsHeader, '/header', '/aheader')
api.add_resource(FileExt, '/file/<string:ext>')


if __name__ == '__main__':
    app.run(debug=True)

