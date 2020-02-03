#%%

import csv
from datetime import datetime
from matplotlib import pyplot as plt



filename = '../data/the_csv_file_format/data/death_valley_2018_simple.csv'

with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, col_header in enumerate(header_row):
        print(index, col_header)
        

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = float(row[4])
            low = float(row[5])
        except ValueError:
            print('Data not present for {date}')
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, highs, linewidth=1, c='Red', alpha = 0.75)
ax.plot(dates, lows, linewidth=1, c='Blue', alpha = 0.75)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha = 0.1)


ax.set_title('Annual distribution for Death Valley, 2018')
ax.set_xlabel('Dates 2018:', fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel('Temperatures:', fontsize = 16)
ax.tick_params(axis='both', which= 'major', labelsize=10)
plt.show()


# %%
