from asyncio.windows_events import NULL
from pickle import APPENDS
import psycopg2
from cgitb import text
from logging import NullHandler, exception
from tkinter import Y, messagebox
from itsdangerous import json
from dataclasses import fields
from unicodedata import numeric
from flask import Flask,jsonify,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import request
from flask_cors import CORS,cross_origin
import math
from datetime import datetime
import os
import cmath
from matplotlib.pyplot import plot
import numpy as np
import seaborn as sns
from sqlalchemy import JSON, Column, null, true
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

app=Flask(__name__)
app.config.from_object(__name__)

#CORS(app,support_credentials=True,resources={r'/*': {'origins': '*'}})
cors=CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:admin%40123@localhost/Weather_Database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
ma=Marshmallow(app)
      

@app.route('/',methods=['GET'])
def index():
    return "Flask Backend Server connected Sucessfully"               
              
  
      
print("#################################################################################")
print("#############Class Model for weather data#######################")

    
@app.route('/DataPipeline',methods=['POST','GET'])
@cross_origin(supports_credentials=True)
def DataPipeline():
    response_object = {'status':'success'}
    csvfile=None
    body = dict(request.form)
    print(body)
    print("***********check1")
    message={
    'msg':    "Welcome in Azure"
    }
    res=message
    return jsonify(res)
   




@app.route('/EToCalculation',methods=['POST','GET'])
@cross_origin(supports_credentials=True)
def EToCalculation():
       
        message={
        'res':"ET0 Calculation Completed"
        }
        return jsonify(message)
#======================================================================================            

if(__name__=="__main__"):
    app.run()