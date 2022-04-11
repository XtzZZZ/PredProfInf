import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import sqlite3
import csv

def predict_costs(file):
    # получение данных из sql и их запись в csv
    con = sqlite3.connect('db.db')
    cursor = con.cursor()
    query = '''SELECT amount,
       strftime('%m', date) AS month
  FROM Costs
 WHERE Costs.user_id = 1 AND 
        CAST(strftime('%m', date) as int) = 10 AND 
        CAST(strftime('%d', date) as int) = 10;
'''
    cursor.execute(query)
    row = cursor.fetchall()
    with open('costs.csv', 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(row)
    cursor.close()

    # считываем данные из csv в датафрейм pandas
    data = pd.read_csv('costs.csv', sep=';')
    size = len(data.index)
    x = data.iloc[:size - 1].drop('after', axis=1)
    y = data.iloc[:size - 1]['after']
    last = data.iloc[size - 1].drop('after')

    # создаем модель линейной регрессии и подгоняем ее под имеющиеся данные
    model = LinearRegression(fit_intercept=True)
    model.fit(x, y)
    result = model.predict(np.array([[last[0], last[1]]]))
    result = float(result)

    return result

