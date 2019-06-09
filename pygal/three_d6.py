from gen import gen_results
from pygal import Bar



times = 5000000


results = [result for result in gen_results(times)]

max_result = 3 * 6
frequencies = [results.count(value) for value in range(3, max_result+1)]


hist = Bar()
hist.title = 'Roll of three D6 ' + str(times) + ' times'
hist.x_labels = [str(i) for i in range(3, max_result+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('three_d6_visual.svg')





