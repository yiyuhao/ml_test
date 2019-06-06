"""
@license : Copyright(C), WAYZ
@author: Xie Wangyi
@contact: wangyi.xie@wayz.ai
"""
from flask import Flask
from flask import request

from clustering.algo.mean_shift_runner import MeanShiftRunner

app = Flask(__name__)


@app.route('/api/mean-shift', methods=['POST'])
def api_mean_shift():
    body = request.json
    labels, cluster_centers, cluster_centers_weights = MeanShiftRunner().run_mean_shift(body)
    return dict(
        labels=labels,
        cluster_centers=cluster_centers,
        cluster_centers_weights=cluster_centers_weights
    )


app.run(host="0.0.0.0")
