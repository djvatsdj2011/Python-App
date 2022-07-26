#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:52:24 2022

@author: dhananjayvatshayan
"""

from flask_restful import Resource,reqparse
from models.users import UserModel

class UserRegister(Resource):
    
    parser=reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,
                        help="this field caanot be left blank")
    parser.add_argument('password',type=int,required=True,
                        help="Every item needs a store id")
    
    def post(self):
        data=UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']):
            return {"message":"an user with this username already exists"},400
        else:
            user=UserModel(**data)
            user.save_to_db()
            return {"message":"User created successfully"},201