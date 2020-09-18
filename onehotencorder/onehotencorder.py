import pandas as pd
import os
import csv
from IPython.display import display

makuake_path = '../makecsv/makuaketagdata.csv'
file = '../makecsv/onehotencorder.csv'

data = pd.read_csv(makuake_path,header=0,index_col = False ,names = ['successorfail','moneygoal','image','projectdetail','riskchallengedetail','numberofpackage','avemoneypackage','minmoneypackage','maxmoneypackage','category'])
data_dummies = pd.get_dummies(data)
# print("Features after get_dummies:\n", list(data_dummies.columns))
# data_dummies.head()

# display(data.head())

data=data_dummies.to_csv(file,index=False)
print(data_dummies)
