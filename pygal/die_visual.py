from die import Die
from pygal import Bar


#Creates a D6 (D6 == die of 6 sides)
die = Die()

times = 1000

#Roll the die and store the results in a list
results = []
for roll_num in range(times):
    result = die.roll()
    results.append(result)
    
    
#Analize the results
frequencies = []
for value in range(1, die.sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

    
#Visualizes the results
hist = Bar()

hist.title = 'Results of rolling one D6 ' + str(times) + ' times'
hist.x_labels = [str(i) for i in range(1, 7)]
hist.x_title = 'Sides'
hist.y_title = 'Frequency of Side'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')