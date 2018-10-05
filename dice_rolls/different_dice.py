import pygal
from Die import Die

# Create a D6
die_1 = Die()
die_2 = Die(10)

# Make some rolls, then store results in a list
results = []
for num_roll in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling 2 D6 dice 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
    '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')
