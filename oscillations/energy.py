import matplotlib.pyplot as plt

from core.particle import Particle
from core.force import SpringForce
from core.integrators import EulerCromerIntegrator
from core.system import System


def run():
    # -----------------------------
    # 1. Create particle
    # -----------------------------
    particle = Particle(
        mass=1.0,
        position=[1.0],
        velocity=[0.0]
    )

    # -----------------------------
    # 2. Define force and integrator
    # -----------------------------
    spring = SpringForce(k=1.0)
    integrator = EulerCromerIntegrator()

    # -----------------------------
    # 3. Create system
    # -----------------------------
    system = System(
        particle=particle,
        force=spring,
        integrator=integrator,
        dt=0.01
    )

    # -----------------------------
    # 4. Data storage
    # -----------------------------
    time_data = []
    kinetic_energy = []
    potential_energy = []
    total_energy = []
    position_data = []

    t = 0.0

    # -----------------------------
    # 5. Time evolution
    # -----------------------------
    for _ in range(2000):
        x = particle.position[0]
        v = particle.velocity[0]

        K = 0.5 * particle.mass * v**2
        U = 0.5 * spring.k * x**2
        E = K + U

        time_data.append(t)
        kinetic_energy.append(K)
        potential_energy.append(U)
        total_energy.append(E)
        position_data.append(x)

        system.step()
        t += system.dt

    # -----------------------------
    # 6. Plot energies vs time
    # -----------------------------
    plt.figure(figsize=(10, 6))

    plt.plot(time_data, kinetic_energy, label="Kinetic Energy")
    plt.plot(time_data, potential_energy, label="Potential Energy")
    plt.plot(time_data, total_energy, label="Total Energy", linewidth=2)

    plt.xlabel("Time")
    plt.ylabel("Energy")
    plt.title("Energy Variation in Simple Harmonic Motion")
    plt.legend()
    plt.grid(True)
    plt.show()
