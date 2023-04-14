import datetime
import calendar
import time
import numpy as np
import pandas as pd


# get current date after adding 5:30 hours
def current_date():
    current_date = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)
    return current_date.strftime("%d %B %Y")


# get current day after adding 5:30 hours
def current_day():
    current_day = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)
    return current_day.strftime("%A")


# function to give an array of times of the next 4 hours as 2:00 AM Format in an increment of 4 hours after adding 5:30 hours initially
def next_4_hours():
    next_4_hours = []
    current_time = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)
    for i in range(5):
        next_4_hours.append((current_time + datetime.timedelta(hours=4 * i)).strftime("%I:00 %p"))
    return next_4_hours

# function to give the data for the last 24 hours
def last_24_hours(req_array):
    # converting a 2d array having humidity,temperature and time to a dataframe
    df = pd.DataFrame(np.array(req_array), columns=['time', 'temperature', 'humidity'])

    # getting the last 24 hours epoch time value from the current time
    current_time = calendar.timegm(time.gmtime())
    last_24_hours = current_time - 86400

    # filtering the dataframe to get the last 24 hours data
    df = df[df['time'] > last_24_hours]
    df = df.reset_index(drop=True)

    # subtracting the last 24 hours epoch time value from the time column
    df['time'] = df['time'].apply(lambda x: x - last_24_hours)
    df['time'] = df['time'].astype(int)

    return df



