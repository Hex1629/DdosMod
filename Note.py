import os
import sys
import time
from time import sleep
#BLACK = '\033[30m'
#RED = '\033[31m'
#GREEN = '\033[32m'
#YELLOW = '\033[33m'
#BLUE = '\033[34m'
#MAGENTA = '\033[35m'
#CYAN = '\033[36m'
#WHITE = '\033[37m'
#UNDERLINE = '\033[4m'
#RESET = '\033[0m'
def slowprints(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)
slowprints('''\033[33mDDOSMOD \033[0m''')
slowprints('''\033[36mWelcome to DdosMod
Update:

New DDos

Cr.Malam-x

Cr.Leeon123

Cr. Ha3MrX

Cr. 4L13199

Cr.Pavithran-R

Link Ddos TCP:https://github.com/Malam-X/TCP-Flood

Link Ddos Tcp/udp:https://github.com/Leeon123/TCP-UDP-Flood

Link Ddos Attack:https://github.com/Ha3MrX

Link Ddos LITE:https://github.com/4L13199/LITEDDOS

Link Ddos Hammer:https://github.com/Pavithran-R/Hammer/\033[0m''')
slowprints('''\033[34m+----------------------------------------------+\033[0m''')
sys.exit()
