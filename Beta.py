import os, platform
os.system('git pull')
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from C23 import menu
    menu()
elif bit == '32bit':
    from C23arm import menu
    menu()
