#%%
from matplotlib import pyplot as plt

from random_walk import RandomWalk

# Generate the random walks as long as the program is active
while True:
    # Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in a walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values,c=point_numbers, cmap=plt.cm.Blues, edgecolors='None', s = 5)

    # Emphasize the starting and ending points.
    ax.scatter(rw.x_values[0], rw.y_values[0],c='Green', edgecolors='None', s = 100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],c='Red', edgecolors='None', s = 100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    plt.show()

    keep_running = input('Make another walk? (y/n) :')
    if keep_running.lower() == 'y':
        print('Generating new random walk.')
        continue
    else:
        if keep_running.lower() == 'n':
            print('Exiting the walk.')
        break



# %%
