from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# Create 6 faced die.
die = Die()

# Store the results of 100 rolls.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the result.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_val = list(range(1, die.num_sides + 1))
data = [Bar(x=x_val, y=frequencies)]

x_axis_config = {'title':'Result'}
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times.', xaxis = x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6.html')

print(frequencies)