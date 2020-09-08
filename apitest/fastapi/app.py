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
from typing import Any, Optional
from fastapi import FastAPI
from fastapi.responses import Response, StreamingResponse, FileResponse, JSONResponse
from apitest.io.access import get_cube, get_header, get_data, get_path

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


class ORJSONResponseCustom(JSONResponse):
    media_type = "application/json"
    option = None

    def __init__(self, option: Optional[int] = None, **kwds):
        self.option = option
        super().__init__(**kwds)

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed to use ORJSONResponse"
        return orjson.dumps(content, option=self.option)


@app.get('/file/{ext}')
async def fits_ext(ext: str):
    cube = get_cube()
    data, hdr = get_data(cube, ext.upper(), header=True)
    results = {'stream': cube, 'header': hdr.tostring(), 'data': data}
    # this is temporary until fastapi.responses.ORJSONResponse can accept options
    #return ORJSONResponseCustom(results, option=orjson.OPT_SERIALIZE_NUMPY)
    return Response(orjson.dumps(results, option=orjson.OPT_SERIALIZE_NUMPY),
                    media_type='application/json')


@app.get("/dlimage")
async def download_image():
    ''' async streams a file as a response '''
    im = get_path('mangaimage', plate=8485, ifu=1901, drpver='v2_4_3', dir3d='stack')
    imname = get_path('mangaimage', full=im, ptype='name')
    return FileResponse(im, filename=imname, media_type='image/png')


@app.get("/dlfile")
async def file_response():
    ''' async streams a file as a response '''
    cube = get_cube()
    name = get_path('mangacube', full=cube, ptype='name')
    # fileresponse is used for streaming downloads
    return FileResponse(cube, filename=name, media_type='application/gzip')


@app.get("/streamall/")
def streaming_response():
    ''' stream a file-like object as a response '''
    cube = get_cube()
    file_like = open(cube, mode="rb")
    return StreamingResponse(file_like, media_type='application/octet-stream')


@app.get("/streamimage")
async def image_response():
    ''' async streams a file as a response '''
    im = get_path('mangaimage', plate=8485, ifu=1901, drpver='v2_4_3', dir3d='stack')
    ii = open(im, 'rb')
    return StreamingResponse(ii)
