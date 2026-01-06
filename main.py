# ===============================
# Computational Physics Lab
# Main Controller File
# ===============================

from oscillations.shm import run_SHM
from oscillations.energy import run as run_energy
from oscillations.shm_ucm import run_ucm as run_shm_ucm
from oscillations.lissagous import run as run_lissajous


def main():
    print("\n===============================")
    print("  Computational Physics Lab")
    print("===============================\n")

    print("1 → Simple Harmonic Motion (SHM)")
    print("2 → Energy analysis of SHM")
    print("3 → SHM–UCM relation (static plots)")
    print("4 → Lissajous Figures (perpendicular SHMs)")
    print("0 → Exit\n")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice == 1:
        run_SHM()

    elif choice == 2:
        run_energy()

    elif choice == 3:
        run_shm_ucm()

    elif choice == 4:
        run_lissajous()

    elif choice == 0:
        print("Exiting program. Goodbye!")

    else:
        print("Invalid choice. Please enter a number between 0 and 5.")


if __name__ == "__main__":
    main()
