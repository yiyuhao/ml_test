"""
@license : Copyright(C), WAYZ
@author: Yuhao Yi
@contact: yuhao.yi@wayz.ai
"""


class ClusteringFeatures:
    # 艾瑞 2015年上班人群时间分布 https://www.useit.com.cn/thread-10280-1-1.html
    # 8:00 - 17:00  35%
    # 8:30 - 17:30  36.7%
    # 9:00 - 18:00  20.9%
    # 9:30 - 18:30  2.3%
    # 10:00 - 19:00 1.5%
    # 弹性制         3.6%

    # 上班时间一小时以内 > 49.8%

    # 可以认为工作日的 10:00-17:00 >95%的人正在工作
    # 可以认为工作日的 0:00-7:00 22:00-24:00(路程1小时及加班情况) 有>95%的人在家

    HOUSE_TIME = 22, 7  # [21, 9) means 0-7 ∩ 22-24
    WORKING_TIME = 10, 17
