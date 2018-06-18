# -*- encoding: utf-8 -*-
import subprocess

ping = subprocess.Popen(
    ['ping', '-t', '127.0.0.1'],
    stdout=subprocess.PIPE
)

for i in range(5):
    print(ping.stdout.readline())

ping.kill()
