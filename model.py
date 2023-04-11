import numpy as np
import pandas as pd


def model(req_array,time):
    # converting a 2d array having humidity,temperature and time to a dataframe
    df = pd.DataFrame(np.array(req_array), columns=['time','temperature','humidity'])

    # creating a new dataframe with only humidity and time
    df1 = df[['humidity', 'time']]
    # creating a new dataframe with only temperature and time
    df2 = df[['temperature', 'time']]

    # using random forest regressor to predict humidity
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    regressor.fit(df1.iloc[:, 1:2].values, df1.iloc[:, 0].values)
    humidity = regressor.predict([[time]])[0]

    # using random forest regressor to predict temperature
    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    regressor.fit(df2.iloc[:, 1:2].values, df2.iloc[:, 0].values)

    # predicting humidity and temperature for a given time

    temperature = regressor.predict([[time]])[0]
    return temperature,humidity