# File: src/advection1d.py
# Author: Kai
# Date: 2025-08-31


import numpy as np

def upwind_advection(u0c, c, dx, dt, steps, periodic=True):
    """
    Solve u_t + c u_x = 0 with first-order upwind.
    u0: 1D array initial condition
    c: wave speed (float, can be +/-)
    dx, dt: spacings
    steps: number of time steps
    periodic: periodic BC if True, else clamp endpoints
    Returns: u (final), history (list of snapshots, optional small)
    """
    u = np.asarray(u0c, dtype=float).copy()
    n = u.size
    sigma = c * dt / dx  # CFL number

    if abs(sigma) > 1.0:
        raise ValueError(f"CFL too large: |c*dt/dx| = {abs(sigma):.3f} > 1.0 (unstable).")

    hist = []
    # snapshots (start, middle, end)
    save_every = max(1, steps // 4)

    for k in range(steps):
        if c >= 0:
            u_left = np.roll(u, 1) if periodic else np.concatenate([[u[0]], u[:-1]])
            u_new = u - sigma * (u - u_left)
        else:
            u_right = np.roll(u, -1) if periodic else np.concatenate([u[1:], [u[-1]]])
            u_new = u - sigma * (u_right - u)

        u = u_new

        if k % save_every == 0 or k == steps - 1:
            hist.append(u.copy())

    return u, hist
