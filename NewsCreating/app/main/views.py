# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time   :  2018/7/17 20:40
# Author :  Richard
# File   :  views.py

from app import app
from flask import request, redirect, url_for, jsonify, session
from .. import file
from config import BASE_PATH
from app import summary_API
from app import writing_API


@app.route('/')
def index():
    return redirect(url_for('static', filename='html/index.html'))


@app.route('/file_upload_1', methods=['POST', 'GET'])
def file_upload_1():
    if request.method == 'GET':
        return redirect(url_for('static', filename='html/index.html'))
    file_tmp = request.files['file_tmp']
    if file_tmp:
        suffix = '.'+str(file_tmp.filename).split('.')[-1]  # 取得文件后缀
        if suffix in ['.txt', '.json', '.xml']:
            filename = "writing_source" + suffix
            file_path = BASE_PATH + "\\app\\static\\" + filename
            # 用session保存文件名
            # session['filename'] = filename
            print(file_path)
            file_tmp.save(file_path)
            # 设置session状态，用于判断是否上传文件
            session['is_writing'] = 1
            return jsonify({"res": "上传成功！"})
        else:
            # 设置session状态，用于判断是否上传文件
            session['is_writing'] = 0
            return jsonify({"res": "文件格式错误！"})
    else:
        # 设置session状态，用于判断是否上传文件
        session['is_writing'] = 0
        return jsonify({"res": "文件不能为空！"})


@app.route('/file_upload_2', methods=['POST','GET'])
def file_upload_2():
    if request.method == 'GET':
        return redirect(url_for('static', filename='html/index.html'))
    try:
        file_tmp = request.files['file_tmp']
    except:
        return jsonify({"res": "文件不能为空！"})
    if file_tmp:
        suffix = '.'+str(file_tmp.filename).split('.')[-1]  # 取得文件后缀
        if suffix in ['.txt','.json','.xml']:
            filename = "summary_source" + suffix
            file_path = BASE_PATH + "\\app\\static\\" + filename
            # 用session保存文件名
            # session['filename'] = filename
            print(file_path)
            file_tmp.save(file_path)
            # 设置session状态，用于判断是否上传文件
            session['is_summary'] = 1
            return jsonify({"res": "上传成功！"})
        else:
            # 设置session状态，用于判断是否上传文件
            session['is_summary'] = 0
            return jsonify({"res": "文件格式错误！"})
    else:
        # 设置session状态，用于判断是否上传文件
        session['is_summary'] = 0
        return jsonify({"res": "文件不能为空！"})


@app.route('/news')
def article():
    if session.get('is_summary') == 0:
        return jsonify({'res': '请先上传文件！'})
    file_path = BASE_PATH + "\\app\\static\\" + 'writing_source.json'
    # file_instance = file.File(file_path)
    # file_content_json = file_instance.parse_content()
    # # 调用接口获取数据
    # res = file_content_json
    # print(res)
    res = writing_API.writing_API(file_path)
    # return jsonify({'res': res})
    return res


@app.route('/summary')
def summary():
    if session.get('is_summary') == 0:
        return jsonify({'res': '请先上传文件！'})
    summary_str = summary_API.summary_API()
    print(summary_str)
    return jsonify({'res':summary_str})



