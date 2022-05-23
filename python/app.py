# ------------------------------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------------------------------
import json
import time
import requests
import os
from dapr.clients import DaprClient

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
dapr_url = "http://localhost:{}/v1.0/invoke/phenny/method/tenant".format(dapr_port)


n = 0
while True:
    n += 1

    try:
        print("Sending message with invoke ...", flush=True)
        result = requests.get(dapr_url, headers={"Content-Type": "application/json"})
        print("test----------", result.status_code)
        print("test----------", result.content)
        print("test----------", result.text)
        print("result", result)

    except Exception as e:
        print(e)

    time.sleep(10)
