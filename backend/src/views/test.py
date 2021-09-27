import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template

from backend.src.pybithumb.RealTimeWebsocketProcess import RealTimeWebsocketProcess

application = Flask(__name__)
random.seed()  # Initialize the random number generator
websocket_process = RealTimeWebsocketProcess(["BTC"])
# while True:
#     print(websocket_process.get_data())

#
# @application.route("/")
# def index():
#     return render_template("index.html")
#
#
# def generate_random_data():
#     while True:
#         print(websocket_process.get_data())
#         json_data = json.dumps(
#             {
#                 "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 "value": websocket_process.get_data()
#             }
#         )
#         yield f"data:{json_data}\n\n"
#         time.sleep(1)
#
#
# @application.route("/chart-data")
# def chart_data():
#     return Response(generate_random_data(), mimetype="text/event-stream")
#
#
# if __name__ == "__main__":
#     application.run(host="0.0.0.0", debug=True, threaded=True)