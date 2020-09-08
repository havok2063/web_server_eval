# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Filename: access.py
# Project: io
# Author: Brian Cherinka
# Created: Monday, 7th September 2020 1:41:59 pm
# License: BSD 3-clause "New" or "Revised" License
# Copyright (c) 2020 Brian Cherinka
# Last Modified: Monday, 7th September 2020 1:42:00 pm
# Modified By: Brian Cherinka


from __future__ import print_function, division, absolute_import
from sdss_access.path import Path
from astropy.io import fits


path = Path(public=True, release='DR15')


def get_path(name, ptype='full', **kwargs):
    ''' get an sdss_access local filepath '''
    if ptype == 'full':
        return path.full(name, **kwargs)
    elif ptype == 'name':
        return path.name(name, **kwargs)
    elif ptype == 'url':
        return path.url(name, **kwargs)
    else:
        return path.full(name, **kwargs)


def get_cube(plate=8485, ifu=1901, drpver='v2_4_3'):
    ''' get a manga cube local filepath '''
    cube = path.full('mangacube', drpver=drpver,
                     plate=plate, ifu=ifu, wave='LOG')
    return cube


def get_header(filename, ext=0):
    ''' get a FITS header '''
    with fits.open(filename) as hdu:
        return hdu[ext].header


def get_data(filename, ext=0, header=True):
    ''' get a FITS extension '''
    with fits.open(filename) as hdu:
        if header:
            return hdu[ext].data, hdu[ext].header
        else:
            return hdu[ext].data
