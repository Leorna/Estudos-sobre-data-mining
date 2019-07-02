import csv
from matplotlib import pyplot as plt
from datetime import datetime as DateTime


def store_data(dates, highs, lows, row):
    try:
        current_date = DateTime.strptime(row[0], '%Y-%m-%d')
        high = int(row[1])
        low = int(row[3])
    except:
        print('Missing', current_date)
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
            
            
def plot_data(dates, highs, lows):            
    fig = plt.figure(dpi=128, figsize=(10, 5))
    plt.plot(dates, highs, c='red', alpha=0.7)
    plt.plot(dates, lows, c='blue', alpha=0.7)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
    format_graphic(fig)


def format_graphic(fig):
    plt.title('High and low temperatures in Death Valley CA - 2014', fontsize=20)
    plt.xlabel('', fontsize=15)
    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)', fontsize=15)
    plt.tick_params(axis='both', labelsize=16)
    
    
filename = 'death_valley_2014.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        store_data(dates, highs, lows, row)
     
            
    plot_data(dates, highs, lows)
    plt.show()
    
 