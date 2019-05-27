"""
@license : Copyright(C), WAYZ
@author: Yuhao Yi
@contact: yuhao.yi@wayz.ai
"""

from numpy import *
import operator
import matplotlib
from matplotlib import pyplot


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
        class_label_vector.append(int(list_from_line[-1]))

    return return_mat, class_label_vector


def auto_normalize(data_set):
    min_values = data_set.min(0)
    max_values = data_set.max(0)

    ranges = max_values - min_values

    normalize_data_set = zeros(shape(data_set))
    m = data_set.shape[0]
    normalize_data_set = data_set - tile(min_values, (m, 1))
    normalize_data_set = normalize_data_set / tile(ranges, (m, 1))
    return normalize_data_set, ranges, min_values


def test_dating_class():
    ho_ratio = 0.10
    dating_data_mat, dating_labels = file2matrix('datingTestSet2.txt')
    norm_mat, ranges, min_values = auto_normalize(dating_data_mat)
    m = norm_mat.shape[0]
    num_test_vecs = int(m * ho_ratio)

    error_count = 0
    for i in range(num_test_vecs):
        classifier_result = classify0(norm_mat[i, :], norm_mat[num_test_vecs:m, :],
                                      dating_labels[num_test_vecs:m], 3)
        print(f'the classifier came back with: {classifier_result}, '
              f'the real answer is: {dating_labels[i]}')

        if classifier_result != dating_labels[i]:
            error_count += 1

    print(f'the total error rate is {error_count / float(num_test_vecs) * 100}%')


def show():
    dating_data_mat, dating_labels = file2matrix('datingTestSet2.txt')

    fig = pyplot.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dating_data_mat[:, 1], dating_data_mat[:, 2],
               15.0 * array(dating_labels), 15.0 * array(dating_labels))
    pyplot.show()


def img2vector(filename):
    return_vector = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        line_str = fr.readline()
        for j in range(32):
            return_vector[0, 32 * i + j] = int(line_str[j])

    return return_vector


if __name__ == '__main__':
    test_dating_class()
