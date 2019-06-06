"""
@license : Copyright(C), WAYZ
@author: Xie Wangyi
@contact: wangyi.xie@wayz.ai
"""
import json

import numpy as np

from bigdata.clustering.nodes import read_trace_data, trace_data_to_fence_list, fence_list_to_work_and_home
from bigdata.clustering.utils import get_file_path


def main():
    count = 0
    trace_data_gen = read_trace_data(get_file_path('trace_data_of_real_samples.json'))

    for trace_data in trace_data_gen:
        print(f'{count}:trace:{json.dumps(trace_data)}')

        fence_list, cluster_centers, cluster_centers_weights = trace_data_to_fence_list(trace_data)
        result = np.hstack([cluster_centers, np.transpose(np.array([cluster_centers_weights]))])
        print('cluster data:' + json.dumps(result.tolist()))

        work_fence, home_fence = fence_list_to_work_and_home(fence_list)

        print(f'{count}:work:{work_fence.tolist() if work_fence is not None else None}')
        print(f'{count}:home:{home_fence.tolist() if home_fence  is not None else None}')
        count += 1
        print(f'Progress {count}\n')

        if count == 50:
            break


if __name__ == '__main__':
    main()
