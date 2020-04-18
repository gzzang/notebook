# @Time    : 2020/4/18 23:58
# @Author  : gzzang
# @File    : kmeans
# @Project : notebook

import numpy as np
from sklearn.cluster import KMeans

np.random.seed(0)

sample_data_number = 100
test_data_number = 10
sample_data = np.random.rand(sample_data_number, 2)
test_data = np.random.rand(sample_data_number, 2)

clusters_number = 3

kmeans = KMeans(n_clusters=clusters_number).fit(sample_data)
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_
inertia = kmeans.inertia_

test_label = kmeans.predict(test_data)

print(f'cluster_centers:{cluster_centers}')
print(f'labels:{labels}')
print(f'inertia:{inertia}')
print(f'test_label:{test_label}')


