import os
from subprocess import check_output
#from termcolor import colored

status = str(check_output(['nordvpn', 'status']))

if os.environ.get('BLOCK_BUTTON'):
   if (os.environ['BLOCK_BUTTON'] == '1'):
      _ = os.system('nordvpn connect > /dev/null 2>&1')
   elif (os.environ['BLOCK_BUTTON'] == '2'):
      _ = os.system('nordvpn disconnect > /dev/null 2>&1')
   elif (os.environ['BLOCK_BUTTON'] == '3'):
      _ = os.system('nordvpn disconnect > /dev/null 2>&1; nordvpn connect > /dev/null 2>&1')

if 'Connecting' in status or 'Restarting' in status:
    msg = 'CONNECTING..\nCONNECTING..\n#0000FF'
elif not ' Connected' in status:
    msg = "UNPROTECTED!\nUNPROTECTED!\n#FF0000"
else:
    server = status.split("Current server: ")[1][:12]
    msg = f'{server}\n{server}\n#00FF00'

print(msg)
