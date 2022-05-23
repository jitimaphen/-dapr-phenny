import time
import requests
import os
from dapr.clients import DaprClient

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
dapr_url = "http://localhost:{}/v1.0/invoke/phenny/method/tenant/".format(dapr_port)


n = 0
while True:
    n += 1

    try:
        print("Sending message with invoke ...", flush=True)
        # case 1 with requests
        # result = requests.get(dapr_url, headers={"Content-Type": "application/json"}, data=b'')

        # case 2 with daprClient
        with DaprClient() as daprClient:
            # Using Dapr SDK to invoke a method
            result = daprClient.invoke_method(
                "phenny",
                "tenant/",
                data=b'',
                http_verb="GET"
            )
            print("result", result.data)

    except Exception as e:
        print(e)

    time.sleep(10)
