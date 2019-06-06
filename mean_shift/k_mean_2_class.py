"""
@license : Copyright(C), WAYZ
@author: Yuhao Yi
@contact: yuhao.yi@wayz.ai
"""
import json

import numpy as np
import pandas
from sklearn.cluster import KMeans
from mean_shift.clustering import run_clustering

run_clustering()


def load_data():
    with open('users_clusters_data.json', encoding='utf-8') as f:
        return json.load(f)


# to ndarray

original_data = load_data()

original_clean_data = []
for user, user_clusters in enumerate(original_data):
    for cluster in user_clusters:
        original_clean_data.append([cluster, user])

prepare_data = []
for user_clusters in original_data:
    prepare_data.extend(user_clusters)

data = np.array(prepare_data)

k_means = KMeans(n_clusters=2)

predicted_result = k_means.fit_predict(data)  # [1 1 0 0 0 0 1 1 0 ... 0]

cluster_result = {}

for i, cluster in enumerate(predicted_result):
    if not cluster_result.get(cluster):
        cluster_result[cluster] = []

    cluster_result[cluster].append(original_clean_data[i])


writer = pandas.ExcelWriter('k_means_result.xlsx')

for cluster, data in cluster_result.items():
    json_data = json.dumps(data)

    data = pandas.read_json(json_data, encoding='utf-8')
    data.to_excel(writer, cluster, index=False)

writer.save()
