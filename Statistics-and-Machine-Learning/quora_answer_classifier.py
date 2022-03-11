from sklearn.ensemble import RandomForestClassifier

N,M = map(int, input().split())

X, y = [],[]
for i in range(N):
    line = input().strip().split()
    if line[1] == '+1':
        y.append('+1')
    elif line[1] == '-1':
        y.append('-1') 
           
    X.append([float(l.split(':')[1]) for l in line[2:]])    

clf = RandomForestClassifier()
clf.fit(X,y)

T = int(input())

X_test, names = [],[]
for i in range(T):
    line = input().strip().split()  
    names.append(line[0])         
    X_test.append([float(l.split(':')[1]) for l in line[1:]])    
    
preds = clf.predict(X_test)
for name, pred in zip(names,preds):
    print(name, pred)