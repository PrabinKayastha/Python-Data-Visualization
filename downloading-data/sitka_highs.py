#%%
import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = '../data/the_csv_file_format/data/sitka_weather_2018_simple.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # get high temperatures from the file.
    date_temp_highs_lows = []
    for row in reader:
        date_high_low = (row[2], row[5], row[6])
        date_temp_highs_lows.append(date_high_low)

# print(date_temp_highs)

dates = [datetime.strptime(i[0], '%Y-%m-%d') for i in date_temp_highs_lows]
max_temp = [float(i[1]) for i in date_temp_highs_lows]
min_temp = [float(i[2]) for i in date_temp_highs_lows]
print(list(zip(dates, max_temp, min_temp)))
plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
ax.plot(dates, min_temp, c='Blue', linewidth = 1, alpha=0.75)
ax.plot(dates, max_temp, c='Red', linewidth = 1, alpha=0.75)
plt.fill_between(dates, max_temp, min_temp, facecolor='blue', alpha = 0.1)

# Format plot
ax.set_title('Daily high and low temperature, 2018', fontsize=24)
ax.set_xlabel('Dates 2018:', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temperatures:', fontsize = 16)
ax.tick_params(axis='both', which= 'major', labelsize=10)
plt.show()

# %%
