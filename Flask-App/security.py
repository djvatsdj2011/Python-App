#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 13:10:27 2022

@author: dhananjayvatshayan
"""

from resources.users import UserModel

def authenticate(username,password):
    user=UserModel.find_by_username(username)
    if user and user.password==password:
        return user
    
def identity(payload):
    user_id=payload['identity']
    return UserModel.find_by_id(user_id)