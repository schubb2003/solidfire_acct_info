#!/usr/local/bin/python
# Author: Scott Chubb scott.chubb@netapp.com
# Written for Python 3.4 and above
# No warranty is offered, use at your own risk.  While these scripts have been tested in lab situations, all use cases cannot be accounted for.
# Usage: python list_specific_account <ID or NAME> <Account name or ID> <src_mvip name or IP> <user> <password>
# <ID or NAME> determine sif the user is looking for account by ID or NAME
# <Account name or ID> this is the actual ID or name you are looking for

import sys
from solidfire.factory import ElementFactory
from solidfire.models import *

accountType = sys.argv[1].lower()
accountInfo = sys.argv[2]
src_mvip = sys.argv[3]
src_user = sys.argv[4]
src_pass = sys.argv[5]

def main():
    # Use ElementFactory to get a SolidFireElement object.
    sfe = ElementFactory.create(src_mvip, src_user, src_pass)
    list_accounts_result = sfe.list_accounts()

    # If the account type was submitted as an ID process it as an integer
    if accountType == "id":
        for account in list_accounts_result.accounts:
            if account.account_id == int(accountInfo):
                print(account.username)

    else:
        #By username
        for account in list_accounts_result.accounts:
            if account.username == accountInfo:
                print(account.account_id)

if __name__ == "__main__":
    main()