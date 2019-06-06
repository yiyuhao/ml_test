"""
@license : Copyright(C), WAYZ
@author: Yuhao Yi
@contact: yuhao.yi@wayz.ai
"""
from datetime import datetime
from os import path

from chinese_calendar import is_workday

from bigdata.clustering.config import ClusteringFeatures


def bet_in_home(datetime_: datetime):
    """guess in house"""
    hour = datetime_.hour
    begin, end = ClusteringFeatures.HOUSE_TIME

    # 法定 非工作日
    if not is_workday(datetime_):
        return True

    # 或工作日指定时间段
    if begin > end:
        return 0 <= hour < end or begin <= hour < 24
    else:
        return begin <= hour < end


def bet_on_working(datetime_: datetime):
    hour = datetime_.hour
    begin, end = ClusteringFeatures.WORKING_TIME

    # 法定 非工作日
    if not is_workday(datetime_):
        return False

    # 或工作日指定时间段
    if begin > end:
        return 0 <= hour < end or begin <= hour < 24
    else:
        return begin <= hour < end


def get_file_path(filename: str):
    data_directory = path.abspath('./bigdata/casestudydata')
    return path.join(data_directory, filename)
