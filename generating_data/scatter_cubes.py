#%%
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

x_val = [x for x in range(5000)]
y_val = [x**3 for x in x_val]

fig, ax = plt.subplots()
ax.scatter(x_val, y_val, c=y_val, cmap=plt.cm.Greys, s=15)

ax.set_title('Cube scatterplots', fontsize = 25)
ax.set_xlabel('x_val', fontsize = 15)
ax.set_ylabel('y_vals = x_vals cubed', fontsize = 15)

ax.tick_params(axis='both', which = 'major', labelsize = 15)

plt.show()

# %%
