import requests
import time
import calendar
import pandas as pd
import numpy as np
from times import *
from model import model

from flask import *

app = Flask(__name__)



@app.route('/')
def message():
    url = "https://api.thingspeak.com/channels/2102608/feeds.json?results=10000"

    data = requests.get(url).json()

    list = data['feeds']
    # print(list)
    temp_humidity = []
    for i in list:
        time1 = i['created_at']
        timestamp = time.strptime(time1, "%Y-%m-%dT%H:%M:%SZ")
        unix_time_local = time.mktime(timestamp)
        unix_time_utc = calendar.timegm(timestamp)
        temp_humidity.append([unix_time_utc, i['field1'], i['field2']])
    # print(temp_humidity)
    i = 0
    while i < len(temp_humidity):
        if temp_humidity[i][1] != None and temp_humidity[i][2] != None:
            temp_humidity[i][1] = float(temp_humidity[i][1])
            temp_humidity[i][2] = float(temp_humidity[i][2][:4])
        else:
            temp_humidity.pop(i)
            i -= 1
        i += 1

    # current time in epochs
    current_time = calendar.timegm(time.gmtime())
    # print(current_time)
    print(model(temp_humidity, current_time))
    current = (temp_humidity[-1][1], temp_humidity[-1][2])
    n_hours = 4
    hour1 = model(temp_humidity, current_time + 3600 * n_hours)
    # round to 1 decimal place
    hour1 = (round(hour1[0], 1), round(hour1[1], 1))
    hour2 = model(temp_humidity, current_time + 3600 * n_hours*2)
    hour2 = (round(hour2[0], 1), round(hour2[1], 1))
    hour3 = model(temp_humidity, current_time + 3600 + n_hours*3)
    hour3 = (round(hour3[0], 1), round(hour3[1], 1))
    hour4 = model(temp_humidity, current_time + 3600 * n_hours*4)
    hour4 = (round(hour4[0], 1), round(hour4[1], 1))

    preds = [current, hour1, hour2, hour3, hour4]

    return render_template('index.html', preds = preds, current_day = current_day(), current_date = current_date(), next = next_4_hours())


if __name__ == '__main__':
    app.run(debug=True)
