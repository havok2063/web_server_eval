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
from quart import Quart
from apitest.io.access import get_cube, get_header

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


app.run()
