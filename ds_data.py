# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 20:12:06 2020

@author: ninjaelf
"""

import glassdoor_scraper as gs
import pandas as pd


path = "C:/Users/ninjaelf/Desktop/first_project/chromedriver"

df = gs.get_jobs('data scientist',15,False,path,15)
