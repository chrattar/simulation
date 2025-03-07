import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.special import sph_harm
from mpl_toolkits.mplot3d import Axes3D

def plot_wavefunction(n, l, m, grid_size=50):
    """Plot the probability density of hydrogen atom wavefunction."""

    #grid of req values
    theta = np.linspace(0, np.pi, grid_size)
    phi = np.linspace(0, 2*np.pi, grid_size)
    theta, phi = np.meshgrid(theta, phi)

# Sphereical harmonix
    Y = sph_harm(m, l, phi, theta)
    
    #Probs
    prob_density = np.abs(Y)**2
    
    #Convert to cart
    r = prob_density  # Using probability density as radial coordinate
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    
    # Create the 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    surf = ax.plot_surface(x, y, z, cmap=cm.viridis, alpha=0.8) #Surfcam plotting conditions
    
 #formt chart
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='Probability Density')
    ax.set_title(f'Hydrogen Atom Wavefunction: n={n}, l={l}, m={m}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    return fig, ax

#I make 1 plot for different eigenstates
fig1, ax1 = plot_wavefunction(n=1, l=0, m=0)  # 1s 
fig2, ax2 = plot_wavefunction(n=2, l=1, m=0)  # 2pz 
fig3, ax3 = plot_wavefunction(n=2, l=3, m=0)  # 2pz 

plt.tight_layout()
plt.show()
