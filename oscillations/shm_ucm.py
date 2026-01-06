import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def run_ucm():
    # -----------------------------
    # 1. Parameters
    # -----------------------------
    A = 1.0
    omega = 2.0
    t = np.linspace(0, 2*np.pi, 300)

    x_circle = A * np.cos(omega * t)
    y_circle = A * np.sin(omega * t)
    x_shm = A * np.cos(omega * t)

    # -----------------------------
    # 2. Figure and axes
    # -----------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # ---- UCM ----
    ax1.set_xlim(-1.5*A, 1.5*A)
    ax1.set_ylim(-1.5*A, 1.5*A)
    ax1.set_aspect("equal")
    ax1.set_title("Uniform Circular Motion")
    ax1.grid(True)

    ax1.plot(x_circle, y_circle, alpha=0.3)
    point_circle, = ax1.plot([], [], "ro")
    projection_line, = ax1.plot([], [], "k--")

    # ---- SHM ----
    ax2.set_xlim(0, t[-1])
    ax2.set_ylim(-1.5*A, 1.5*A)
    ax2.set_title("SHM (Projection of UCM)")
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Displacement")
    ax2.grid(True)

    ax2.plot(t, x_shm, alpha=0.3)
    point_shm, = ax2.plot([], [], "ro")

    # -----------------------------
    # 3. Animation update function
    # -----------------------------
    def update(frame):
        xc = x_circle[frame]
        yc = y_circle[frame]

        point_circle.set_data([xc], [yc])
        projection_line.set_data([xc, xc], [0, yc])
        point_shm.set_data([t[frame]], [x_shm[frame]])

        return point_circle, projection_line, point_shm

    # -----------------------------
    # 4. Create animation (OUTSIDE update!)
    # -----------------------------
    animation = FuncAnimation(
        fig,
        update,
        frames=len(t),
        interval=30,
        blit=False
    )

    plt.show()
