from datetime import datetime
from datetime import timedelta
from datetime import date
from datetime import time

# timediff = timedelta(days = 1)
# print(timediff.total_seconds())
# unit = 3600
# print (unit)
# bins_in_hour = 24*60
# datetime_now = datetime.now()

# print(midnight_datetime)

# bin_no = 120 # 12 hours
# new_time = midnight_datetime + timedelta(days = -1, minutes = bin_no)
# print(new_time)


'''
# Dict doesn't work too well as need both date and time as keys
def get_time_dict(day_offset_range):
    time_dict = {}
    day_counter = 0
    for day_offset in day_offset_range:
        for time_bin in range(0,60*24 + 1):  # values every second, although chart plots every 10s
            time_dict[time_bin + day_counter] = convert_to_time(day_offset, time_bin)
        day_counter += 60*24
    # print (time_dict)
    return time_dict'''

midnight_datetime = datetime.combine(date.today(), time())
def convert_to_time(day_offset, bin_no):
    return midnight_datetime + timedelta(days = day_offset, minutes = bin_no)

def get_x_time_values(day_offset_range, bins_per_day, seconds_per_bin):
    time_list = []
    for day_offset in day_offset_range:
        for time_bin in range(0,bins_per_day):
            time_list.append(convert_to_time(day_offset, time_bin*seconds_per_bin))
    # print(time_list)
    return time_list

# get_time_dict(range(-3,0))
# get_x_time_values(range(-3,0),24*6, 10)