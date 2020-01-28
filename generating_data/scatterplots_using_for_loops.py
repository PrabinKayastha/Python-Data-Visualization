#%%
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

x_val = [x for x in range(1000)]
y_val = [x**2 for x in x_val]


fig, ax = plt.subplots()
ax.scatter(x_val, y_val, s=25)

ax.set_title('Squares scatterplots', fontsize = 25)
ax.set_xlabel('x_val', fontsize = 15)
ax.set_ylabel('y_vals = x_vals squared', fontsize = 15)


ax.tick_params(axis='both', which = 'major', labelsize = 15)

plt.show()

# %%
