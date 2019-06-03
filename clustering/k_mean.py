"""
@license : Copyright(C), WAYZ
@author: Yuhao Yi
@contact: yuhao.yi@wayz.ai
"""
import json

import numpy as np
import pandas
from sklearn.cluster import KMeans


def load_data():
    # with open('fence_features.json', encoding='utf-8') as f:
    #     return json.load(f)
    return pandas.read_csv('trace_data_of_10000_people_with_136_lv.fences.csv').values


def normalize(array):
    min_, max_ = np.min(array, axis=0), np.max(array, axis=0)
    return (array - min_) / (max_ - min_)


# prepare
origin_data_list = load_data()

data_list = []
# clean
for row in origin_data_list:
    event, lv, duration, day_span, day_count, hour_0_6, hour_11_17 = row

    duration /= event
    hour_0_6 /= event
    hour_11_17 /= event
    data_list.append([event, lv, duration, day_span, day_count, hour_0_6, hour_11_17])

# to ndarray
data = np.array(data_list)

normalized_data = normalize(data)

k_means = KMeans(n_clusters=5)

predicted_result = k_means.fit_predict(normalized_data)  # [9 8 0 0 0 0 7 4 0 ... 0]

cluster_result = {}

for row, cluster in enumerate(predicted_result):
    cluster = str(cluster)
    if not cluster_result.get(cluster):
        cluster_result[cluster] = [['event', 'lv', 'duration', 'day_span', 'day_count', 'hour_0_to_6', 'hour_11_to_17']]

    cluster_result[cluster].append(data_list[row])

# json_result = json.dumps(cluster_result)

writer = pandas.ExcelWriter('k_means_result.xlsx')

for cluster, data in cluster_result.items():
    json_data = json.dumps(data)

    data = pandas.read_json(json_data, encoding='utf-8')
    data.to_excel(writer, cluster, index=False)

writer.save()
