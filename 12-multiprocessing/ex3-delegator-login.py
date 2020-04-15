import re

import delegator

p = delegator.run('python login_test.py', block=False)
print('PID of subprocess', p.pid)

p.expect('Username: ')
print('input username')
p.send('user')

p.expect('Password: ')
print('input password')
p.send('pass')

VERIFICATION_CODE_REGEX = re.compile(r'Input verification code \((\d{4})\): ')
p.expect(VERIFICATION_CODE_REGEX)
print('input verification code', p.subprocess.match.group(1))
p.send(p.subprocess.match.group(1))

try:
    p.expect('>>>')
    p.send('print(1 + 1)')
    p.send('exit()')
    p.block()
except:
    print('unmatched output:', p.subprocess.before)
finally:
    print('final output:', p.out)
