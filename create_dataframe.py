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


def map_zipcode(csvfilename):
    """Create a dataframe with zipcodes, GPS coords., and population"""
    
    # Read CSV file as a dataframe
    data = pd.read_csv('%s.csv', csvfilename)

    # Create blank columns in the dataframe
    blanks = []
    for k in range(len(data)):
        blanks.append('None')
    data['lats'] = pd.Series(blanks)
    data['lons'] = pd.Series(blanks)
    data['city names'] = pd.Series(blanks)

    latitudes = []
    longitudes = []
    city_names = []

    # Get city data for each zip code
    for zipc in data['Zip Code ZCTA']:
        data_tuple = get_city_data(zipc)
        latitudes.append(data_tuple[0])
        longitudes.append(data_tuple[1])
        city_names.append(data_tuple[2])

    # TODO This is inefficient, should be able to use one loop
    # Input city data into the dataframe
    for k in range(len(data)):
        data.iloc[k,2] = latitudes[k]
        data.iloc[k,3] = longitudes[k]
        data.iloc[k,4] = city_names[k]

    # Create pickle object from the dataframe
    pk.pickle_object(data, 'city_coords', test=False)










