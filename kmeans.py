import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# 生成示例数据（二维数据，3个簇）
X, y_true = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# 初始化参数
k = 3  # 簇的数量
max_iters = 100  # 最大迭代次数

# 随机初始化簇中心
centroids = X[np.random.choice(X.shape[0], k, replace=False)]

# 计算两个点之间的欧几里得距离
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# K-means 算法核心逻辑
for iteration in range(max_iters):
    # 分配每个点到最近的簇中心
    labels = np.array([np.argmin([euclidean_distance(x, centroid) for centroid in centroids]) for x in X])

    # 计算新的簇中心
    new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

    # 如果簇中心不再变化，则结束迭代
    if np.all(centroids == new_centroids):
        break

    centroids = new_centroids

# 绘制结果
plt.scatter(X[:, 0], X[:, 1], c=labels, s=30, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='X')  # 标记簇中心
plt.title("K-means Clustering")
plt.show()