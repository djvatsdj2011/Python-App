#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:51:18 2022

@author: dhananjayvatshayan
"""

from flask import Flask
from flask_restful import Resource,Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.users import UserRegister
from resources.items import Item,ItemList
from resources.stores import Store,StoreList
from db import db

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqllite://data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='Jose'
api=Api(app)

@app.before_first_request 
def create_table():
    db.create_all()
    
jwt=JWT(app,authenticate,identity)
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__=="__main__":
    db.init_app(app)
    app.run(port=5000)