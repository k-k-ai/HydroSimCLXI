# examples/animate_advection_1d.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from src.advection1d import upwind_advection

# grid
L = 1.0
nx = 400
x = np.linspace(0, L, nx, endpoint=False)
dx = x[1] - x[0]

# initial condition: pulse + gaussian
u = np.zeros_like(x)
u[(x > 0.2) & (x < 0.35)] = 1.0
u += 0.6 * np.exp(-((x - 0.65) ** 2) / (2 * (0.03 ** 2)))
u0 = u.copy()

# numerics
c = 1.0
cfl = 0.9
dt = cfl * dx / abs(c)

# set up figure
fig, ax = plt.subplots(figsize=(8, 4))
(line_start,) = ax.plot(x, u0, lw=2, label="start")
(line_live,) = ax.plot(x, u, lw=1.5, label="live")
ax.set_title("1D Advection — live upwind")
ax.set_xlabel("x")
ax.set_ylabel("u")
ax.grid(True, alpha=0.25)
ax.legend(loc="upper right")
txt = ax.text(0.02, 0.95, "", transform=ax.transAxes, va="top")

# animation step
def step(frame):
    global u
    # one explicit upwind step (inline to keep it fast)
    sigma = c * dt / dx
    if c >= 0:
        u_left = np.roll(u, 1)
        u = u - sigma * (u - u_left)
    else:
        u_right = np.roll(u, -1)
        u = u - sigma * (u_right - u)

    line_live.set_ydata(u)
    txt.set_text(f"CFL ≈ {abs(sigma):.2f} | frame {frame}")
    return line_live, txt

ani = FuncAnimation(fig, step, frames=600, interval=16, blit=True)  # ~60 FPS
plt.show()
