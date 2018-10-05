import pygal
from Die import Die

# Create a D6
die = Die()

# Make some rolls, then store results in a list
results = []
for num_roll in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling 1 die 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
