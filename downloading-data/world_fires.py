import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from datetime import datetime


# Explore the structure of data.
filename = "data/mapping_global_data_sets/data/world_fires_1_day.csv"

lons, lats, bright_ti4, hover_texts = [], [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    column_header = next(reader)
    print(column_header)

    for rec in reader:
        lons.append(rec[1])
        lats.append(rec[0])
        bright_ti4.append(rec[2])
        hover_texts.append(rec[5])


    # Map the earthquakes.
data = [Scattergeo(lon=lons, lat=lats, text=['Reported on : '+ hover_text for hover_text in hover_texts], marker= {'size' : 2, 'color':'firebrick', 'colorscale':'Viridis', 'reversescale':True, 'colorbar':{'title':'Magnitude'}})]
my_layout = Layout(title='World Fires!!!')

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='output-files/world_fires.html')