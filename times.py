import datetime


def current_date():
    current_time = datetime.datetime.now().strftime("%d %b %Y")
    return current_time


def current_day():
    current_day = datetime.datetime.now().strftime("%A")
    return current_day


# function to give an array of times of the next 4 hours as 2:00 AM Format in an increment of 2 hours
def next_4_hours():
    next_4_hours = []
    for i in range(0, 9, 2):
        next_4_hours.append((datetime.datetime.now() + datetime.timedelta(hours=i)).strftime("%I:00 %p"))
    return next_4_hours
