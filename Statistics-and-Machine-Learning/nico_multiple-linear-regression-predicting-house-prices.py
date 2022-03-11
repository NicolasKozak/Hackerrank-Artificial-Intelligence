from sklearn.linear_model import LinearRegression
import numpy as np

F, N = map(int, input().split())

X = []
y = []

for i in range(N):
    vals = list(map(float, input().split()))
    y.append(vals[-1])
    X.append(vals[:-1])

model = LinearRegression()
model.fit(X,y)


T =int(input())

X_test = []

for i in range(T):
    vals = list(map(float, input().split()))
    X_test.append(vals)

preds = model.predict(X_test)

for pred in preds:
    print("%.2f" % pred)