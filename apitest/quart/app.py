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

app = Quart(__name__)


@app.route('/')
async def hello():
    return {'hello quart': 'hello'}


app.run()
