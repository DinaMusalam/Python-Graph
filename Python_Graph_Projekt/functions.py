# -*- coding: cp1252 -*-

import os, getpass

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

# Standardfunktion för att ta emot endast int i input
# Indata: max (antalet val som kan göras), prompt (texten för input)
def input_int(max=0, prompt="Gör ett val: ", clear=True):
	correct = False
	
	while correct != True:
		try:
			choice = int(raw_input(prompt))
			if isinstance(choice, int):
				if choice <= max:
					if clear == True:
						os.system('cls' if os.name=='nt' else 'clear')
					return choice
				elif choice > max:
					print2("Inkorrekt val, försök igen", 'fail')
			elif not isinstance(choice, int):
				print2("Inkorrekt val, försök igen", 'fail')
			
		except ValueError:
			print2("Inkorrekt val, försök igen", 'fail')

def input2(prompt="Gör ett val: ", clear=True):
	choice = raw_input(prompt)
	if clear == True:
		os.system('cls' if os.name=='nt' else 'clear')
	return choice
			

def print2(text, type=None, clear=False, newline=True):
	if clear == True:
		os.system('cls' if os.name=='nt' else 'clear')
	if type.lower() == 'blue' or type.lower() == 'okblue':
		print bcolors.OKBLUE+text+bcolors.ENDC
	if type.lower() == 'green' or type.lower() == 'okgreen':
		print bcolors.OKGREEN+text+bcolors.ENDC
	if type.lower() == 'yellow' or type.lower() == 'orange' or type.lower() == 'warning':
		print bcolors.WARNING+text+bcolors.ENDC
	if type.lower() == 'red' or type.lower() == 'fail' or type.lower() == 'error':
		print bcolors.FAIL+text+bcolors.ENDC
	if newline == True:
		print
