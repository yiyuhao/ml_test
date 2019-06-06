"""
@license : Copyright(C), WAYZ
@author: Xie Wangyi
@contact: wangyi.xie@wayz.ai
"""

from sklearn.metrics import pairwise_distances_argmin


def select_work_or_home(fence_list):
    work_or_home_cluster_center = [0.5885, 0.6132, 0.7361, 0.0817, 0.1575]
    other_cluster_center = [0.01, 0.0094, 0.0061, 0.0008, 0.003]

    work_fence_list = []
    home_fence_list = []

    for f, c in fence_list:  # fence, center

        if 0 == pairwise_distances_argmin([f], [work_or_home_cluster_center, other_cluster_center])[0]:
            # percentage of in home, percentage of on working
            le, lv, duration, p_home, p_working = f

            if p_working == 0:
                home_fence_list.append((f, c))
            elif p_home / p_working > 1:
                home_fence_list.append((f, c))
            elif p_working / p_home > 1:
                work_fence_list.append((f, c))

    work_fence = work_fence_list[
        pairwise_distances_argmin([work_or_home_cluster_center],
                                  list(map(lambda fe: fe[0], work_fence_list)))[0]] if len(
        work_fence_list) else (None, None)

    home_fence = home_fence_list[
        pairwise_distances_argmin([work_or_home_cluster_center],
                                  list(map(lambda fe: fe[0], home_fence_list)))[0]] if len(
        home_fence_list) else (None, None)

    return work_fence[1], home_fence[1]


def select_work_or_home_by_le_num(fence_list):
    home_fence = (None, None)
    work_fence = (None, None)

    def more_proper_fence(old_fence, new_fence):
        if old_fence == (None, None):
            return new_fence

        # compare le num
        return new_fence if new_fence[0][0] > old_fence[0][0] else old_fence

    for f, c in fence_list:  # fence, center

        # percentage of in home, percentage of on working
        le, lv, duration, p_home, p_working = f

        if p_working == 0:
            home_fence = more_proper_fence(home_fence, (f, c))
        elif p_home == 0:
            work_fence = more_proper_fence(work_fence, (f, c))

        elif p_home / p_working > 1:
            home_fence = more_proper_fence(home_fence, (f, c))
        elif p_working / p_home > 1:
            work_fence = more_proper_fence(work_fence, (f, c))

    work_fence_center, home_fence_center = work_fence[1], home_fence[1]

    return work_fence_center, home_fence_center
