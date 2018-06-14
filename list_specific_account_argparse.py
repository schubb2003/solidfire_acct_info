#!/usr/local/bin/python
# Author: Scott Chubb scott.chubb@netapp.com
# Written for Python 3.4 and above
# No warranty is offered, use at your own risk.  While these scripts have been tested in lab situations, all use cases cannot be accounted for.
# This script takes input arguments and looks up accounts by ID or IDs by accounts
import sys
import argparse
from solidfire.factory import ElementFactory

# Set vars for connectivity using argparse
def parse_inputs():
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
    return args


def main():
    agrv = parse_inputs()
    src_mvip = argv.sm
    src_user = argv.su
    src_pass = argv.sp
    vol_acct = argv.a
    acct_type = argv.t
    
    if acct_type == "id":
        accountInfo = int(vol_acct)
    
    else:
        accountInfo = str(vol_acct)
    
    # Use ElementFactory to get a SolidFireElement object.
    sfe = ElementFactory.create(src_mvip, src_user, src_pass)
    list_accounts_result = sfe.list_accounts()
    def main():
        # If the account type was submitted as an ID process it as an integer
        if acct_type == "id":
            for account in list_accounts_result.accounts:
                    if vol_acct.account_id == int(accountInfo):
                        print("Account name is:\t %s" % vol_acct.username) 
                    else:
                        print("Account was not found, please check the account ID")

        else:
            #By username
            for account in list_accounts_result.accounts:
                    if vol_acct.username == accountInfo:
                        print("account ID is:\t %s" % vol_acct.account_id)
                    else:
                        print("Account ID was not found, please check the account name")

if __name__ == "__main__"
    main()