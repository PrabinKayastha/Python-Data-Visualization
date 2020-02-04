import json


# Explore the structure of data.
filename = "data/mapping_global_data_sets/data/eq_data_1_day_m1.json"

with open(filename, 'r') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(list(zip(mags, lons, lats)))