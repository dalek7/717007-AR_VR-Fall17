# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import DDUtil

dat = np.loadtxt ("pose/out_20170919_010635_555719_pose.txt")
#dat = np.loadtxt ("pose/out_20170919_010615_996641_pose.txt")

print dat.shape

x = dat[:,12+1]
y = dat[:,13+1]
z = dat[:,14+1]

x2 = []
y2 = []
z2 = []

# 너무 촘촘해서 띄엄띄엄 그리기 위함
nJump = 10
x2 = DDUtil.GetSparseIDX(x, nJump)
y2 = DDUtil.GetSparseIDX(y, nJump)
z2 = DDUtil.GetSparseIDX(z, nJump)

x2 = np.array(x2)
y2 = np.array(y2)
z2 = np.array(z2)

print x2.shape


fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(x2, z2,-y2, c='r', marker='.')
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_zlabel('Y')
ax.set_aspect('equal')
plt.show()
