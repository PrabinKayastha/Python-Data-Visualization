#%%
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
ax.scatter(2, 4)

# Set the title chart and label axis.
ax.set_title('Squares scatter plot.', fontsize = 25)
ax.set_xlabel("Value", fontsize  =15)
ax.set_ylabel("Square of Value", fontsize  =15)


# Change the sixe of ticks in label.
ax.tick_params(axis='both', labelsize=15)


plt.show()

# %%
