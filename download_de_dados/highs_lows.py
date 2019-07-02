import csv
from matplotlib import pyplot as plt
from datetime import datetime as DateTime


#Gets the max temperatures of the file
#filename = 'sitka_weather_07-2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = DateTime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
    
#Make the plot of the data
fig = plt.figure(dpi=128, figsize=(10, 6))

color_highs = 'red'
color_lows = 'blue'
plt.plot(dates, highs, c=color_highs, alpha=0.5)
plt.plot(dates, lows, c=color_lows, alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Formats the graphic
title = 'Daily high and low temperatures - 2014\nDeath Valley, CA'
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', labelsize=16)

plt.show()        
