#!/usr/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "Please Run Script As Root User.";
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
	pip install str;
	mv snake_URLs/Portable.py /usr/bin/snake;
	chmod +x /usr/bin/snake;
	echo 'Installed Successfully. Command: snake';
else
	echo 'Error Connect To GitHub.com! Check "git" Package Be Installed.';
	COD=1;
fi
if [$COD == 0]
then
	rm -r /tmp/Snake_URLs_Installer 1> /dev/null 2>&1;
fi
exit $COD;
