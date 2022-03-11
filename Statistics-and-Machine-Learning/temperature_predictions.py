from sklearn.ensemble import RandomForestRegressor

month = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}

n = int(input())
input()
lines = [input().split() for i in range(n)]
for i in [2, 3]:
    x, y, xx = [], [], []
    for t in lines:
        yy = int(t[0])
        mm = [0]*12
        mm[month[t[1]]-1] = 1
        if t[5-i][0] != 'M':
            xl = mm+[yy*12+month[t[1]]-1, float(t[5-i])]
        if t[2][0] != 'M' and t[3][0] != 'M':
            x.append(xl)
            y.append(float(t[i]))
        if t[i][0] == 'M':
            xx.append(xl)
    model = RandomForestRegressor()
    model.fit(x, y)
    yy = model.predict(xx)
    if i == 2:
        maxp = yy
    else:
        minp = yy

maxi, mini = 0, 0
for t in lines:
    if t[2][0] == 'M':
        print('{:.1f}'.format(float(maxp[maxi])))
        maxi += 1
    elif t[3][0] == 'M':
        print('{:.1f}'.format(float(minp[mini])))
        mini += 1