# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import DDUtil
import DDUtilDraw
#dat = np.loadtxt ("pose/out_20170919_010635_555719_pose.txt")
#dat = np.loadtxt ("pose/out_20170919_010615_996641_pose.txt")

# 다음은 2017/9/21 수업시간에 측정한 Google Tango 장치의 pose 입니다. 본인의 숫자를 열어 보세요
dat = np.loadtxt ("pose/TangoPose/out_20000101_185919_855635_pose.txt") # pose 01 - 신예림
#dat = np.loadtxt ("pose/TangoPose/out_20000101_185953_781812_pose.txt") # pose 02 - 김동훈
#dat = np.loadtxt ("pose/TangoPose/out_20000101_190023_307195_pose.txt") # pose 03 - 배정준

#dat = np.loadtxt ("pose/TangoPose/out_20000101_190044_616806_pose.txt") # pose 04 - 김도윤
#dat = np.loadtxt ("pose/TangoPose/out_20000101_190112_537176_pose.txt") # pose 05 - 남홍근
#dat = np.loadtxt ("pose/TangoPose/out_20000101_190153_197452_pose.txt") # pose 06 - 정예찬
#dat = np.loadtxt ("pose/TangoPose/out_20000101_190234_838543_pose.txt") # pose 07 - 한가희
#dat = np.loadtxt ("pose/TangoPose/out_20000101_190301_437286_pose.txt") # pose 08 - 이주현
#dat = np.loadtxt ("pose/TangoPose/out_20000101_190350_166419_pose.txt") # pose 09 - 김현주
#dat = np.loadtxt ("pose/out_20170919_010635_555719_pose.txt") - 김미래
#dat = np.loadtxt ("pose/out_20170919_010615_996641_pose.txt") - 임지수


print('dat.shape (before) =', dat.shape)

# 너무 촘촘해서 띄엄띄엄 그리기 위함
nJump = 10 # 필요에 따라 늘려서 해보세요
dat = DDUtil.GetSparseIDX(dat, nJump)

dat = np.array(dat)
print('dat.shape (after) =', dat.shape)

# 매 순간 회전, x/y/z 축 Column vectors
rx = dat[:, 1:4]
ry = dat[:, 5:8]
rz = dat[:, 9:12]
#print(rx[0], ry[0], rz[0])
print(dat[0])

# Translation (3자유도 위치)
x = dat[:,12+1]
y = dat[:,13+1]
z = dat[:,14+1]

print('rx.shape =', rx.shape)
print('x.shape =', x.shape)

# 그림 그리기 시작
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(x, y, z, c='r', marker='.')

#시작점을 별(*)로 표시
ax.scatter(x[0], y[0], z[0], c='r', marker='*',  s=100)

DDUtilDraw.DrawAxis(ax, x, y, z, rx, ry, rz, scale= 0.02) # axis 그리기

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_aspect('equal')

plt.show()




