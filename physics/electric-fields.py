import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive

def plot(a, b):
     # centre charge & position
    A_pos = np.array([a,b])
    A_charge = 1.6e-19 # electron

    # constants
    pi = np.pi
    epsilon_nought = 8.85e-12

    def electric_field_strength(pos):
        # Need to include conditions for positive and negative charge to be handled automatically
        d_sqrd = np.linalg.norm(pos) ** 2
        electric_field_strength = (A_charge) / (4 * pi * epsilon_nought * d_sqrd)
        vector_direction = np.array(pos) - A_pos
        norm_vec = vector_direction / np.linalg.norm(vector_direction)
        return electric_field_strength, norm_vec

    B = np.random.uniform(-3, 3, (10000, 2))
    efs, nv = electric_field_strength(B)
    B_quiv = B + nv
    plt.quiver(B[:, 0], B[:, 1], nv[:, 0], nv[:, 1]) #, width=0.002)

    plt.scatter(A_pos[0], A_pos[1])
    plt.grid(alpha=0.4)
    plt.xlim(-3,3)
    plt.ylim(-3,3)
    plt.show()

plot = interactive(plot, a=(-3,3,0.1), b=(-3,3,0.1))
output = plot.children[-1]
plot