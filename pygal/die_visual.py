from die import Die
from pygal import Bar


#Creates two D6 dice (D6 == die of 6 sides)
die = Die()

times = 1000

#Roll the die and store the results in a list
results = [die.roll() for roll_num in range(times)]
    
#Analize the results
frequencies = [results.count(value) for value in range(1, die.sides+1)]
    
#Visualizes the results
hist = Bar()

hist.title = 'Results of rolling one D6 die ' + str(times) + ' times'
hist.x_labels = [str(i) for i in range(1, 7)]
hist.x_title = 'Sides'
hist.y_title = 'Frequency of Side'

#add will add automatically the y_labels
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')