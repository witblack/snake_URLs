#!/usr/bin/python
# coding: latin-1

#Import Libs From Python
from googlesearch import search
from os import system
from os.path import exists
#from termcolor import colored
#from rhinoscriptsyntax import CreateColor as cc

#Setting Colors
bblue = "\\[\\033[0;38;5;12m\\]"
black = "\\[\\033[0;38;5;0m\\]"
blue = "\\[\\033[0;38;5;4m\\]"
coldblue = "\\[\\033[0;38;5;33m\\]"
cyan = "\\[\\033[0;38;5;6m\\]"
green = "\\[\\033[0;38;5;2m\\]"
iceblue = "\\[\\033[0;38;5;45m\\]"
magenta = "\\[\\033[0;38;5;55m\\]"
myred = "\\[\\033[01;31m\\]"
orange = "\\[\\033[0;38;5;130m\\]"
red = "\\[\\033[0;38;5;1m\\]"
smoothblue = "\\[\\033[0;38;5;111m\\]"
smoothgreen = "\\[\\033[0;38;5;42m\\]"
turqoise = "\\[\\033[0;38;5;50m\\]"
white = "\\[\\033[0;38;5;6m\\]"
yellow = "\\[\\033[0;38;5;3m\\]"

#Functions
def Clear():
	if OS == 'Windows':
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
	print("\nProgramed By WitBlack HAcker. - Web ~> Https://0man.ir")
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#Checking Os Type
if exists('C:/Windows/'):
	OS = 'Windows'
elif exists('/etc/'):
	OS = 'Linux'
else:
	exit('Sorry! Your OS Not Support. :(')

#Clear The Page And Showing Banner
Banner()

#Send A Tip For Users
system('wget https://0man.ir/Server/Snake_URL_TIP.php -O /tmp/SnakeURLs_TIP 1> /dev/null 2>&1')

#Geting Help Or Google Search Options
print("\nEnter 'h' For Get Help. 'q' for exit.")
Query = raw_input("Please Enter Query ~> ")

#Checking Input. If User Enter 'h' Showing Help And Exit.
#Also Check 'q' For Exit
if str.lower(Query) == "h" or str.lower(Query) == 'help':
	print('For See More Information Read:')
	exit('http://www.googleguide.com/advanced_operators_reference.html')
elif str.lower(Query) == 'q' or str.lower(Query) == 'exit' or str.lower(Query) == 'quit':
	exit("\n\nQuiting...")

#Saving Export File Option
WriteType = ''
SaveInFile = raw_input('Do You Want Save In A File? [y/n] ')
if str.lower(SaveInFile) == 'y' or str.lower(SaveInFile) == 'yes' or str.lower(SaveInFile) == 'ok':
	#If It's Ture Ask File Name Or File Address. If File Exist Ask Ower Write? Append Or Write?
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

#Showing Resault Report Type
if WriteType == '':
	print("Searching And Showing Result(s) ...\n\n")
elif str.lower(WriteType) == 'w' or str.lower(WriteType) == 'write':
	print('Searching And Write Result(s) At "' + SaveInFile + '"')
else:
	print('Searching And Append Result(s) At "' + SaveInFile + '"')

#Opeing File For Write Or Append If Need Write
if WriteType != '':
	if str.lower(WriteType) == 'w' or str.lower(WriteType) == 'write':
		File = open(SaveInFile ,'w')
	else:
		File = open(SaveInFile ,'a')

#Gettind Resualt(s) One By One. Show Or Write Or Appned Them
for Resualt in search(Query):
	#, tld="co.in", num=10, stop=1, pause=2):
	if WriteType != '':
		File.write("\n" + Resualt)
	else:
		print(Resualt)

#Close Opened File And Exit
if WriteType != '':
	File.close()
print("\n\nQuiting...")
