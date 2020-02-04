import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Explore the structure of data.
filename = "data/mapping_global_data_sets/data/eq_data_30_day_m1.json"

with open(filename, 'r') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    hover_text = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(hover_text)

# Map the earthquakes.
data = [Scattergeo(lon=lons, lat=lats, text=hover_texts, marker= {'size' : [5*mag for mag in mags], 'color':mags, 'colorscale':'Viridis', 'reversescale':True, 'colorbar':{'title':'Magnitude'}})]
my_layout = Layout(title='Global Earthquakes')

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='output-files/global_earthquakes.html')