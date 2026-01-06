import matplotlib.pyplot as plt
from core.particle import Particle
from core.force import SpringForce
from core.system import System
from core.integrators import EulerCromerIntegrator
import numpy as np  


class SHMForce:
    """
    Force for Simple Harmonic Motion:
    F = -m * omega^2 * x
    """

    def __init__(self, omega):
        self.omega = omega

    def compute(self, particle):
        return -particle.mass * (self.omega ** 2) * particle.position


def run():
    print("\n--- Lissajous Figure Generator ---\n")

    # -----------------------------
    # User Inputs
    # -----------------------------
    A1 = float(input("Enter amplitude A1 (x-direction): "))
    A2 = float(input("Enter amplitude A2 (y-direction): "))
    w1 = float(input("Enter angular frequency ω1: "))
    w2 = float(input("Enter angular frequency ω2: "))
    phi = float(input("Enter phase difference φ (in radians): "))

    dt = 0.01
    steps = 5000

    # -----------------------------
    # Create particles
    # -----------------------------
    particle_x = Particle(
        mass=1.0,
        position=[A1],
        velocity=[0.0]
    )

    particle_y = Particle(
        mass=1.0,
        position=[A2 * np.cos(phi)],
        velocity=[-A2 * w2 * np.sin(phi)]
    )

    # -----------------------------
    # Forces
    # -----------------------------
    force_x = SHMForce(w1)
    force_y = SHMForce(w2)

    # -----------------------------
    # Integrator
    # -----------------------------
    integrator = EulerCromerIntegrator()

    # -----------------------------
    # Systems
    # -----------------------------
    system_x = System(particle_x, force_x, integrator, dt)
    system_y = System(particle_y, force_y, integrator, dt)

    # -----------------------------
    # Data storage
    # -----------------------------
    x_data = []
    y_data = []

    # -----------------------------
    # Time evolution
    # -----------------------------
    for _ in range(steps):
        x_data.append(particle_x.position[0])
        y_data.append(particle_y.position[0])

        system_x.step()
        system_y.step()

    # -----------------------------
    # Plot Lissajous figure
    # -----------------------------
    plt.figure(figsize=(6, 6))
    plt.plot(x_data, y_data)
    plt.xlabel("x displacement")
    plt.ylabel("y displacement")
    plt.title("Lissajous Figure")
    plt.grid(True)
    plt.axis("equal")
    plt.show()
