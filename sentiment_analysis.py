# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 09:41:38 2023

@author: rbben
"""

import pandas as pd
from transformers import pipeline


##reading xlsx files

data = pd.read_excel('articles.xlsx')

##summary of the data 
data.describe()

#summary of the columns 
data.info()

#counting the number of articles per source
# format of groupby: df.groupby(['column_to_be_grouped'])['column_to_count'].count()

data.groupby(['source_id'])['article_id'].count()

#number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping a column
data = data.drop('engagement_comment_plugin_count' , axis=1)

keyword_flag = []
for x in range(0,10):
    heading = data['title'][x]
    if keyword in heading:
        flag = 1 
    else:
        flag = 0
    keyword_flag.append(flag)

sentiment_flag = []   
for x in range(0,10): 
    sentiment_pipeline = pipeline("sentiment-analysis")
    heading = data['title'][x]
    sentiment_pipeline(heading)
    sentiment_flag.append(sentiment_pipeline)

