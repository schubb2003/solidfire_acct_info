#!/usr/local/bin/python
# Change sf-mvip.demo.netapp.com to your MVIP name or IP
# Change admin to your user account
# Change Netapp1! to your password

from solidfire.factory import ElementFactory

# Use ElementFactory to get a SolidFireElement object.
sfe = ElementFactory.create("sf-mvip.demo.netapp.com", "admin", "Netapp1!")
list_accounts_result = sfe.list_accounts()

for account in list_accounts_result.accounts:
    print(account)
    
# To do the same with CLI arguments
# Uncomment the lines below
# import sys
# from solidfire.factory import ElementFactory
#
#if len(sys.argv) < 4:
#    print("insufficient arguments supplied, usage is \n"
#          " python <script_name> <mvip> <user> <password>")
#
#mvip_ip = sys.argv[1]
#user_name = sys.argv[2]
#user_pass = sys.argv[3]
#
# sfe = ElementFactory.create(mvip_ip, user_name, user_pass)
# list_accounts_result = sfe.list_accounts()

# for account in list_accounts_result.accounts:
#    print(account)
