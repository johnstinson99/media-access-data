import matplotlib.pyplot as plt
# import datetime
# from py.timedict import get_time_dict
from py.timedict import get_x_time_values
from matplotlib.dates import DayLocator, DateFormatter

import numpy
# data_flats1 = list(numpy.random.exponential(5, 10000))
numbers_per_distribution = 10000  #increase to get more values
std_dev = 0.5  # leave this fixed

date_offsets = range(0,-10)
hours_per_day = 24 # hours
bins_per_hour = 1 # 10 second intervals
seconds_per_bin = 60 / bins_per_hour
bins_per_day = hours_per_day * bins_per_hour
bin_numbers = list(range(0, bins_per_day))
days = 5
day_offset_range = range (-days, 0)
total_bins = days*bins_per_day
x_time_values = get_x_time_values(day_offset_range, bins_per_day, seconds_per_bin)


def day_multiplier(day_offset, less_each_day): #-1 -> 1, -2 -> 0.9
    return max(1 + (day_offset+1)*less_each_day, 0.2) # add 1 to day_offset as its max value is -1

params_tv = ['gray', #colour gray  #http://matplotlib.org/examples/color/named_colors.html
             0,  # less_each_day
                          [(1, std_dev, 0.1),   # normal distribution params
                          (2, std_dev, 0.05),   # first param = mean, 2nd param = distribution (small for narrow)
                          (3, std_dev, 0.005),
                          (4, std_dev, 0.005),
                          (5, std_dev, 0.005),
                          (6, std_dev, 0.05),
                          (7, std_dev, 0.1),
                          (8, std_dev, 0.2),
                          (9, std_dev, 0.2),
                          (10, std_dev, 0.2),
                          (11, std_dev, 0.2),
                          (12, std_dev, 0.25),
                          (13, std_dev, 0.3),
                          (14, std_dev, 0.3),
                          (15, std_dev, 0.3),
                          (16, std_dev, 0.4),
                          (17, std_dev, 0.5),
                          (18, std_dev, 0.75),
                          (19, std_dev, 0.8),
                          (20, std_dev, 1),
                          (21, std_dev, 1),
                          (22, std_dev, 0.75),
                          (23, std_dev, 0.25),
                          (24, std_dev, 0.2)]
             ]


params_iPlayer = ['magenta',
                  0.05,
                  [(1, std_dev, .25),
                               (2, std_dev, .1),
                               (3, std_dev, .05),
                               (4, std_dev, .04),
                               (5, std_dev, .04),
                               (6, std_dev, .15),
                               (7, std_dev, .2),
                               (8, std_dev, .3),
                               (9, std_dev, .33),
                               (10, std_dev, .36),
                               (11, std_dev, .38),
                               (12, std_dev, .4),
                               (13, std_dev, .4),
                               (14, std_dev, .4),
                               (15, std_dev, .5),
                               (16, std_dev, .6),
                               (17, std_dev, .7),
                               (18, std_dev, .8),
                               (19, std_dev, .9),
                               (20, std_dev, .9),
                               (21, std_dev, 1.0),
                               (22, std_dev, .95),
                               (23, std_dev, .55),
                               (24, std_dev, .35)]
                  ]

params_internet = ['blue',
                   0,
                   [(1, std_dev, .25),
                    (2, std_dev, .2),
                    (3, std_dev, .12),
                    (4, std_dev, .12),
                    (5, std_dev, .12),
                    (6, std_dev, 0.2),
                    (7, std_dev, .45),
                    (8, std_dev, .8),
                    (9, std_dev, .9),
                    (10, std_dev, .9),
                    (11, std_dev, .9),
                    (12, std_dev, .9),
                    (13, std_dev, .9),
                    (14, std_dev, .9),
                    (15, std_dev, .95),
                    (16, std_dev, .98),
                    (17, std_dev, 1.0),
                    (18, std_dev, .95),
                    (19, std_dev, .9),
                    (20, std_dev, .85),
                    (21, std_dev, .8),
                    (22, std_dev, .75),
                    (23, std_dev, .5),
                    (24, std_dev, .4)]
                   ]

def get_distribution_for_day_offset(day_offset, less_each_day, my_distribution):
    # float in 24 hour range, but may overlap to 25 etc
    list_of_list_data_floats = list([list(numpy.random.normal(a,b, c*numbers_per_distribution * day_multiplier(day_offset, less_each_day))) for (a,b,c) in my_distribution])
   # Use rounding to int to find the bin, rather than something moe complex.
    flattened_data_ints = [int(bins_per_hour * (my_elem % hours_per_day)) for my_list in list_of_list_data_floats for my_elem in my_list]
    return [flattened_data_ints.count(i) for i in bin_numbers]

def get_y_values(less_each_day, my_distribution):
    print (date_offsets)
    result = []
    for day_offset in day_offset_range:
        result += get_distribution_for_day_offset(day_offset, less_each_day, my_distribution)
    return result


# def get_x_values():
#    return [bin_number/bins_per_division for bin_number in bin_numbers]
    #print(x_values)

# time_dict = get_time_dict();
# print (time_dict)

# y_values = get_y_values()
# print("y_values")
# print(y_values)
# x_values = list(range(0,len(y_values)))
# print("x_values")
# print(x_values)
# print(len(x_values))
# print(len(x_time_values))
# print(len(y_values))

# def get_x_values_as_datetimes():
#     return [time_dict.get(bin_number) for bin_number in bin_numbers ]
# print (get_x_values_as_datetimes())

# plt.plot(x_values, y_values)
def draw_plots():

    fig, ax = plt.subplots()
    ax.xaxis.set_major_locator(DayLocator())
    ax.xaxis.set_major_formatter(DateFormatter('%d %b'))  # '%Y-%m-%d'  # Weirdly %b = Mar etc.
    for params in [params_tv, params_iPlayer, params_internet]:
        line_colour, less_each_day, distribution_tuple_list = params
        plt.plot(x_time_values, get_y_values(less_each_day, distribution_tuple_list), line_colour)
    plt.xlabel('time (days)', color='r')
    plt.ylabel('occurrences', color='r')
    plt.title('iPlayer hits', color='r')
    plt.show()

draw_plots()





# Easy when integers as can bin by converting to ints.  use 240 increments, then divide by 10 right at the end.