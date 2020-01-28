#%%
import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth = 3)

# Set the title chart and label axis.
ax.set_title("Square Numbers", fontsize = 25)
ax.set_xlabel("Value", fontsize  =15)
ax.set_ylabel("Square of Value", fontsize  =15)

plt.show()


# %%
