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

app = FastAPI()


@app.get("/")
async def hello():
    return {'hello fastapi': 'world'}

