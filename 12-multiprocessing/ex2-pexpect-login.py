# -*- encoding: utf-8 -*-
import re

from pexpect.popen_spawn import PopenSpawn

login_test = PopenSpawn(
    ['py', '-3', 'login_test.py'],
)

login_test.expect('Username: ')
print('input username')
login_test.sendline('user')

login_test.expect('Password: ')
print('input password')
login_test.sendline('pass')

VERIFICATION_CODE_REGEX = re.compile(rb'Input verification code \((\d{4})\): ')
login_test.expect(VERIFICATION_CODE_REGEX)
print('input verification code', login_test.match.group(1))
login_test.sendline(login_test.match.group(1))


try:
    login_test.expect('>>>')
    login_test.sendline('print(1 + 1)')
    login_test.sendline('exit()')
except:
    print('unmatched output:', login_test.before)
finally:
    print('final output:', login_test.read())
