import numpy as np
import matplotlib.pyplot as plt
import time
import simulate as sim

"""
Initial attempt: 3 Ar particles in 2D
=====================================
STEPS:
1. Initialize uniformly random velocity and position 
(it should be fcc for positions and Maxwell distribution for velocities)
2. Force calculation using the Lennard-Jones potential
3. Euler method for time evolution
4. Periodic boundary condition
5. Check momenta and energy conservation
(another check can be time reversibility)

UNITS: in International System
"""

# Input parameters
N = 10 # number of particles
L = 1E-6 # box length
T = 300 # temperature
time_step = 1E-11 # time-step
run_time = 1E-9 # run time of the simulation
Niter = 100 # number of times the simulation is run

# Velocity and Position initialization (uniformly random)
pos = L*np.random.rand(N, 2)
vel = np.sqrt(sim.KB*T/sim.MASS) - 2*np.sqrt(sim.KB*T/sim.MASS)*np.random.rand(N, 2)

# Total energy storage vector
tot_energy=[]

# Simulation

for t in range(Niter): # temporal loop to check that simulate.py works
    pos, vel = sim.simulate(pos,vel,int(run_time/time_step),time_step,L)
    tot_energy += [sim.total_energy(pos, vel, L)] 

# Plotting the energy to check conservation
ax = plt.axes()
plt.plot(np.linspace(0, Niter, len(tot_energy)),tot_energy)
plt.show()

