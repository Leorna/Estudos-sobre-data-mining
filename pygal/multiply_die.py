from die import Die
from pygal import Bar

die_1 = Die()
die_2 = Die()

times = 10**7

results = [die_1.roll() * die_2.roll() for _ in range(times)]


max_result = die_1.sides * die_2.sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

hist = Bar()

hist.title = 'Product among two D6 dice ' + str(times) + ' times'
hist.x_labels = [str(i) for i in range(1, max_result+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 x D6', frequencies)
hist.render_to_file('md.svg')