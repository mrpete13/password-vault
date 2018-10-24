#! /usr/bin/python3

from vault_funcs import get_func, add_account, add_another_account, view_account
# from encrypt import 

# file_object = open('accounts.txt', 'rw')
accounts = []

func_trig = get_func()

if func_trig == 'add':
	while True:
		add_account()
		# verify_cred()
		add_another_acct()
# elif func_trig == 'view':
# 	view_account()