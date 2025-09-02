# HydroSimCLXI
Lightweight math playground for shallow-water and advection-diffusion equations.


### To-do
- [x] Develop repo structure (src, examples)
- [x] Implement 1D advection solver
- [x] 1D Benchmarking + CFL stability demo
- [ ] Build into 2D scalar transport
- [ ] Shallow-water equations
- [ ] Write notes ("CFD-Notes")


## Results (a): 1D Advection (Upwind)
Moves a simple shape to the right with constant speed.
Upwind is stable at `|c·Δt/Δx| ≤ 1`, but smears sharp edges over time (diffusion).

![1D advection](assets/TBD.png) # replace with file name

**How to run:**
```bash
python -m examples.run_advection_1d
```


*Takeaway:* Stability isn’t accurate in detail. Upwind keeps the solution less volatile but forsakes precision. Next method should use a less diffusive scheme.
