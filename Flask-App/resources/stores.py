#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:49:13 2022

@author: dhananjayvatshayan
"""

from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'store not found'},404
    
    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message":"an store with this name already exists"},400
        else:
            store=StoreModel(name)
            try:
                store.save_to_db()
            except:
                return {"message":"an error occured during insert"},404
            
    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message':'store deleted'}
    
    
class StoreList(Resource):
    def get(self):
        return {'Stores':list(map(lambda  x:x.json(),StoreModel.query.all()))}