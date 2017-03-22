"""Create dataframe with zipcode, GPS coords. and city name"""
import pandas as pd
import pickle_funcs as pk
import zipcode
from pyzipcode import ZipCodeDatabase
from geopy.geocoders import Nominatim

def get_city_data_geopy(zipc):
    """Given a zip code, return latlon and city name"""
    geolocator = Nominatim()
    coord_data = geolocator.geocode(str(zipc))
    name_data = zipcode.isequal(str(zipc))

    if coord_data is not None and name_data is not None:
        lat = coord_data[1][0]
        lon = coord_data[1][1]
        name = '%s, %s' % (name_data.city, name_data.state)
        return lat, lon, name
    # Some data points are empty, return string of none in this case
    else:
        return 'None', 'None', 'None'

def get_city_data(zipc):
    """Given a zip code, return latlon and city name"""
    geolocator = ZipCodeDatabase()
    try:
        zip_data = geolocator[str(zipc)]
        lat = zip_data.latitude
        lon = zip_data.longitude
        name = '%s, %s' % (zip_data.city, zip_data.state)
        return lat, lon, name

    except:
        return 'None', 'None', 'None'


def strip_chars(string):
    """Returns a string with only ints"""
    string = str(string)
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
    print('data read')

    lat_dict = {}
    lon_dict = {}
    name_dict = {}

    data['zipcode'] = data['zipcode'].apply(strip_chars)
    print('zipcode modified')

    for zipc in data['zipcode']:
        city_data = get_city_data(zipc)
        lat_dict[zipc] = city_data[0]
        lon_dict[zipc] = city_data[1]
        name_dict[zipc] = city_data[2]

    print('looked up zipcode data')

    def dict_lookup(zipcode, dict_name):
        return dict_name[zipcode]

    data['lats'] = data['zipcode'].apply(dict_lookup, args=(lat_dict,))
    print('input lats data')
    data['lons'] = data['zipcode'].apply(dict_lookup, args=(lon_dict,))
    print('input lons data')
    data['city names'] = data['zipcode'].apply(dict_lookup, args=(name_dict,))
    print('input city name data')


    # Create pickle object from the dataframe
    pk.pickle_object(data, 'error_data', test=False)

    return data












