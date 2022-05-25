import time
import requests
import os
from flask_cors import CORS
from flask import Flask, redirect, url_for, request, render_template
from dapr.clients import DaprClient

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
dapr_url = "http://localhost:{}/v1.0/invoke/phenny/method/tenant/".format(dapr_port)

pub_sub_url = "http://localhost:{}/v1.0/publish/pubsub/deathStarStatus".format(dapr_port)

app = Flask(__name__)
CORS(app)


@app.route('/bird', methods=['POST'])
def bird():
    # data = request.get_json()
    print("------bird function")
    print("Bird: Sending message to pubsub ...", flush=True)
    requests.post(pub_sub_url, json={"status": "completed"})
    print("Bird: end pubsub ...", flush=True)



# n = 0
# while True:
#     n += 1
#     message_pub_sub = {"status": "completed"}
#
#     try:
#         print("Sending message with invoke ...", flush=True)
#         # # case 1 with requests
#         # # result = requests.get(dapr_url, headers={"Content-Type": "application/json"}, data=b'')
#         #
#         # # case 2 with daprClient
#         # with DaprClient() as daprClient:
#         #     # Using Dapr SDK to invoke a method
#         #     result = daprClient.invoke_method(
#         #         "phenny",
#         #         "tenant/",
#         #         data=b'',
#         #         http_verb="GET"
#         #     )
#         #     print("result", result.data)
#
#         # ---------------------------------------------
#         # print("Sending message to pubsub ...", flush=True)
#         # requests.post(pub_sub_url, json=message_pub_sub)
#
#     except Exception as e:
#         print(e)
#
#     time.sleep(10)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=6000)