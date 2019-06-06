"""
@license : Copyright(C), WAYZ
@author: Yuhao Yi
@contact: yuhao.yi@wayz.ai
"""
import json

import numpy as np

from bigdata.clustering.nodes import read_trace_data, trace_data_to_fence_list, fence_list_to_work_and_home
from bigdata.clustering.utils import get_file_path


def predict_home_working(trace_data):
    fence_list, cluster_centers, cluster_centers_weights = trace_data_to_fence_list(trace_data)
    result = np.hstack([cluster_centers, np.transpose(np.array([cluster_centers_weights]))])
    print('cluster data:' + json.dumps(result.tolist()))

    work_position, home_position = fence_list_to_work_and_home(fence_list)

    print('work:{}'.format(work_position.tolist() if work_position is not None else None))
    print('home:{}'.format(home_position.tolist() if home_position is not None else None))

    return work_position, home_position
