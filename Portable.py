#!/usr/bin/python
# coding: latin-1
#---------------------------
# Writed By WitBlack HAcker
#---------------------------

try:
	from googlesearch import search
	from os import system
	from os import name
	from os.path import exists
except:
	print('Some libs not installed! Pls install all "requires.txt".')
	exit(1)
def Clear():
	if name == 'nt':
		system('cls')
	else:
		system('clear')
def Banner():
	Clear()
	print(' __     __     __      __        __         |')
	print('/\ \   /\ \   /\ \    /\_\      /\ \        |   Snake     _______')
	print('\ \ \  \ \ \  \ \ \   \/_/     _\_\_\____   |      URLs  /_|___|_\\')
	print(' \ \ \  \ \ \  \ \ \     __   /\_________\  |           |_.|   |_.|')
	print('  \ \ \  \ \ \  \ \ \   /\ \  \/___/\ \__/  |     ______| .|    \'\'')
	print('   \ \ \__\_\ \__\_\ \  \ \ \      \ \ \    |    /______|_/')
	print('    \ \_____________\_\  \ \_\      \ \_\   |~~~~~~~~~~~~~~~~~~~~~~~')
	print('     \/_______________/   \/_/       \/_/   |~~~~~~~~~~~~~~~~~~~~~~~')
	print('')
	print(' ________     __     _________     ____________      __')
	print('/\  ____ \   /\ \   /\  _____ \   /\  ________/\    /\ \    __')
	print('\ \ \__/\ \  \ \ \  \ \_\___/\ \  \ \ \______/\ \   \ \ \  / /\\')
	print(' \ \ \_\_\ \  \ \ \  \/_/___\_\ \  \ \ \     \/_/__  \ \ \/ / /')
	print('  \ \  ____ \  \ \ \   /\  _____ \  \ \ \       /\ \  \ \ \/_/____ ')
	print('   \ \ \__/\ \  \ \ \  \ \ \___/\ \  \ \ \      \ \ \  \ \  ___ \ \\')
	print('    \ \ \_\_\ \  \ \ \  \ \ \__\_\ \  \ \ \______\/  \  \ \ \  \ \ \\')
	print('     \ \_______\  \ \_\  \ \________\  \ \___________/   \ \_\  \ \_\\')
	print('      \/_______/   \/_/   \/________/   \/__________/     \/_/   \/_/')
	print("\nProgramed By WitBlack HAcker. - Web ~> Https://BugZone.ir")
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print('VERSION 1.0.4')
if not (exists('C:/Windows/') or exists('/etc/')):
	exit('Sorry! Your OS Not Support. :(')
Banner()
try:
	print("\nEnter 'h' For Get Help. 'q' for exit.")
	Query = raw_input("Please Enter Query ~> ")
	if str.lower(Query) == "h" or str.lower(Query) == 'help':
		print('For See More Information Read:')
		exit('http://www.googleguide.com/advanced_operators_reference.html')
	elif str.lower(Query) == 'q' or str.lower(Query) == 'exit' or str.lower(Query) == 'quit':
		exit("\n\nQuiting...")
	WriteType = ''
	SaveInFile = raw_input('Do You Want Save In A File? [y/n] ')
	if str.lower(SaveInFile) == 'y' or str.lower(SaveInFile) == 'yes' or str.lower(SaveInFile) == 'ok':
		while WriteType == '':
			SaveInFile = raw_input('Enter Name Or File Address: ')
			if exists(SaveInFile):
				WriteType = raw_input('File Or Address Exist. Continue? [y/n] ')
				if str.lower(WriteType) == 'yes' or str.lower(WriteType) == 'y' or str.lower(WriteType) == 'ok':
					WriteType = raw_input('Append or Write? [a/w] ')
					if str.lower(WriteType) == 'w' or str.lower(WriteType) == 'write':
						WriteType = 'Write'
					else:
						WriteType = 'Append'
				else:
					exit("\nCancelled Search!")
			else:
				WriteType = 'Write'
	if WriteType == '':
		print("Searching And Showing Result(s) ...\n\n")
	elif str.lower(WriteType) == 'w' or str.lower(WriteType) == 'write':
		print('Searching And Write Result(s) At "' + SaveInFile + '"')
	else:
		print('Searching And Append Result(s) At "' + SaveInFile + '"')
	if WriteType != '':
		if str.lower(WriteType) == 'w' or str.lower(WriteType) == 'write':
			File = open(SaveInFile ,'w')
		else:
			File = open(SaveInFile ,'a')
	for Result in search(Query):
		if WriteType != '':
			File.write("\n" + Result)
		else:
			print(Result)
except:
        print("Exit.\n")
        exit(1)
if WriteType != '':
	File.close()
print("\n\nQuiting...")
