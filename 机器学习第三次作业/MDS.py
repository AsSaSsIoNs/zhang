import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


def cal_pairwise_dist(x):
    sum_x = np.sum(np.square(x), 1)
    dist = np.add(np.add(-2 * np.dot(x, x.T), sum_x).T, sum_x)
    return dist


def mds(data, n_dims):
    n, d = data.shape
    dist = cal_pairwise_dist(data)
    T1 = np.ones((n,n))*np.sum(dist)/n**2
    T2 = np.sum(dist, axis = 1, keepdims=True)/n
    T3 = np.sum(dist, axis = 0, keepdims=True)/n
    B = -(T1 - T2 - T3 + dist)/2
    eig_val, eig_vector = np.linalg.eig(B)
    index_ = np.argsort(-eig_val)[:n_dims]
    picked_eig_val = eig_val[index_].real
    picked_eig_vector = eig_vector[:, index_]
    return picked_eig_vector*picked_eig_val**(0.5)


if __name__ == '__main__':
    iris = load_iris()
    data = iris.data
    Y = iris.target
    data_1 = mds(data, 2)
    plt.figure()
    plt.scatter(data_1[:, 0], data_1[:, 1], c=Y)
    plt.savefig('MDS_Result')
    plt.show()