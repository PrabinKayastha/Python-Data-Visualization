#%%
import csv
import matplotlib.pyplot as plt


filename = '..././data/the_csv_file_format/data/"sitka_weather_07_2018_simple.csv"'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # get high temperatures from the file.
    date_temp_highs = []
    for row in reader:
        high = (row[2], row[5])
        date_temp_highs.append(high)

# print(date_temp_highs)

dates = [i[0] for i in date_temp_highs]
max_temp = [i[1] for i in date_temp_highs]

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
ax.plot(dates, max_temp, c='red')

# Format plot
plt.title('Daily high temperatures, July 2018', font=24)
plt.xlabel('date', fontsize = 16)
plt.ylabel('Temperatures', fontsize = 16)
plt.tick_params(axis='both', which='major', lablesize=16)

plt.show()