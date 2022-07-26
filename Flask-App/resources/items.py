#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:53:02 2022

@author: dhananjayvatshayan
"""

from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required
from models.items import ItemModel

class Item(Resource):
    
    parser=reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,
                        help="this field caanot be left blank")
    parser.add_argument('store_id',type=int,required=True,
                        help="Every item needs a store id")
    
    @jwt_required
    def get(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message":"item not found"},404
    
    def post(self,name):
        if ItemModel.find_by_name(name):
            return {"message":"an item with this name already exists"},400
        data=Item.parser.parse_args()
        item=ItemModel(name, data['price'], data['store_id'])
        try:
            item.svae_to_db()
        except:
            return {"message":"an error occured during insert"},404
        
    def delete(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message":"item deleted"}
    
    def put(self,name):
        item=ItemModel.find_by_name(name)
        data=Item.parser.parse_args()
        
        if item is None:
            item=ItemModel(name, data['price'], data['store_id'])
        else:
            item.price=data['price']
            item.store_id=data['store_id']
            
        item.save_to_db()
        return item.json()
    
class ItemList(Resource):
    def get(self):
        return {'items':list(map(lambda  x:x.json(),ItemModel.query.all()))}
        