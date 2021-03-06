# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Filename: app.py
# Project: quart
# Author: Brian Cherinka
# Created: Thursday, 2nd April 2020 10:17:33 am
# License: BSD 3-clause "New" or "Revised" License
# Copyright (c) 2020 Brian Cherinka
# Last Modified: Thursday, 2nd April 2020 11:30:01 am
# Modified By: Brian Cherinka


from __future__ import print_function, division, absolute_import
import orjson
from quart import Quart, Response, send_file
from apitest.io.access import get_cube, get_header, get_data, get_path

app = Quart(__name__)


@app.route('/')
async def hello():
    return {'hello quart': 'hello'}


@app.route('/header/')
def header():
    cube = get_cube()
    hdr = get_header(cube)
    results = {'stream': cube, 'header': hdr.tostring()}
    return results


@app.route('/aheader/')
async def async_header():
    cube = get_cube()
    hdr = get_header(cube)
    results = {'stream': cube, 'header': hdr.tostring()}
    return results


async def compdata(data):
    ''' compress the data '''
    return orjson.dumps(data, option=orjson.OPT_SERIALIZE_NUMPY)


@app.route('/file/<string:ext>')
async def json(ext):
    cube = get_cube()
    data, hdr = get_data(cube, ext=ext.upper(), header=True)
    results = {'stream': cube, 'header': hdr.tostring(), 'data': data}
    compressed = await compdata(results)
    return Response(compressed, mimetype='application/json')


@app.route('/dlimage/')
async def download_image():
    im = get_path('mangaimage', plate=8485, ifu=1901, drpver='v2_4_3', dir3d='stack')
    return await send_file(im, as_attachment=True)


@app.route('/dlfile/')
async def download_file():
    cube = get_cube()
    return await send_file(cube, as_attachment=True)


app.run()
