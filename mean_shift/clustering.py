"""
@license : Copyright(C), WAYZ
@author: Yuhao Yi
@contact: yuhao.yi@wayz.ai
"""
import json
from datetime import datetime

import numpy as np
from sklearn.cluster import MeanShift


# Generate sample data
def load_data():
    with open('prepare_data.json', encoding='utf-8') as f:
        init_data = json.load(f)

    data = []

    for user_lvs in init_data:
        user_data = []
        for lv in user_lvs:
            timestamp, longitude, latitude, _, _ = lv

            dt = datetime.fromtimestamp(int(timestamp) / 100)

            # exclude [10,22) lv
            if 10 <= dt.hour < 22:
                continue

            # in CD
            # if not (104.3 < longitude < 105) or not (30.6 < latitude < 40):
            #     continue

            user_data.append([longitude, latitude])
        data.append(user_data)
    return data


def clustering(data):
    users_clusters = []

    for user, prepare_data in enumerate(data):

        prepare_data = np.array(prepare_data)

        if len(prepare_data) == 0:
            continue

        # The following bandwidth can be automatically detected using

        ms = MeanShift(bandwidth=0.001, bin_seeding=True, cluster_all=False)

        ms.fit(prepare_data)

        labels = ms.labels_
        # cluster_centers = ms.cluster_centers_

        labels_unique = np.unique(labels)
        n_clusters_ = len(labels_unique)
        print("number of estimated clusters : %d" % n_clusters_)

        user_clusters = [[0] for _ in range(labels_unique[-1] + 1)]  # [[0], [0], [0], ...]

        for label in labels:
            if label == -1:
                continue

            user_clusters[label][0] += 1

        users_clusters.append(user_clusters)

    return json.dumps(users_clusters)


def run_clustering():
    """generate a file users_clusters_data.json"""
    data = load_data()
    users_clusters = clustering(data)

    with open('users_clusters_data.json', 'w+') as f:
        f.write(users_clusters)


if __name__ == '__main__':
    run_clustering()