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
from fastapi import FastAPI
from apitest.io.access import get_cube, get_header

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
