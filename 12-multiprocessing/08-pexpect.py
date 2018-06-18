# -*- encoding: utf-8 -*-
import sys

from pexpect.popen_spawn import PopenSpawn

child = PopenSpawn('cmd /c pause', logfile=sys.stdout, encoding='cp936')
child.expect('Press any key .*')
child.sendline('\n')
child.readline()
