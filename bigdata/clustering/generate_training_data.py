"""
@license : Copyright(C), WAYZ
@author: Xie Wangyi
@contact: wangyi.xie@wayz.ai
"""

import numpy as np

from bigdata.clustering.nodes import read_trace_data, trace_data_to_fence_list
from bigdata.clustering.utils import get_file_path


def main():
    count = 0
    all_fences = []
    trace_data_gen = read_trace_data(get_file_path('trace_data_of_10000_people_with_136_lv.json'))

    for trace_data in trace_data_gen:
        fence_list = trace_data_to_fence_list(trace_data)
        all_fences += fence_list  # TODO get features
        count += 1
        print(f'Progress {count}')

    all_fences = np.array(all_fences)

    np.savetxt('/Users/xiewangyi/projects/bigdata/'
               'casestudydata/trace_data_of_10000_people_with_136_lv.fences.csv',
               all_fences, delimiter=',',
               fmt='%.09f',
               header='le,lv,du,lv0_6,lv11_17')


if __name__ == '__main__':
    main()
