#!/usr/local/bin/python
# Usage: python list_specific_account <ID or NAME> <Account name or ID> <mvip name or IP> <user> <password>
# <ID or NAME> determine sif the user is looking for account by ID or NAME
# <Account name or ID> this is the actual ID or name you are looking for

import sys
from solidfire.factory import ElementFactory
from solidfire.models import *

accountType = sys.argv[1].lower()
accountInfo = sys.argv[2]
MVIP = sys.argv[3]
SFUser = sys.argv[4]
SFUserPass = sys.argv[5]

# Use ElementFactory to get a SolidFireElement object.
sfe = ElementFactory.create(MVIP, SFUser, SFUserPass)
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