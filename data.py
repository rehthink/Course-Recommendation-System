# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 12:21:12 2022

@author: REHAN AHMED KHAN
"""

from pydantic import BaseModel

class request_body(BaseModel):
    course_title: str
    num: int

