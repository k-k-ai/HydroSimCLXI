# examples/run_advection_1d.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.advection1d import upwind_advection
from src.viz import new_fig, save_fig
import matplotlib.pyplot as plt


# grid
L = 1.0
nx = 400
x = np.linspace(0, L, nx, endpoint=False)
dx = x[1] - x[0]

# initial condition: square pulse + small gaussian
u0 = np.zeros_like(x)
u0[(x > 0.2) & (x < 0.35)] = 1.0
u0 += 0.6 * np.exp(-((x - 0.65) ** 2) / (2 * (0.03 ** 2)))

# physics / numerics
c = 1.0  # positive speed -> right-moving
cfl = 0.9
dt = cfl * dx / abs(c)
T = 0.4  # total time
steps = int(T / dt)

u_final, hist = upwind_advection(u0, c, dx, dt, steps, periodic=True)

# layman-friendly plot
fig, ax = new_fig(
    title="1D Advection (Upwind) - shape drifts right and diffuses",
    xlabel="Position x",
    ylabel="u(x)"
)

# show start
ax.plot(x, u0, linewidth=2, label="Start (t=0)")

# show evenly spaced time slices
labels = ["25% of total time", "50%", "75%", "100% (final)"]
for snap, lab in zip(hist, labels):
    ax.plot(x, snap, linewidth=1.5, label=lab)

# annotatio
ax.annotate(
    f"CFL = {c*dt/dx:.2f}  (|c·Δt/Δx| ≤ 1 → stable)",
    xy=(0.02, 0.95), xycoords='axes fraction',
    va="top"
)

ax.legend(loc="upper right", frameon=True)

# save
fname = save_fig(fig, stem="advection1d_demo")
print(f"Saved: {fname.resolve()}")