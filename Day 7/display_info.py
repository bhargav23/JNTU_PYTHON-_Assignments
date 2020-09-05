# -*- coding: utf-8 -*-

#Write a Python program to display the below information.

#display the current user name
import getpass
print(getpass.getuser())

#display current working directory
import os
os.getcwd()

#display Operating system name
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())

#display process id of your running program
# Python program to explain os.getpid() method 
	
# importing os module 
import os 

# Get the process ID of 
# the current process 
pid = os.getpid() 


# Print the process ID of 
# the current process 
print(pid) 

#display the current timestamp
from datetime import datetime

dateTimeObj = datetime.now()
print(dateTimeObj)

#display yesterday’s date
#display tomorrow’s date

import datetime 
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)

#display all the environment variables that are existing
import os
print(os.environ)

#display the python executable path ( just like ‘which python3’ in Linux )

import sys
print(sys.executable)

