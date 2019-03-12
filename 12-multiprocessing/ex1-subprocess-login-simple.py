# -*- encoding: utf-8 -*-
import re
import subprocess
from queue import Queue
from threading import Thread

login_test = subprocess.Popen(
    ['py', '-3', 'login_test.py'],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    bufsize=0,
)


def background_read(reader, queue: Queue):
    print('reading thread begin')
    while True:
        out = reader.read(1)
        if out:
            # print(out)
            queue.put(out.decode())
        else:
            # process exits or stdout is closed
            break
    print('reading thread end')
    queue.put(None)
    return 0


stdout_queue = Queue()
read_thread = Thread(
    target=background_read,
    kwargs={
        'reader': login_test.stdout,
        'queue': stdout_queue,
    }
)
read_thread.start()

prompt = ''

while login_test.poll() is None:
    out = stdout_queue.get(block=True)
    if out is None:
        break

    prompt += out

    USERNAME_PROMPT = 'Username: '
    PASSWORD_PROMPT = 'Password: '
    VERIFICATION_CODE_REGEX = re.compile(r'Input verification code \((\d{4})\): ')
    if prompt.startswith(USERNAME_PROMPT):
        print('username prompt found, input username')
        login_test.stdin.write(b'user\n')
        prompt = prompt[len(USERNAME_PROMPT):].strip()
    elif prompt.startswith('%s' % PASSWORD_PROMPT):
        print('password prompt found, input password')
        login_test.stdin.write(b'pass\n')
        prompt = prompt[len(PASSWORD_PROMPT):].strip()
    elif VERIFICATION_CODE_REGEX.search(prompt):
        m = VERIFICATION_CODE_REGEX.search(prompt)
        print('verification code prompt found, input verification code', m.group(1))
        login_test.stdin.write(m.group(1).encode('ascii') + b'\n')
        prompt = ''
    elif prompt.startswith('>>>'):
        print('command prompt found, input command')
        login_test.stdin.write(b'print(1 + 1)\nexit()\n')
        prompt = ''

read_thread.join()
print('final output: %r' % (prompt, ))
