#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：coding 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：lu.yu
@Date    ：2022-09-28 10:53 
"""
import casbin_sqlalchemy_adapter
from casbin import Enforcer
from flask import Flask, jsonify
from flask_authz import CasbinEnforcer

app = Flask(__name__)
# Set up Casbin model config
app.config['CASBIN_MODEL'] = './app/conf/rbac_model.conf'
# Set headers where owner for enforcement policy should be located
app.config['CASBIN_OWNER_HEADERS'] = {'X-User', 'X-Group'}
# Add User Audit Logging with user name associated to log
# i.e. `[2020-11-10 12:55:06,060] ERROR in casbin_enforcer: Unauthorized attempt: method: GET resource: /api/v1/item by user: janedoe@example.com`
app.config['CASBIN_USER_NAME_HEADERS'] = {'X-User'}
# Set up Casbin Adapter
adapter = casbin_sqlalchemy_adapter.Adapter('sqlite:///test.db')

casbin_enforcer = CasbinEnforcer(app, adapter)
e: Enforcer = casbin_enforcer.e



@app.route('/', methods=['GET'])
@casbin_enforcer.enforcer
def get_root():
    return jsonify({'message': 'If you see this you have access'})


@app.route('/manager', methods=['POST'])
@casbin_enforcer.enforcer
@casbin_enforcer.manager
def make_casbin_change(manager):
    # Manager is an casbin.enforcer.Enforcer object to make changes to Casbin
    return jsonify({'message': 'If you see this you have access'})
