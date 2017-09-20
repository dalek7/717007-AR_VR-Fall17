# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import DDUtil

dat = np.loadtxt ("pose/out_20170919_010635_555719_pose.txt")
#dat = np.loadtxt ("pose/out_20170919_010615_996641_pose.txt")

print('dat.shape (before) =', dat.shape)

# 너무 촘촘해서 띄엄띄엄 그리기 위함
nJump = 10
dat = DDUtil.GetSparseIDX(dat, nJump)

dat = np.array(dat)
print('dat.shape (after) =', dat.shape)

x = dat[:,12+1]
y = dat[:,13+1]
z = dat[:,14+1]
print('x.shape =', x.shape)

# 그림 그리기 시작
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(x, z,-y, c='r', marker='.')
ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.set_zlabel('Y')
ax.set_aspect('equal')
plt.show()