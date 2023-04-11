import datetime


# get current date after adding 9:30 hours
def current_date():
    current_date = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)
    return current_date.strftime("%d %B %Y")


# get current day after adding 9:30 hours
def current_day():
    current_day = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)
    return current_day.strftime("%A")


# function to give an array of times of the next 4 hours as 2:00 AM Format in an increment of 2 hours after adding 9:30 hours initially
def next_4_hours():
    next_4_hours = []
    current_time = datetime.datetime.now() + datetime.timedelta(hours=5, minutes=30)
    for i in range(5):
        next_4_hours.append((current_time + datetime.timedelta(hours=2 * i)).strftime("%I:00 %p"))
    return next_4_hours
