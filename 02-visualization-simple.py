# 717007 한림대학교 AR/VR
# 20170926

import matplotlib.pyplot as plt


import numpy as np
from DDRotation import eulerAnglesToRotationMatrixD
from DDRotation import makeHomogeneous
from DDUtilDraw import draw_axis

H0 = [ 0.,      1.0,      0.,       0.,
       0.,      0.,       1.0,      0.,
       0.,      0, 0 ,    0.9981,   0.,
       -0.1808,  0.1399,  0.336,    1.]

H2 = [ 0.,      0.9989, -0.0181, -0.0433,  0.,      0.02,    0.9988,  0.0442,  0.,
  0.0425, -0.045,   0.9981,  0.,     -0.1808,  0.1399,  0.336,   1.    ]

t = [0,0,0] # [-0.1808,  0.1399,  0.336]

# 각 축을 기준으로 임의로 회전한 Matrix 생성
deg = 60
r3 = eulerAnglesToRotationMatrixD([deg, 0,0]) # 각 축별 회전각도 입력
H3 = makeHomogeneous(r3, t)

print(H2)
print(r3)

H0 = np.array(H0)
H2 = np.array(H2)

H0_rx = H0[1:4]
H0_ry = H0[5:8]
H0_rz = H0[9:12]

H2_rx = H2[1:4]
H2_ry = H2[5:8]
H2_rz = H2[9:12]

H3_rx = H3[0:3]
H3_ry = H3[4:7]
H3_rz = H3[8:11]

# Translation (3자유도 위치)
H0_x = t[0] # H0[12+1]
H0_y = t[1] # H0[13+1]
H0_z = t[2] # H0[14+1]


#print(H0_rx[1])
#print(H0_rx.ndim)

# 그림 그리기 시작
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.scatter(H0_x, H0_y, H0_z, c='r', marker='.')

draw_axis(ax, H0_x, H0_y, H0_z, H0_rx, H0_ry, H0_rz, scale= 0.02) # axis 그리기
#draw_axis(ax, H0_x, H0_y, H0_z, H2_rx, H2_ry, H2_rz, scale= 0.02) # axis 그리기
draw_axis(ax, H0_x, H0_y, H0_z, H3_rx, H3_ry, H3_rz, scale= 0.02) # axis 그리기

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#ax.set_aspect('equal')
str = 'Rotation about X-axis : ' + str(deg) + ' degrees'
plt.title(str)

plt.savefig('examples/3d_rotation_degrees_{}.svg'.format(deg))
plt.savefig('examples/3d_rotation_degrees_{}.png'.format(deg))

plt.show()