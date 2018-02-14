#!/usr/local/bin/python
# Usage: python list_specific_account <ID or NAME> <Account name or ID> <mvip name or IP> <user> <password>
# <ID or NAME> determine sif the user is looking for account by ID or NAME
# <Account name or ID> this is the actual ID or name you are looking for
import requests
import base64
import json
import sys
from solidfire.factory import ElementFactory
from solidfire.models import *

if len(sys.argv) < 6:
    print("Insufficient arguments submitted, usage is:"
          "\n python <script_name> <cluster> <username> <password> <type - id | name> <account_name | account_id>"
          "<user_name> <password>")

mvip_ip = sys.argv[1]
user_name = sys.argv[2]
user_pass = sys.argv[3]
acct_type = sys.argv[4].lower()
account = sys.argv[5]
accountInfo = str(account)

# Web/REST auth credentials build authentication
auth = (user_name + ":" + user_pass)
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
# payload = "{\n\t\"method\": \"GetAccountByID\",\n    \"params\": {\n        \"accountID\": <Account ID>\n    },\n    \"id\": 1\n}"
# payload = "{\n\t\"method\": \"GetAccountByName\",\n    \"params\": {\n        \"username\": \"<Account Name>\"\n    },\n    \"id\": 1\n}"

# payload in JSON multi-line
if acct_type == "id":
    payload = "{" + \
                    "\n  \"method\": \"GetAccountByID\"," + \
                    "\n    \"params\": {" + \
                    "\n    \t\"accountID\": " + str(accountInfo) + \
                    "\n    }," + \
                    "\n    \"id\": 1" + \
                "\n}"
else:
    payload = "{" + \
                    "\n  \"method\": \"GetAccountByName\"," + \
                    "\n    \"params\": {" + \
                    "\n    \t\"username\": \"" + str(accountInfo) + "\"" + \
                    "\n    }," + \
                    "\n    \"id\": 1" + \
                "\n}"    

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

raw = json.loads(response.text)

print(json.dumps(raw, indent=4, sort_keys=True))