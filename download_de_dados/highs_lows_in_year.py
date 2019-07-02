import csv
from matplotlib import pyplot as plt
from datetime import datetime as DateTime


#Gets the dates and max and min temperatures from the file
filename = 'sitka_weather_2014.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = DateTime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        
        high = int(row[1])
        highs.append(high)
        
        low = int(row[3])
        lows.append(low)
        

#Make the plot of the data
fig = plt.figure(dpi=128, figsize=(10, 6))

color_highs = 'red'
color_lows = 'blue'
plt.plot(dates, highs, c=color_highs, alpha=0.5)
plt.plot(dates, lows, c=color_lows, alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Formats the graphic
plt.title('Daily high and low temperatures - 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', labelsize=16)

plt.show() 