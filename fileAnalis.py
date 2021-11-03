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

X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)