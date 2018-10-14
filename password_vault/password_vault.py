#! /usr/bin/python3
# Simple program to store passwords to various accounts.
import os

# file_object = open('accounts.txt', 'rw')
accounts = []

def get_func():
	"""
	Gets User input to determine what function to execute.
	"""
	prompt = 'Would you like to view an accounts username and password or'
	prompt_pt2 = ' add a new one? [view/add]\n'
	prompt = prompt + prompt_pt2
	ui = input(prompt).strip().lower()
	while ui not in ('view', 'add'):
		print('Invalid input. Enter \"view\" or \"add.\"')
		ui = input().strip().lower()
	return ui

def view_account():
	"""
	Retrieves username/password of specified account 
	"""
	acct = input('Which account credentials would you like to view?\n')


def add_account():
	"""
	Where the user adds login credentials for an account.
	"""
	while True:
		acct = input('What account are these login credentials for?\n').title()
		un = input('What is the username of this account?\n').strip()
		pw = input('What is the password of this account?\n').strip()
		pw_ver = input('Re-enter password for verification.\n').strip()
		
		while pw != pw_ver:
			print('Passwords do not match.')
			pw = input('What is the password of this account?\n').strip()
			pw_ver = input('Please verify your password.\n').strip()
		
		new_acct = {
			'Account': acct,
			'Username': un,
			'Password': pw,
			}
		
		print(new_acct)
		
		cred_ver = input('Is this information correct? [y/n]\n').lower().strip()
		if cred_ver == 'y':
			accounts.append(new_acct)
			while cred_ver not in ('y', 'n', 'yes', 'no'):
				print('Invalid input. Enter \"y\" or \"n\"')	
				cred_ver = input().lower().strip()
	
		cont = input('Do you want to add another account? [y/n]\n').lower()
		if cont == 'n':
			break;
			while cont not in ('y', 'n', 'yes', 'no'):
				print('Invalid input. Enter \"y\" or \"n\"')	
				cont = input().lower().strip()			
	
func_trig = get_func()

# if func_trig == 'view':
# 	view_account()
if func_trig == 'add':
	add_account()
