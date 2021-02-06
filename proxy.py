import os
from colorama import Fore as F

print(F.LIGHTCYAN_EX+"""
-------------------------------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++Use A Tor Proxy Server+++++++++++++++++++++++++++++++++++++++++++
-------------------------------------------------------------------------------------------------------
█████╗ ░██████╗░░█████╗░██╗░░██╗██╗░░░██╗   ██╗░░░░░██╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝  ██║░░░░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░  ██║░░░░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░  ██║░░░░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░  ███████╗██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░  ╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
-------------------------------------------------------------------------------------------------------
++++++++++++++++++++++++++++++++++++++++++Coded By MacroTrojan+++++++++++++++++++++++++++++++++++++++++
-------------------------------------------------------------------------------------------------------
""")
name = input(F.CYAN+'Do You Want To Make User Porxys?:[Y,N?] ')

if name == 'Y':
    os.system('''
    sudo apt-get install proxychains
    sudo apt-get install tor
    service tor start
    cd /etc/
    sudo rm -r proxychains4.conf
    sudo rm -r proxychains.conf
    sudo wget -O /etc/proxychains.conf 'https://filetransfer.io/data-package/IJOJ6YzU/download'
    proxychains firefox google.com
    ''')
elif name == 'y':
    os.system('''
    sudo apt-get install proxychains
    sudo apt-get install tor
    service tor start
    cd /etc/
    sudo rm -r proxychains4.conf
    sudo rm -r proxychains.conf
    sudo wget -O /etc/proxychains.conf 'https://filetransfer.io/data-package/IJOJ6YzU/download'
    proxychains firefox google.com
    ''')
else:
    print('Good Bye')





