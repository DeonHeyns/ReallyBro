#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv

import bottle
from bottle import get, view, route, static_file

bottle.debug(False)

@route("/static/<filepath:path>")
def resources(filepath):
    return static_file(filepath, root='static')

@route('/')
@view('index')
def index():
    return {}

bottle.run(host='0.0.0.0', port=argv[1])
