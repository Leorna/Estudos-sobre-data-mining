from die import Die 
from pygal import Bar


#Creates a D6 and a D10
die_1 = Die()
die_2 = Die(10)

#Roll the dice some times and stores it in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
#Analise the results 
max_result = die_1.sides + die_2.sides   
frequencies = []
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
    
hist = Bar()

hist.title = 'Result of rolling a D6 and a D10 50.000 times'
hist.x_labels = [str(i) for i in range(2, max_result+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('different_dice_visual.svg')

sum = 0
for frequency in frequencies:
    sum += frequency
    
    
print(sum)