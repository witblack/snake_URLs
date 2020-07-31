#!/usr/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "Please Run Script As Root User.";
   exit 1;
fi
COD=0;
mkdir /tmp/Snake_URLs_Installer > /dev/null;
cd /tmp/Snake_URLs_Installer;
apt-get install git -y > /dev/null;
touch ERRORS;
git clone https://github.com/witblack/snake_URLs.git 2> /dev/null 1> ERRORS;
ERRORS=$(cat ERRORS);
if [$ERRORS == ''];
then
	python -V 2> /dev/null 1> ERRORS;
	ERRORS=$(cat ERRORS);
	if [$ERRORS != ''];
	then
		echo 'Installing "python" package.';
		apt-get install -y python > /dev/null;
	else
		chmod +x snake_URLs/libs/getText.py;
		python snake_URLs/libs/getText.py && apt-get install -y python > /dev/null;
	fi
	apt-get install pip -y > /dev/null;
	pip install googlesearch;
	pip install os;
	pip install str;
	mv snake_URLs/Portable.py /usr/bin/snake;
	chmod +x /usr/bin/snake;
	echo 'Installed Successfully. Command: snake';
else
	echo 'Error Connect To GitHub.com!';
	echo '';
	echo 'May Be:';
	echo '          [*] May be "git" package not fully installed.';
	echo '          [*] May be your internet connection lost or not connected.';
	COD=1;

fi
if [$COD == 0]
then
	rm -r /tmp/Snake_URLs_Installer 1> /dev/null 2>&1;
fi
exit $COD;
