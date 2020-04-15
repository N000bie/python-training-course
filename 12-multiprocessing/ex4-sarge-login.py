import re

from sarge import Capture, Feeder, run

f = Feeder()
c = Capture(buffer_size=1)
p = run('python login_test.py', async_=True, stdout=c, input=f)

c.expect('Username:')
print('input username')
f.feed('user\n')

c.expect('Password:')
print('input password')
f.feed('pass\n')

VERIFICATION_CODE_REGEX = re.compile(rb'Input verification code \((\d{4})\): ')
match = c.expect(VERIFICATION_CODE_REGEX)
print('input verification code', match.group(1))
f.feed(match.group(1) + b'\n')

c.expect('>>>', timeout=5)
f.feed('print(1 + 1)\n')
f.feed('exit()\n')
p.wait()

print('final output:\n', b''.join(c.readlines()).decode('utf-8'))
