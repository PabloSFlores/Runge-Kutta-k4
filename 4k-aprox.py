# +-----------------------------+
# Imports
import math
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# +-----------------------------+
# Constants
X_0 = 0
Y_0 = -3

# Steps
H = 1
H_HR= 0.01

# Number of iterations
N = 5

# +-----------------------------+
# Functions
def f(x, y):
    return x + y / 5

def euler_step(x_i, y_i, h, f):
    return y_i + h*f(x_i, y_i)

def rk4_step(x_i, y_i, h, f):
    k1 = f(x_i, y_i)
    k2 = f(x_i + h/2, y_i + k1*h/2)
    k3 = f(x_i + h/2, y_i + k2*h/2)
    k4 = f(x_i + h, y_i + k3*h)
    return y_i + h/6*(k1 + 2*k2 + 2*k3 + k4)

# +-----------------------------+
# Computing approximate results with Euler
x = X_0

ys_euler = [Y_0]
y_euler = Y_0

for i in range(N):
    y_euler = euler_step(x, y_euler, H, f)
    ys_euler.append(y_euler)
    x += H

# +-----------------------------+
# Computing approximate results with Runge-Kutta
x = X_0

ys_rk4 = [Y_0]
y_rk4 = Y_0

for i in range(N):
    y_rk4 = rk4_step(x, y_rk4, H, f)
    ys_rk4.append(y_rk4)
    x += H

# +-----------------------------+
# Computing x values
x = X_0

xs = [X_0]

for i in range(N):
    x += H
    xs.append(x)

# +-----------------------------+
# print(len(xs))
# print(len(ys_exact_p))
# print(len(ys_rk4))
# print(len(ys_euler))
# print(len(rk_abs_errs))
# print(len(rk_rel_errs))
# print(len(rk_rel_errs_p))
# print(len(euler_abs_errs))
# print(len(euler_rel_errs))
# print(len(euler_rel_errs_p))
# Info tables
data_rk = {'x': xs,
        'y(RK4)': ys_rk4}

data_euler = {'x': xs,
        'y(Euler)': ys_euler}

df_rk = pd.DataFrame(data_rk)
df_euler = pd.DataFrame(data_euler)

# Create new window
window = tk.Tk()
window.title("DataFrame Viewer")

# Add a text area to display the DataFrame
txt_area = scrolledtext.ScrolledText(window)
txt_area.insert(tk.INSERT, df_rk)
txt_area.insert(tk.END, '\n\n')
txt_area.insert(tk.INSERT, df_euler)
txt_area.pack(expand=True, fill=tk.BOTH)

# Plotting
plt.plot(xs, ys_rk4, color='red', marker='o', linewidth=0.0, label='RK4')
plt.plot(xs, ys_euler, color='green', marker='o', linewidth=0.0, label='Euler')
plt.legend()

# Show the graphic individualy
plt.show()

# Start the GUI event loop
window.mainloop()