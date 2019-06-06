"""
@license : Copyright(C), WAYZ
@author: Xie Wangyi
@contact: wangyi.xie@wayz.ai
"""
import json

import numpy as np

from bigdata.clustering.algo.fence_feature_extractor import extract_features
from bigdata.clustering.algo.mean_shift_runner import MeanShiftRunner
from bigdata.clustering.algo.work_and_home_predictor import select_work_or_home, select_work_or_home_by_le_num


def read_trace_data(filename):
    with open(filename, 'rt') as f:
        while True:
            json_str = f.readline()
            if not json_str:
                break
            yield json.loads(json_str)


def trace_data_to_fence_list(trace_data):
    data = np.array(trace_data)
    labels, cluster_centers, cluster_centers_weights \
        = MeanShiftRunner().run_mean_shift(trace_data)
    n_clusters_ = len(cluster_centers)

    fence_list = []
    for k in range(n_clusters_):
        wheres_my_members = labels == k
        cluster_center = cluster_centers[k]
        my_menbers = data[wheres_my_members, :]
        if len(my_menbers) == 0:
            continue
        features = extract_features(trace_data, cluster_center, my_menbers)

        fence_list.append((features, cluster_center))

    return fence_list, cluster_centers, cluster_centers_weights


def fence_list_to_work_and_home(fence_list):
    work_fence, home_fence = select_work_or_home_by_le_num(fence_list)
    return work_fence, home_fence
