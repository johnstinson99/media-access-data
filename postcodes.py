import csv
import json
first_names = {'m':[], 'f':[]}  # Make any name other.

postcodes = []
postcodes_json = ''
with open('C:\\Users\\John\\Documents\\2016\\SQL Training 2016 Unicom\\Datasets\\postcodes_summarised\\postcodes_all.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|') #DictReader uses first column as the key
    for row in reader:
        print(row)
        postcodes.append(row)
        postcodes_json += json.dumps(row)

print(postcodes[0:30])
print(postcodes_json)
#print(postcodes)

with open ('C:\\Users\\John\\Documents\\2016\\SQL Training 2016 Unicom\\Datasets\\output_files\\postcodes.json', 'w') as outfile:
    outfile.write(postcodes_json)

'''
first_names_o = first_names.get('m') + first_names.get('f')
first_names['o'] = first_names_o
# print(first_names)

def rnd_m_f_o():  #male, female or other
    m_to_f_ratio = .491
    other_ratio = .03 #.01 = 1%
    m_plus_f_ratio = 1 - other_ratio
    m_ratio = m_plus_f_ratio * m_to_f_ratio    # f_ratio = 1 - m_ratio - other_ratio
    # print(m_ratio, f_ratio, other_ratio)
    rnd = random.random()
    # print(rnd)
    if rnd < m_ratio:
        return 'm'
    elif rnd < m_plus_f_ratio:
        return 'f'
    else:
        return 'o'

def rnd_first_name_m_f_o(m_f_o):

    rnd = random.random()
    name_list = first_names.get(m_f_o)
    my_len = len(name_list)
    position = int(rnd * my_len)
    return name_list[position]

def rnd_last_name():
    rnd = random.random()
    position = int(rnd * len(last_names))
    return last_names[position]

def rnd_age_start_end(start_yrs, end_years):
    rnd = random.random()
    age_diff = end_years - start_yrs
    age = start_yrs + age_diff*rnd
    return age

def rnd_age():
    age_under_16 = 0
    age_under_35 = .45 + age_under_16
    age_under_55 = .37 + age_under_35
    rnd = random.random()
    if rnd < age_under_35:
        return rnd_age_start_end(16, 35)
    elif rnd < age_under_55:
        return rnd_age_start_end(35,55)
    else:
        return rnd_age_start_end(55, 100)

def get_date_of_birth(age):
    today_datetime = datetime.combine(date.today(), time()) #convert to datetime so we can do datetime maths
    birthday_datetime = today_datetime + timedelta(days = -age*365.25) #subtract days to get new datetime. No years option.
    birthday = birthday_datetime.date()
    return birthday

def get_user_id(i):
    start_num = 12345
    return i + start_num

# postcode_area_region
postcode_area_region_list_of_dicts = []
with open('C:\\Users\\John\\Documents\\2016\\SQL Training 2016 Unicom\\Datasets\\postcodes_summarised\\postcode_area_region.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
        postcode_area_region_list_of_dicts.append(row)
        # print(row)
        # postcode_area_code = row['postcode_area_code']
        # print(postcode_area_code)

# postcode_district_area
postcode_district_area_list_of_dicts = []
postcode_district_area_list_of_population_tuples = []
with open('C:\\Users\\John\\Documents\\2016\\SQL Training 2016 Unicom\\Datasets\\postcodes_summarised\\postcode_district_area.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
        # print(row)
        postcode_district_area_list_of_dicts.append(row)
        postcode_district = row['postcode_district']
        population_cum_pct = float(row['population_cum_pct'])
        postcode_district_area_list_of_population_tuples.append((population_cum_pct, postcode_district))
        # print(postcode_district, population_cum_pct)

# print(postcode_district_area_list_of_population_tuples)

def get_rnd_postcode_district():
    rnd = random.random()
    for cum_pct, postcode_district in postcode_district_area_list_of_population_tuples:
        # print(rnd)
        #
        # print(cum_pct, postcode_district)
        if rnd < cum_pct:
             return postcode_district

def date_to_string(my_date):
    return my_date.strftime('%Y-%m-%d')

def rnd_direct_email():
    rnd = random.random()
    if rnd < 0.25:
        return 1
    else:
        return 0



user_list = []
json_string = ''
for i in range(1,100000):
    user_id = get_user_id(i)
    gender = rnd_m_f_o()
    first_name = rnd_first_name_m_f_o(gender)
    last_name = rnd_last_name()
    age = rnd_age()
    date_of_birth_string = date_to_string(get_date_of_birth(age))
    postcode_district = get_rnd_postcode_district()
    email_address = first_name.lower() + '.' + last_name.lower() + get_random_email_extension()
    direct_email_ok = rnd_direct_email()
    dict = {'user_id': user_id,
            'gender': gender,
            'first_name': first_name,
            'last_name': last_name,
            'date_of_birth_string': date_of_birth_string,
            'postcode_district': postcode_district,
            'email_address': email_address,
            'direct_email_ok': direct_email_ok}
    user_list.append(dict)
    json_string += (json.dumps(dict))

# print(user_list)

# print (user_id, first_name, last_name, gender, date_of_birth, postcode_district)
# json_data = json.dumps(user_list)  # [{..},{..}, ...]  --copy doesn't recognize commas
# json_data_no_square_brackets = json_data[1:-1]  # {..},{..}, ...
# print(json_data_no_square_brackets)

# json_user_list = json.dumps(user_list)
with open ('C:\\Users\\John\\Documents\\2016\\SQL Training 2016 Unicom\\Datasets\\output_files\\user_list.json', 'w') as outfile:
    outfile.write(json_string)
    # json.dump(user_list, outfile)

with open ('C:\\Users\\John\\Documents\\2016\\SQL Training 2016 Unicom\\Datasets\\output_files\\user_list_true_json.json', 'w') as outfile:
    # outfile.write(json_string)
    json.dump(user_list, outfile)
    '''