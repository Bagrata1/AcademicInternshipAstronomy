"""
Tools for density estimation


"""
import numpy as np
from scipy import special
from sklearn.neighbors import BallTree


def n_volume(r, n):
    """compute the n-volume of a sphere of radius r in n dimensions"""
    return np.pi ** (0.5 * n) / special.gamma(0.5 * n + 1) * (r ** n)


class KNeighborsDensity(object):
    def __init__(self, method='bayesian', n_neighbors=10):
        if method not in ['simple', 'bayesian']:
            raise ValueError("method = %s not recognized" % method)

        self.n_neighbors = n_neighbors
        self.method = method

    def fit(self, X):      
        self.X_ = np.atleast_2d(X)
        if self.X_.ndim != 2:
            raise ValueError('X must be two-dimensional')

        self.bt_ = BallTree(self.X_)

        return self

    def eval(self, X):
       
        X = np.atleast_2d(X)
        if X.ndim != 2:
            raise ValueError('X must be two-dimensional')

        if X.shape[1] != self.X_.shape[1]:
            raise ValueError('dimensions of X do not match training dimension')

        dist, ind = self.bt_.query(X, self.n_neighbors, return_distance=True)
        k = float(self.n_neighbors)
        ndim = X.shape[1]

        if self.method == 'simple':
            return k / n_volume(dist[:, -1], ndim)

        elif self.method == 'bayesian':
            # XXX this may be wrong in more than 1 dimension!
            return (k * (k + 1) * 0.5 / n_volume(1, ndim)
                    / (dist ** ndim).sum(1))
        else:
            raise ValueError("Unrecognized method '%s'" % self.method)

        return dens