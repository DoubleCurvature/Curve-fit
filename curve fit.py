#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the form of the function to fit
def func(x, a, b, c, d):
    return a * np.sin(b * x + c) + d

# y-coordinates
y_data = np.array([
    13.21, 13.24, 13.24, 13.15, 13.09, 12.96, 12.84, 12.75, 12.57, 12.35, 
    12.17, 11.92, 11.71, 11.43, 11.19, 10.91, 10.61, 10.3, 10, 9.69, 9.42, 
    9.08, 8.77, 8.47, 8.13, 7.86, 7.55, 7.28, 6.97, 6.73, 6.51, 6.27, 6.15, 
    5.9, 5.72, 5.56, 5.41, 5.32, 5.26, 5.23, 5.2, 5.2, 5.23, 5.26, 5.38, 
    5.5, 5.56, 5.75, 5.87, 6.15, 6.33
])

# Generate x-coordinates. This assumes that x-coordinates are evenly spaced.
x_data = np.linspace(0, 2*np.pi, len(y_data))  # or np.arange(len(y_data)) if not 0-2pi

# Use curve_fit to find the optimal parameters
popt, pcov = curve_fit(func, x_data, y_data)
perr = np.sqrt(np.diag(pcov))
conf_int = [popt - 1.96*perr, popt + 1.96*perr]

# Generate a fine x-coordinate grid for plotting the fit
x_fine = np.linspace(0, 2*np.pi, 1000)  # or np.linspace(0, len(y_data), 1000)
plt.figure(figsize=(30, 6))  # Adjust the width and height as needed

# Plot the data and the fit
plt.figure(figsize=(25, 6))
plt.scatter(x_data, y_data, label='data')
plt.plot(x_fine, func(x_fine, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f, d=%5.3f' % tuple(popt))
plt.legend(fontsize='xx-large')
plt.show()
# fitted parameters are in the 'popt' array. access them like this:
a, b, c, d = popt
residuals = y_data - func(x_data, *popt)
rmse = np.sqrt(np.mean(residuals**2))
print(f'Root Mean Squared Error: {rmse:.3f}')

# Print out the equation with these values
print(f'y = {a:.3f} * sin({b:.3f} * x + {c:.3f}) + {d:.3f}')



























# In[ ]:





# In[ ]:




