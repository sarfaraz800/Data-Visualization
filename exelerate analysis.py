# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 12:32:21 2023

@author: HP
"""

import os
os.chdir('D:\Spyder Files')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_data=pd.read_excel(r'D:\Spyder Files\Datasets\marketdata.xlsx')
df_data.insert(1,'Campaign Id',0)
campaign_mapping = {
    'Campaign 1': 1,
    'Campaign 2': 2,
    'Campaign 3': 3,
    'Campaign 4': 4,
    'Campaign 5': 5,
    'Campaign 6': 6,
    'Campaign 7': 7,
    'Campaign 8': 8,
    'Campaign 9': 9,
    'Campaign 10': 10,
    'Campaign 11': 11
}
df_data['Campaign Id'] = df_data['Campaign ID'].apply(lambda x: campaign_mapping.get(x, 11))

sns.boxplot(x=df_data['Campaign Id'],y=df_data['Amount Spent in INR'])
plt.title("Amount spent by each Campaign")

plt.scatter(df_data['Campaign Id'],df_data['Amount Spent in INR'],c='blue')
plt.title("Amount spent by each Campaign")
plt.xlabel('Campaign ID')
plt.ylabel("Amount Spent in INR")

sns.regplot(x=df_data['Campaign Id'],y=df_data['Reach'],fit_reg=False)
plt.title("Reach of each Campaign")

sns.regplot(x=df_data['Campaign Id'],y=df_data['Impressions'],fit_reg=False)
plt.title("Impressions of each Campaign")
