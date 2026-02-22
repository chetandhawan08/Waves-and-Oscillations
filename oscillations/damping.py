# =======================
# Damping Experiment Controller
# ===============================

import matplotlib.pyplot as plt

from core.particle import Particle
from core.force import DampingForce, SpringForce
from core.integrators import EulerCromerIntegrator


def run_damping():

    print("\n===== Damped Oscillator Experiment =====\n")

    # --------------------------
    # User Input
    # --------------------------
    mass = float(input("Enter mass (kg): "))
    k = float(input("Enter spring constant (N/m): "))
    b = float(input("Enter damping coefficient (kg/s): "))

    initial_position = float(input("Enter initial position (m): "))
    initial_velocity = float(input("Enter initial velocity (m/s): "))

    dt = 0.01
    total_time = float(input("Enter total simulation time: "))
    # --------------------------
    # Determine damping type
    # --------------------------
    b_critical = 2 * (mass * k) ** 0.5
    
    if abs(b - b_critical) < 1e-6:
        print("\nDamping Type: Critical damping")
    elif b < b_critical:
        print("\nDamping Type: Lightly damped (Underdamped)")
    else:
        print("\nDamping Type: Heavily damped (Overdamped)")

    

    # --------------------------
    # Create physics objects
    # --------------------------
    particle = Particle(mass, [initial_position], [initial_velocity])

    spring_force = SpringForce(k)
    damping_force = DampingForce(b)
    integrator = EulerCromerIntegrator()

    # --------------------------
    # Run Simulation
    # --------------------------
    time_data = []
    position_data = []

    t = 0.0
    steps = int(total_time / dt)

    for _ in range(steps):
        time_data.append(t)
        position_data.append(particle.position[0])

        total_force = spring_force.compute(particle) + damping_force.compute(particle)
        integrator.step(particle, total_force, dt)
        t += dt

    # --------------------------
    # Plot Results
    # --------------------------
    plt.plot(time_data, position_data)
    plt.xlabel("Time")
    plt.ylabel("Displacement")
    plt.title("Damped Oscillator")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    run_damping()
