"""
@license : Copyright(C), WAYZ
@author: Xie Wangyi
@contact: wangyi.xie@wayz.ai
"""
from datetime import datetime

from bigdata.clustering.utils import bet_in_home, bet_on_working


def extract_features(raw_data, cluster_center, location_event_list):
    # this user
    total_le_count = len(raw_data)
    total_lv = sum((x[3] for x in raw_data))
    total_duration = sum((x[4] for x in raw_data))

    # this cluster
    location_event_count = len(location_event_list)
    location_view_sum = 0
    location_duration_sum = 0
    date_set = set()
    location_bet_in_house = 0
    location_bet_in_working = 0

    for le in location_event_list:
        timestamp, lv_sum, duration = le[0] / 1000, le[3], le[4]
        lv_bj_datetime = datetime.fromtimestamp(timestamp)
        location_view_sum += lv_sum
        location_duration_sum += duration
        date_set.add(lv_bj_datetime.date())
        if bet_in_home(lv_bj_datetime):
            location_bet_in_house += lv_sum
        elif bet_on_working(lv_bj_datetime):
            location_bet_in_working += lv_sum

    day_span = (max(date_set) - min(date_set)).days
    day_count = len(date_set)

    features = (location_event_count, location_view_sum, location_duration_sum, day_span, day_count,
                location_bet_in_house, location_bet_in_working)

    return (features[0] * 1.0 / total_le_count,
            features[1] * 1.0 / total_lv,
            features[2] * 1.0 / total_duration if total_duration else 0,
            features[5] * 1.0 / location_view_sum,
            features[6] * 1.0 / location_view_sum)
