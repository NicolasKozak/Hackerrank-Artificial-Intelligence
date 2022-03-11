import json
from sklearn.svm import LinearSVC
#from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import HashingVectorizer

transformer=HashingVectorizer(stop_words='english', n_features=10**4)

_train=[]
train_label=[]
f=open('training.json')
for i in range(int(f.readline())):
    h=json.loads(f.readline())
    _train.append(h['city']+"\r\n"+h['section']+"\r\n+"+h['heading'])
    train_label.append(h['category'])
f.close()
train = transformer.fit_transform(_train)
clf=LinearSVC()
clf.fit(train,train_label)

_test=[]
for i in range(int(input())):
    h=json.loads(input())
    _test.append(h['city']+"\r\n"+h['section']+"\r\n+"+h['heading'])
test = transformer.transform(_test)
test_label=clf.predict(test)
for e in test_label: print(e)