from plot_eigen_energies import plot_eigen_energies
from diabatic_basis import run_diabatic_basis
from adiabatic_basis import run_adiabatic_basis
from compare_results import compare_results

if __name__ == "__main__":
    print("Plotting Eigen-Energies...")
    plot_eigen_energies()

    print("Running Diabatic Basis Analysis...")
    run_diabatic_basis()

    print("Running Adiabatic Basis Analysis...")
    run_adiabatic_basis()

    print("Comparing Results...")
    compare_results()
