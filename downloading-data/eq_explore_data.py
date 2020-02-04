import json


# Explore the structure of data.
filename = "data/mapping_global_data_sets/data/eq_data_1_day_m1.json"

with open(filename, 'r') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))