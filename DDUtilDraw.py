# Seung-Chan Kim

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

def DrawAxis(ax, posx, posy, posz, rx, ry, rz, scale=1):
    nd = rx.ndim
    if nd==2:
        for i in range(posx.shape[0]):
            ax.plot([posx[i], posx[i] + scale * rx[i, 0]], [posy[i], posy[i] + scale * rx[i, 1]], [posz[i], posz[i] + scale * rx[i, 2]], 'r')
            ax.plot([posx[i], posx[i] + scale * ry[i, 0]], [posy[i], posy[i] + scale * ry[i, 1]], [posz[i], posz[i] + scale * ry[i, 2]], 'g')
            ax.plot([posx[i], posx[i] + scale * rz[i, 0]], [posy[i], posy[i] + scale * rz[i, 1]], [posz[i], posz[i] + scale * rz[i, 2]], 'b')

    elif nd==1:
        ax.plot([posx, posx + scale * rx[0]], [posy, posy + scale * rx[1]], [posz, posz + scale * rx[2]], 'r')
        ax.plot([posx, posx + scale * ry[0]], [posy, posy + scale * ry[1]], [posz, posz + scale * ry[2]], 'g')
        ax.plot([posx, posx + scale * rz[0]], [posy, posy + scale * rz[1]], [posz, posz + scale * rz[2]], 'b')


