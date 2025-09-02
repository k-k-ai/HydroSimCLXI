# src/viz.py
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt

def new_fig(title:str, xlabel: str, ylabel: str, figsize=(8, 4)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.25) # structure
    return fig, ax

def save_fig(fig, outdir="assets", stem="figure", dpi=160):
    Path(outdir).mkdir(exist_ok=True)
    fname = Path(outdir) / f"{stem}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    fig.tight_layout()
    fig.savefig(fname, dpi=dpi)
    return fname