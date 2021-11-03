import csv

import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import pandas as pd

fields = ['level', 'time', 'score', 'health']
df = pd.read_csv("dano.csv", skipinitialspace=True, usecols=fields)

x = np.array(df[['health', 'time', 'level']])
y = np.array(df['score'])

model = LinearRegression()
model.fit(x, y)
print('predskazanie: ', model.intercept_, model.coef_)
X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
predictions = model.predict(X)
print('predicted response:', predictions, sep='\n')

print_model = model.summary()
print(print_model)

buffer = []
for i in range(0, len(x)-1):
    buff = ''
    for j in x[i]:
        buff += str(j) + ","
    #print(buff)
    buff += str(predictions[i])
    #print(buff)
    buffer.append(buff)
print(buffer)

with open("ans.csv", "wt", encoding="utf-8") as output:
    for line in buffer:
        output.write(line + '\n')