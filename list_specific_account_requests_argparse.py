#!/usr/local/bin/python
# Author: Scott Chubb scott.chubb@netapp.com
# Written for Python 3.4 and above
# No warranty is offered, use at your own risk.  While these scripts have been tested in lab situations, all use cases cannot be accounted for.
# This script takes input arguments and looks up accounts by ID or IDs by accounts
import requests
import base64
import json
import sys
import argparse
from solidfire.factory import ElementFactory

# Set vars for connectivity using argparse
parser = argparse.ArgumentParser()
parser.add_argument('-sm', type=str,
                    required=True,
                    metavar='mvip',
                    help='MVIP/node name or IP')
parser.add_argument('-su', type=str,
                    required=True,
                    metavar='username',
                    help='username to connect with')
parser.add_argument('-sp', type=str,
                    required=True,
                    metavar='password',
                    help='password for user')
parser.add_argument('-t', type=str,
                    required=True,
                    metavar='type',
                    choices=['id', 'name'],
                    help='Enter id to lookup by ID or name to lookup by name')
parser.add_argument('-a', type=str,
                    required=True,
                    metavar='account',
                    help="Enter the account name or ID")
args = parser.parse_args()

mvip_ip = args.m
user_name = args.u
user_pass = args.p
acct_type = args.t
account = args.a
accountInfo = str(account)

def main():
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

if __name__ == "__main__"
    main()
