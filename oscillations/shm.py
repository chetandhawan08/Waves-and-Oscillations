import matplotlib.pyplot as plt

from core.particle import Particle
from core.force import SpringForce
from core.integrators import EulerCromerIntegrator
from core.system import System


def run_SHM():
    # -----------------------------
    # 1. Create the particle
    # -----------------------------
    particle = Particle(
        mass=1.0,
        position=[1.0],   # initial displacement
        velocity=[0.0]    # released from rest
    )

    # -----------------------------
    # 2. Define force and integrator
    # -----------------------------
    force = SpringForce(k=1.0)
    integrator = EulerCromerIntegrator()

    # -----------------------------
    # 3. Create the system
    # -----------------------------
    system = System(
        particle=particle,
        force=force,
        integrator=integrator,
        dt=0.01
    )

    # -----------------------------
    # 4. Data storage
    # -----------------------------
    time_data = []
    position_data = []

    t = 0.0

    # -----------------------------
    # 5. Time evolution
    # -----------------------------
    for _ in range(2000):
        time_data.append(t)
        position_data.append(particle.position[0])

        system.step()
        t += system.dt

    # -----------------------------
    # 6. Plot SHM
    # -----------------------------
    plt.plot(time_data, position_data)
    plt.xlabel("Time")
    plt.ylabel("Displacement")
    plt.title("Simple Harmonic Motion")
    plt.grid(True)
    plt.show()
