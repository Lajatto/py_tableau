# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:27:35 2023

@author: rbben
"""

import pandas as pd
import json


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
 

##getting the results from the sentiment analysis and putting them in a table
#from transformers import pipeline
#sentiment_pipeline = pipeline("sentiment-analysis")
#data = ["It was the best of times.", "t was the worst of times."]
#df = pd.DataFrame(sentiment_pipeline(data))

title_column = pd.DataFrame({'title': data['title']})

title_list = title_column['title'].iloc[:100].tolist()

from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
exp = title_list
df = pd.DataFrame(sentiment_pipeline(exp))