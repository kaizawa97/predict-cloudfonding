# -*- coding: utf-8 -*-
import os
import pandas as pd 
import numpy as np

from sklearn import svm
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

os.chdir("makecsv/")
df = pd.read_csv("onehotencorder.csv",header = 0)

data = df['successorfail'] 
answers = []

X_train, X_test, y_train, y_test = train_test_split(data, answers, train_size=0.8, test_size=0.2, random_state=1)
  # データの分割（データの80%を訓練用に、20％をテスト用に分割する）

clf = svm.LinearSVC()
clf.fit(X_train,y_train)

# 正解率の計算
train_score = accuracy_score(y_train, y_train_pred)
test_score = accuracy_score(y_test, y_val_pred)

# 正解率を表示
print("トレーニングデータに対する正解率：" + str(train_score * 100) + "%")
print("テストデータに対する正解率：" + str(test_score * 100) + "%")
