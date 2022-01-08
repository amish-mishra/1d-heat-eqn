import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


# Initialize data
L = 1   # length of rod
T = .2 # time interval
k = 1   # constant
N = 20  # number of points in space (don't exceed more than 20 or 30)
M = 200  # number of time steps-
dx = L/N
dt = T/M
alpha = k*dt/(dx**2)

# Initial Condition
f = lambda x: (-x**4+x)
# f = lambda x: np.sin(np.pi*x)*np.cos(10*x)
# f = lambda x: np.tan(3*x)
# f = lambda x: CREATE YOUR OWN
left_IC = 0
right_IC = 0
#--------------------------------------------------
# Position
x = np.empty(N+1)
for i in range(N+1):
    x[i] = i*dx

u0 = np.empty(N+1)
for i in range(N+1):
    u0[i]=f(x[i])

# Partial Difference Equation (Numerical Scheme)
heat_grid = np.zeros((M,N+1))   # put evolution of heat solution in a grid
u1 = np.empty(N+1)
for j in range(M):
    for i in range(1,N):
        u1[i] = u0[i]+alpha*(u0[i+1]-2*u0[i]+u0[i-1])
    u1[0]=left_IC     # Left boundary condition
    u1[N] = right_IC   # Right boundary condition
    heat_grid[M-1-j,:] = u1
    u0 = u1     # move to computing next row (increment time position by 1)


# Plotting
fig = plt.figure()
plt.subplots_adjust(bottom=0.25)
ax = fig.subplots()
plt.xlabel("Position on rod (x)")
plt.ylabel("Value of u(x,t)")
plt.title("Evolution of Heat equation solution as time passes")
p, = ax.plot(x, heat_grid[M-1,:], 'r')

# Defining the Slider button
# xposition, yposition, width and height
ax_slide = plt.axes([0.25, 0.1, 0.65, 0.03])

# Properties of the slider
s_factor = Slider(ax_slide, 'Time evolution',
                  dt, T, valinit=dt, valstep=dt)

# Updating the plot
def update(val):
    current_v = s_factor.val
    time_index = int(current_v/dt)
    p.set_ydata(heat_grid[M-1-time_index])
    #redrawing the figure
    fig.canvas.draw()
    
# Calling the function "update" when the value of the slider is changed
s_factor.on_changed(update)
plt.show()