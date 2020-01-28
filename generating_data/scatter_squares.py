#%%
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')


x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]


fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=150)

# Set the title chart and label axis.
ax.set_title('Squares scatter plot.', fontsize = 25)
ax.set_xlabel("Value", fontsize  =15)
ax.set_ylabel("Square of Value", fontsize  =15)


# Change the sixe of ticks in label.
ax.tick_params(axis='both', which = 'major',labelsize=15)


plt.show()

# %%
