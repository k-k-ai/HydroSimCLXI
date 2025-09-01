# examples/run_advection_1d.py
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

from src.advection1d import upwind_advection

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

# plot
plt.figure(figsize=(8, 4))
plt.plot(x, u0, label="t=0")
labels = ["25%", "50%", "75%", "100%"]
for snap, lab in zip(hist, labels):
    plt.plot(x, snap, label=lab)

plt.title("1D Advection — Upwind scheme (CFL=%.2f)" % (c * dt / dx))
plt.xlabel("x")
plt.ylabel("u")
plt.legend(loc="upper right")
plt.tight_layout()

# save
outdir = Path("assets")
outdir.mkdir(exist_ok=True)
fname = outdir / f"advection1d_demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
plt.savefig(fname, dpi=160)
print(f"Saved figure to {fname.resolve()}")
