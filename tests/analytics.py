import numpy as np
import matplotlib.pyplot as plt

def wavy_line_plot(af, a, b):
    x1 = np.linspace(0.0, a)
    x2 = np.linspace(0.0, b)

    y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
    y2 = np.cos(2 * np.pi * x2)
    
    plt.subplot(2, 1, 1)
    plt.plot(x1, y1, 'o-')
    plt.title('A tale of 2 subplots')
    plt.ylabel('Damped oscillation')
    
    plt.subplot(2, 1, 2)
    plt.plot(x2, y2, '.-')
    plt.xlabel('time (s)')
    plt.ylabel('Undamped')

    plt.savefig("two_subplots.png")
    af.add_existing_file("two_subplots.png", remove=True)

    return (list(x1), list(y1))
