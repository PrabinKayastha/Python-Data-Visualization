from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# Create TWO 6 faced die.
die_1 = Die()
die_2 = Die()


# Store the results of 100 rolls.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the result.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_val = list(range(2, max_result + 1))
data = [Bar(x=x_val, y=frequencies)]

x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config = {'title':'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 1000 times.', xaxis = x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout':my_layout}, filename='d6_d6.html')

print(frequencies)