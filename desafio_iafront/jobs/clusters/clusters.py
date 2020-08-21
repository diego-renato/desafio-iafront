import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn.mixture import GaussianMixture
from sklearn.mixture import BayesianGaussianMixture
from sklearn.cluster import SpectralClustering
from sklearn.cluster import Birch


def kmeans(vector: np.array, n: int):
    k = KMeans(n_clusters=n, random_state=0)
    cluster_coordinate = k.fit_transform(vector)
    cluster_label = k.fit(vector)

    return cluster_coordinate, cluster_label.labels_

def mini_batch_kmeans(vector: np.array, n: int):
    mbk = MiniBatchKMeans(n_clusters=n, random_state=0)
    cluster_coordinate = mbk.fit_transform(vector)
    cluster_label = mbk.fit(vector)

    return cluster_coordinate, cluster_label.labels_

def gaussian_mixture(vector: np.array, n: int, BIC_calculate = False):
    if BIC_calculate == True:
        np.random.seed(140597)
        mask = np.random.choice([False, True], len(vector), p=[0.70, 0.30])
        model_train = GaussianMixture(n_components=n, covariance_type='full', max_iter=1000, tol=1e-5).fit(vector[~mask])
        BIC = model_train.bic(vector[mask])
        BIC_train = model_train.bic(vector[~mask])
        return BIC, BIC_train
    else:
        gmm = GaussianMixture(n_components=n, covariance_type='full', max_iter=500, tol=1e-4).fit(vector)
        cluster_label = gmm.predict(vector)
        return cluster_label

def bayesian_gaussian_mixture(vector: np.array, n: int, BIC_calculate = False):
    if BIC_calculate == True:
        np.random.seed(140597)
        mask = np.random.choice([False, True], len(vector), p=[0.70, 0.30])
        model_train = BayesianGaussianMixture(n_components=n, covariance_type='full').fit(vector[~mask])
        validation_score = model_train.score(vector[mask])
        train_score = model_train.score(vector[~mask])
        return validation_score, train_score
    else:
        np.random.seed(140597)
        mask = np.random.choice([False, True], len(vector), p=[0.70, 0.30])
        dpgmm = BayesianGaussianMixture(n_components=n, covariance_type='full', max_iter=900, tol=1e-4).fit(vector[~mask])
        cluster_label = dpgmm.predict(vector)
        return cluster_label

def spectral_clustering(vector: np.array, n: int):
    spc = SpectralClustering(n_clusters=n)
    cluster_label = spc.fit(vector)

    return cluster_label.labels_

def birch(vector: np.array, n: int):
    birch = Birch(n_clusters=n)
    cluster_label = birch.fit_predict(vector)

    return cluster_label.labels_