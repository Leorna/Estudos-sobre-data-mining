from die import Die
from pygal import Bar


#Creates two D6 dice
die_1 = Die()
die_2 = Die()

times = 1000

#Roll the dice one thousand times
results = [die_1.roll() + die_2.roll() for _ in range(times)]

#Analize the results
max_result = die_1.sides + die_2.sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

#Visualize the results
hist = Bar()

hist.title = 'Results of rolling a two D5 dice ' + str(times) + ' times'
hist.x_labels = [str(i) for i in range(2, 13)]
hist.x_title = 'Sum of Sides'
hist.y_title = 'Frequency of Sum'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
