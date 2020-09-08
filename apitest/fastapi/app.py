# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Filename: app.py
# Project: fastapi
# Author: Brian Cherinka
# Created: Thursday, 2nd April 2020 11:41:36 am
# License: BSD 3-clause "New" or "Revised" License
# Copyright (c) 2020 Brian Cherinka
# Last Modified: Thursday, 2nd April 2020 4:37:11 pm
# Modified By: Brian Cherinka


from __future__ import print_function, division, absolute_import
import orjson
from fastapi import FastAPI
from fastapi.responses import Response
from apitest.io.access import get_cube, get_header, get_data

app = FastAPI()


@app.get("/")
async def hello():
    return {'hello fastapi': 'world'}


@app.get("/header/")
def header():
    cube = get_cube()
    hdr = get_header(cube)
    results = {'stream': cube, 'header': hdr.tostring()}
    return results


@app.get("/aheader/")
async def async_header():
    cube = get_cube()
    hdr = get_header(cube)
    results = {'stream': cube, 'header': hdr.tostring()}
    return results


@app.get('/file/{ext}')
async def fits_ext(ext: str):
    cube = get_cube()
    data, hdr = get_data(cube, ext.upper(), header=True)
    results = {'stream': cube, 'header': hdr.tostring(), 'data': data}
    # this is temporary until fastapi.responses.ORJSONResponse can accept options
    return Response(orjson.dumps(results, option=orjson.OPT_SERIALIZE_NUMPY),
                    media_type='application/json')
