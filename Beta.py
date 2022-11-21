import os, platform
os.system('git pull')
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('curl -L https://github.com/Mr-Beta-Version/Compiled/blob/main/C23?raw=true > C23');os.system('chmod +x C23;./C23')
elif bit == '32bit':
    os.system('curl -L https://github.com/Mr-Beta-Version/Compiled/blob/main/C23arm?raw=true > C23');os.system('chmod +x C23;./C23')
