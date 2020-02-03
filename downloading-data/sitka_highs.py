#%%
import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = '../data/the_csv_file_format/data/sitka_weather_2018_simple.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # get high temperatures from the file.
    date_temp_highs = []
    for row in reader:
        high = (row[2], row[5])
        date_temp_highs.append(high)

# print(date_temp_highs)

dates = [datetime.strptime(i[0], '%Y-%m-%d') for i in date_temp_highs]
max_temp = [i[1] for i in date_temp_highs]

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
ax.plot(dates, max_temp, c='Red')

# Format plot
ax.set_title('Daily high temperatures, 2018', fontsize=24)
ax.set_xlabel('Dates 2018:', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temperatures:', fontsize = 16)
ax.tick_params(axis='both', which= 'major', labelsize=10)
plt.show()

# %%
