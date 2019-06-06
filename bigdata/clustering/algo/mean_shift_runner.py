import math

import numpy as np

from bigdata.clustering.algo.mean_shift_algo import MeanShift

EARTH_R = 6371393
MAX_DEG = 150.0 / (2 * math.pi * EARTH_R) * 360


class MeanShiftRunner(object):
    def run_mean_shift(self, data):
        data = np.array(data)
        X = data[:, 1:3]  # location ndarray
        W = data[:, 3]  # lv
        # bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
        bandwidth = MAX_DEG
        ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        ms.fit(X, weights=W)
        labels = ms.labels_
        cluster_centers = ms.cluster_centers_
        cluster_centers_weights = ms.cluster_centers_weights_
        return labels, cluster_centers, cluster_centers_weights
