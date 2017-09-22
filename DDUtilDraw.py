# Seung-Chan Kim

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np


def DrawAxis(ax, posx, posy, posz, rx, ry, rz, scale=1):
    for i in range(posx.shape[0]):
        ax.plot([posx[i], posx[i] + scale * rx[i, 0]], [posy[i], posy[i] + scale * rx[i, 1]], [posz[i], posz[i] + scale * rx[i, 2]], 'r')
        ax.plot([posx[i], posx[i] + scale * ry[i, 0]], [posy[i], posy[i] + scale * ry[i, 1]], [posz[i], posz[i] + scale * ry[i, 2]], 'g')
        ax.plot([posx[i], posx[i] + scale * rz[i, 0]], [posy[i], posy[i] + scale * rz[i, 1]], [posz[i], posz[i] + scale * rz[i, 2]], 'b')
