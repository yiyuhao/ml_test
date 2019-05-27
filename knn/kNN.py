"""
@license : Copyright(C), WAYZ
@author: Yuhao Yi
@contact: yuhao.yi@wayz.ai
"""

from numpy import *
import operator


def create_data_set():
    group = array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0, 0],
        [0, 0.1],
    ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]

    # distance calculation
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5

    sorted_dist_indicies = distances.argsort()

    class_count = {}

    # voting with lowest k distances
    for i in range(k):
        vote_i_label = labels[sorted_dist_indicies[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1

    # sort
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_class_count[0][0]


def file2matrix(filename):
    fr = open(filename)
    number_of_lines = len(fr.readlines())
    return_mat = zeros((number_of_lines, 3))

    class_label_vector = []

    fr = open(filename)

    # parse line to a list
    for i, line in enumerate(fr.readlines()):
        line = line.strip()
        list_from_line = line.split('\t')
        return_mat[i, :] = list_from_line[0:3]
        class_label_vector.append(list_from_line[-1])

    return return_mat, class_label_vector


if __name__ == '__main__':
    dating_data_mat, dating_labels = file2matrix('datingTestSet.txt')