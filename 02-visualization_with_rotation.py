# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import DDUtil
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from matplotlib import collections  as mc

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

dat = np.loadtxt ("pose/out_20170919_010635_555719_pose.txt")
#dat = np.loadtxt ("pose/out_20170919_010615_996641_pose.txt")

print('dat.shape (before) =', dat.shape)

# 너무 촘촘해서 띄엄띄엄 그리기 위함
nJump = 10
dat = DDUtil.GetSparseIDX(dat, nJump)

dat = np.array(dat)
print('dat.shape (after) =', dat.shape)

rx = dat[:, 1:4]
ry = dat[:, 5:8]
rz = dat[:, 9:12]
#print(rx[0], ry[0], rz[0])
#print(dat[0])

x = dat[:,12+1]
y = dat[:,13+1]
z = dat[:,14+1]

print('rx.shape =', rx.shape)
print('x.shape =', x.shape)

# 그림 그리기 시작
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(x, y, z, c='r', marker='.')

ax.scatter(x[0], y[0], z[0], c='r', marker='*',  s=100)
# Column vectors
g = 0.02
lines = []
for i in range(x.shape[0]):
    ax.plot([x[i], x[i] + g * rx[i, 0]], [y[i], y[i] + g * rx[i, 1]], [z[i], z[i] + g * rx[i, 2]], 'r')
    ax.plot([x[i], x[i] + g * ry[i, 0]], [y[i], y[i] + g * ry[i, 1]], [z[i], z[i] + g * ry[i, 2]], 'g')
    ax.plot([x[i], x[i] + g * rz[i, 0]], [y[i], y[i] + g * rz[i, 1]], [z[i], z[i] + g * rz[i, 2]], 'b')



ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_aspect('equal')



plt.show()