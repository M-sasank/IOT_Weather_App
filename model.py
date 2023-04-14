import numpy as np
import pandas as pd
import time
from times import *
import calendar



def model(req_array,pred_time):
    # converting a 2d array having humidity,temperature and time to a dataframe
    df = pd.DataFrame(np.array(req_array), columns=['time','temperature','humidity'])

    # getting the last 24 hours epoch time value from the current time
    current_time = calendar.timegm(time.gmtime())
    last_24_hours = current_time - 86400

    # ffiltering the dataframe to get the last 24 hours data
    df = df[df['time'] > last_24_hours]
    df = df.reset_index(drop=True)

    # subtracting the last 24 hours epoch time value from the time column
    df['time'] = df['time'].apply(lambda x: x - last_24_hours)
    df['time'] = df['time'].astype(int)

    # subtracting the last 24 hours epoch time value from the time parameter
    pred_time = pred_time - last_24_hours

    # creating a new dataframe with only humidity and time
    df1 = df[['humidity', 'time']]
    # creating a new dataframe with only temperature and time
    df2 = df[['temperature', 'time']]

    # using random forest regressor to predict humidity
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    regressor.fit(df1.iloc[:, 1:2].values, df1.iloc[:, 0].values)
    humidity = regressor.predict([[pred_time]])[0]

    # using random forest regressor to predict temperature
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    regressor.fit(df2.iloc[:, 1:2].values, df2.iloc[:, 0].values)

    # predicting humidity and temperature for a given time

    temperature = regressor.predict([[pred_time]])[0]
    return temperature,humidity