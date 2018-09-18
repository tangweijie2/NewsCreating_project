# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/7/22 17:58
# Author :  Richard
# File   :  __init__.py.py

from flask import Response, Flask
import config
from flask_cors import *
from app.exts.summary import summary_API
from app.exts.writing import writing_API

class MyResponse(Response):
    default_mimetype = 'application/json'


app = Flask(__name__)
app.config.from_object(config)
CORS(app, supports_credentials=True)
app.config['JSON_AS_ASCII'] = False
app.response_class = MyResponse

from app import main