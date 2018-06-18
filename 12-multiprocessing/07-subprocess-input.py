# -*- encoding: utf-8 -*-
import subprocess

pause = subprocess.Popen(
    ['cmd', '/c', 'pause'],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
)

# print(pause.stdout.read())
# pause.stdin.write(b'a')
# pause.stdin.flush()
# print(pause.stdout.read())

out, err = pause.communicate(b'\n')
print(out)
print('done')
