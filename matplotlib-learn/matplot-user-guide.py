from matplotlib import pyplot as plt

# plt.plot([1,2,3,4])
# plt.xlabel('distance')
# plt.ylabel('height')

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])


# plt.plot([1,2,3,4], [1,4,9,16], 'go')
# # axis() 命令接收 [xmin，xmax，ymin，ymax]
# plt.axis([0, 6, 0, 20])

import numpy as np
# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
# print(t)
# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

# # 设置线的宽度
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'g', linewidth=10)


x1=[1, 2, 3, 4];y1=[1, 4, 9, 16];x2=[5,6,7,8];y2=[10,20,30,40]

# lines = plt.plot(x1, y1, x2, y2)
# # 使用关键字参数
# setp=plt.setp(lines, c='r', linewidth=2.0, ls='--')
# print(setp)
# # 或者 MATLAB 风格的字符串值对
# plt.setp(lines, 'color', 'b', 'linewidth', 2.0)

print('处理多个图形和轴域')
# 处理多个图形和轴域
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
plt.figure(1)
plt.subplot(221)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
plt.subplot(222)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.subplot(2,2,3)
plt.plot(x1, y1)

plt.show()
