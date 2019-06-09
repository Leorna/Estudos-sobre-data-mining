from die import Die
from pygal import Bar

die_1 = Die(8)
die_2 = Die(8)

times = 1000000

results = [die_1.roll() + die_2.roll() for _ in range(times)]

max_result = die_1.sides + die_2.sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

hist = Bar()

hist.title = 'Roll of a D8 and a D8 ' + str(times) + ' times'
hist.x_labels = [str(i) for i in range(2, max_result+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D8 + D8', frequencies)
hist.render_to_file('d8.svg')