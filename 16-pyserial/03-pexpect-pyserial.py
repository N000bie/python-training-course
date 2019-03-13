# -*- encoding: utf-8 -*-
# this script can only be run on Linux or Unix OS
# socat must be installed and a pair of virtual serial port must be created as follow if no hardware serial port available

# create vsp pair in one terminal
#     sudo socat -d -d PTY,raw,echo=0,link=/dev/ttyVA00 PTY,raw,echo=0,link=/dev/ttyVB00
# keep it running and connect one end of the VSP in another terminal
#     sudo chmod 777 /dev/ttyVA00 /dev/ttyVB00
#     socat -d -d open:/dev/ttyVB00,nonblock,echo=0,raw stdio
# now run the script in the 3rd terminal
#     python 03-pexpect-pyserial.py
# then input in the second terminal (simulate serial device) and watch responses from pexpect
#     Username:
#     Password:
from pexpect import TIMEOUT
from pexpect.fdpexpect import fdspawn
from serial import Serial

with Serial('/dev/ttyVA00', 115200, timeout=0) as com_port:
    login_test = fdspawn(
        com_port.fileno(),
    )

    login_test.expect('Username:')
    print('input username')
    login_test.sendline('user')

    login_test.expect('Password:')
    print('input password')
    login_test.sendline('pass')

    login_test.expect('!')
    try:
        print(login_test.before)
    except TIMEOUT:
        pass

