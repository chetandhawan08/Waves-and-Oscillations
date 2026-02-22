# Computational Physics Lab

A small Python app for simulating and visualizing oscillation systems:

- Simple Harmonic Motion (SHM)
- SHM energy analysis
- SHM-UCM relation animation
- Lissajous figures
- Damped oscillator

## Project Structure

```text
computational_physics_lab/
  main.py
  core/
    particle.py
    force.py
    integrators.py
    system.py
  oscillations/
    shm.py
    energy.py
    shm_ucm.py
    lissagous.py
    damping.py
```

## Requirements

- Python 3.9+
- `numpy`
- `matplotlib`

Install dependencies:

```bash
pip install numpy matplotlib
```

## Run

From the project root:

```bash
python main.py
```

Then choose from the menu:

- `1` Simple Harmonic Motion
- `2` Energy analysis
- `3` SHM-UCM relation
- `4` Lissajous figures
- `5` Damped oscillator
- `0` Exit

## Notes

- The file is named `lissagous.py` in this project (spelling kept to match imports in `main.py`).
- Most simulations open a Matplotlib plot window; close the plot to return control to the terminal.

