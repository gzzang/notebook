# @Time    : 2020/5/14 22:07
# @Author  : gzzang
# @File    : lognorm
# @Project : notebook

from scipy.stats import lognorm
import matplotlib.pyplot as plt
import numpy as np
import pdb

fig, ax = plt.subplots(1, 1)
s = 0.954
s = 0.5
mean, var, skew, kurt = lognorm.stats(s, moments='mvsk')
x = np.linspace(lognorm.ppf(0.01, s),
                lognorm.ppf(0.99, s), 100)
ax.plot(x, lognorm.pdf(x, s),
       'r-', lw=5, alpha=0.6, label='lognorm pdf')

rv = lognorm(s)
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
vals = lognorm.ppf([0.001, 0.5, 0.999], s)
print(np.allclose([0.001, 0.5, 0.999], lognorm.cdf(vals, s)))

print(np.allclose(a=[1.1000000000001,1.2],b=[1.1,1.2]))

# pdb.set_trace()

r = lognorm.rvs(s, size=1000)

sigma = s
mu = 0


r = lognorm.rvs(s=sigma, loc=0, scale=np.exp(mu), size=1000)
rr = np.log(r)
print(rr)

print(r.mean())
print(r.var())
print(rr.mean())
print(rr.var())

ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
# plt.show()



from sklearn.cluster import KMeans

# np.random.seed(0)
#
# sample_data_number = 100
# test_data_number = 10
# sample_data = np.random.rand(sample_data_number, 2)
# test_data = np.random.rand(sample_data_number, 2)

clusters_number = 6

print(r.shape)
print(r.reshape([-1,1]).shape)

kmeans = KMeans(n_clusters=clusters_number).fit(r.reshape([-1,1]))
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_
inertia = kmeans.inertia_

print(f'cluster_centers:{cluster_centers}')
b= np.bincount(labels)
print(b)
# print(f'labels:{labels}')
# print(f'inertia:{inertia}')

a = np.argsort(cluster_centers.flatten())
c= b[a]
print(c)
plt.figure()
plt.bar(x = np.arange(clusters_number), height=c)

plt.figure()
plt.plot(cluster_centers[a],c,'-o')
plt.show()