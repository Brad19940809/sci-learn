import numpy as np
import scipy.stats as stats
import scipy.optimize as opt
import matplotlib.pyplot as plt

# 均匀分布
rv_unif = stats.uniform.rvs(size=10)
print(rv_unif)
plt.subplot(211)
plt.plot(rv_unif)

# 贝塔分布
rv_beta = stats.beta.rvs(size=10, a=4, b=2)
print(rv_beta)
plt.subplot(212)
plt.plot(rv_beta)

plt.show()