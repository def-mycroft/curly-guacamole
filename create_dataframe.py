"""Create dataframe with zipcode, GPS coords. and city name"""
import pandas as pd
import zipcode
import pickle_funcs as pk

def get_city_data(zipc):
    """Given a zip code, return latlon and city name"""
    data = zipcode.isequal(str(zipc))

    if data is not None:
        lat = data.lat
        lon = data.lon
        name = '%s, %s' % (data.city, data.state)
        return lat, lon, name
    # Some data points are empty, return string of none in this case
    else:
        return 'None', 'None', 'None'


def strip_chars(string):
    """Returns a string with only ints"""
    newstring = ''

    for k in string:

        try:
            a = int(k)
            newstring = newstring + k
        except ValueError:
            pass

    return newstring # Must return string due to leading zeros


def pull_numbers(dataframe, column_name):
    """Extracts numbers from members of a column"""

    for k in range(len(dataframe)):
        dataframe[column_name][k] = strip_chars(dataframe[column_name][k])

    return dataframe


def create_dataframe(csvfilename):
    """Create a dataframe with zipcodes, GPS coords., and population"""
    
    # Read CSV file as a dataframe
    data = pd.read_csv('%s.csv' % csvfilename)
    data = pull_numbers(data, 'zipcode')

    # Create blank columns in the dataframe
    blanks = []
    for k in range(len(data)):
        blanks.append('None')
    data['lats'] = pd.Series(blanks)
    data['lons'] = pd.Series(blanks)
    data['city names'] = pd.Series(blanks)

    # Fill in city data
    for k in range(len(data.index)):
        city_data = get_city_data(data['zipcode'][k])
        data['lats'][k] = city_data[0]
        data['lons'][k] = city_data[1]
        data['city names'][k] = city_data[2]

    # Create pickle object from the dataframe
    pk.pickle_object(data, 'city_coords', test=False)

    return data










