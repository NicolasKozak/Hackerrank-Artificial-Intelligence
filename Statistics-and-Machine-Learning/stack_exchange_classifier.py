# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 20:26:12 2022

@author: Nico
"""

import json
from sklearn.svm import LinearSVC
#from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import HashingVectorizer

transformer=HashingVectorizer(stop_words='english')

_train=[]
train_label=[]
f=open('training.json')
for i in range(int(f.readline())):
    h=json.loads(f.readline())
    _train.append(h['question']+"\r\n"+h['excerpt'])
    train_label.append(h['topic'])
f.close()
train = transformer.fit_transform(_train)
svm=LinearSVC()
svm.fit(train,train_label)

_test=[]
for i in range(int(input())):
    h=json.loads(input())
    _test.append(h['question']+"\r\n"+h['excerpt'])
test = transformer.transform(_test)
test_label=svm.predict(test)
for e in test_label: print(e)