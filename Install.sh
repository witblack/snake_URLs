#!/usr/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "Please Run Script As Root User." ;
   exit 1;
fi
COD=0;
mkdir /tmp/Snake_URLs_Installer 1> /dev/null 2>&1;
cd /tmp/Snake_URLs_Installer;
touch ERRORS;
git clone https://github.com/witblack/snake_URLs.git 2> /dev/null 1> ERRORS;
ERRORS=$(cat ERRORS);
if [$ERRORS == ''];
then
	apt-get install pip -y;
	pip install googlesearch;
	pip install os;
	mv snake_URLs/Portable.py /usr/bin/snake;
	chmod 555 /usr/bin/snake;
	echo 'Installed Successfully'
else
	echo 'Error Connect To GitHub.com! Check "git" Package Be Installed.';
	COD=1;
fi
rm -r /tmp/Snake_URLs_Installer 1> /dev/null 2>&1;
exit $COD;
