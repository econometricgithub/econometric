#importing necessary library
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from flask import Flask, render_template,flash, request
from wtforms import Form, StringField, validators, SubmitField, SelectField
from bioinfokit.analys import get_data, stat
#Importing SQLAlcheny
from flask_sqlalchemy import SQLAlchemy
#from custom_validators import height_validator, weight_validator
from myModules import results_summary_to_dataframe, result_one,results_two, main_fun, reg_metric, linerity,normality,homoscedasticity,multicollinearity
#input are just variables - not as in the short form [ Y, X ]


df=pd.read_csv("Dataset/data_cleaning.csv")
print(df.head)
y=df['OEP']
print(y)
y=df.iloc[:,39]
print(y)
#X=df["informational_use","SIU","entertainment_use","gender","age","education","income","location"]
#print(X)
X=df[['informational_use','SIU','entertainment_use','gender','age','education','income','location']]
print(X)
X=df.iloc[:,[['informational_use','SIU','entertainment_use','gender','age','education','income','location']]]
print(X)