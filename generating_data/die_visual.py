from die import Die


# Create 6 faced die.
die = Die()

# Store the results of 100 rolls.
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)