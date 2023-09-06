from .harmonic_oscillator import create_trajectories as create_trajectories_ho
from .kepler_problem import create_trajectories as create_trajectories_kp
from .coupled_oscillator import create_trajectories as create_trajectories_co
from .double_pendulum_different_energies import choose_trajectories_low_and_high_energies

def create_trajectories(path):
    print("creating harmonic oscillator trajectories")
    create_trajectories_ho(path=path)
    
    print("creating kepler problem trajectories")
    create_trajectories_kp(path=path)
    
    print("creating coupled oscillator trajectories")
    create_trajectories_co(path=path)

    print("choosing double pendulum trajectories")
    choose_trajectories_low_and_high_energies(path=path)
