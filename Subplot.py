import matplotlib.pyplot as plt
import numpy as np


def draw_subplot():
    fig, ax = plt.subplots(3, 3)
    for i in range(3):
        for j in range(3):
            ax[i, j].plot(np.random.randn(4, 4))
    plt.tight_layout()
    plt.show()


draw_subplot()