import pickle

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn import metrics

df = pd.read_excel("mldata.xlsx")

# dealing with nulls
df['PRODLEVEL'].fillna((df['PRODLEVEL'].mean()), inplace=True)
df['PRODHOURS'].fillna((df['PRODHOURS'].mean()), inplace=True)

type_encoder = LabelEncoder()
df['Type'] = type_encoder.fit_transform(df['Type'].astype('str'))
output = open('type_encoder.pkl', 'wb')
pickle.dump(type_encoder, output)
output.close()

x = df[['Type', 'SALES', 'EMPLOYEES', 'PLANT_AREA', 'PRODLEVEL', 'PRODHOURS']]

y = df['SOURC_ELEC']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)

# predict
y_pred_rfr = lin_reg.predict(x_test)

print("score : " + str(metrics.r2_score(y_test, y_pred_rfr)))

filename = 'finalized_model.sav'
pickle.dump(lin_reg, open(filename, 'wb'))


