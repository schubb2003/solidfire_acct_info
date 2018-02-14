#!/usr/local/bin/python
# Change sf-mvip.demo.netapp.com to your MVIP name or IP
# Change admin to your user account
# Change Netapp1! to your password

import json
import base64
import requests
from solidfire.factory import ElementFactory


# Web/REST auth credentials build authentication
auth = ("admin:Netapp1!")
encodeKey = base64.b64encode(auth.encode('utf-8'))
basicAuth = bytes.decode(encodeKey)

headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic %s" % basicAuth,
    'Cache-Control': "no-cache",
    }

# Be certain of your API version path here
url = "https://" + mvip_ip + "/json-rpc/9.0"
# Various payload params in one liner
# payload = "{\n\t\"method\": \"ListAccounts\",\n    \"params\": {\n        \"startAccountID\": <Optional Account ID to start listing>,\n        \"limit\": <Optional Number of accounts to return>,\n        \"includeStorageContainers\": <Boolean true or false>\n    },\n    \"id\": 1\n}"

payload = "{" + \
                "\n  \"method\": \"ListAccounts\"," + \
                "\n    \"params\": {}" + \
                "\n    \"id\": 1" + \
            "\n}"


response = requests.request("POST", url, data=payload, headers=headers, verify=False)

raw = json.loads(response.text)

print(json.dumps(raw, indent=4, sort_keys=True))