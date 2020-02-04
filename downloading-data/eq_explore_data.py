import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from pprint import pprint


# Explore the structure of data.
filename = "data/mapping_global_data_sets/data/eq_data_30_day_m1.json"

with open(filename, 'r') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']


mags = [mag['properties']['mag'] for mag in all_eq_dicts]
lons = [lon['geometry']['coordinates'][0] for lon in all_eq_dicts]
lats = [lat['geometry']['coordinates'][1] for lat in all_eq_dicts]
hover_texts = [hover_text['properties']['title'] for hover_text in all_eq_dicts] 
 

# Map the earthquakes.
data = [Scattergeo(lon=lons, lat=lats, text=hover_texts, marker= {'size' : [5*mag for mag in mags], 'color':mags, 'colorscale':'Viridis', 'reversescale':True, 'colorbar':{'title':'Magnitude'}})]
my_layout = Layout(title=all_eq_data['metadata']['title'])

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='output-files/global_earthquakes.html')