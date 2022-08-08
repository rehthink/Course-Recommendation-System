# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:25:29 2022

@author: Rehan Ahmed Khan
"""

# 1. Import libraries 
import uvicorn
from fastapi import FastAPI
import pickle

# 2. Create the app object
app = FastAPI()

from pydantic import BaseModel

class request_body(BaseModel):
    course_title: str
    num: int


pickle_in = open("recommendation.pkl","rb")
classifier=pickle.load(pickle_in)


### To Run Enter http://127.0.0.1:8000/
@app.get('/')
def index():
    return {'message': 'Hello, World'}

### To Run query http://127.0.0.1:8000/Welcome?name=Rehan
@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome': f'{name}'}

@app.post('/recommend')
def recommend_course(data: request_body):
    test_data =[[data.course_title, data.num]]
    class_predict = classifier.recommend_course(test_data)[0]
    return {'result' : class_predict}


#Just to Start. type - uvicorn main:app --reload
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
