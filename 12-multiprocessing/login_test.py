# -*- encoding: utf-8 -*-
import random
import time
from code import interact
from six.moves import input


def main():
    username = input('Username: ')
    password = input('Password: ')
    verification_code = ''.join(str(random.randint(0, 9)) for _ in range(4))
    retrieved_code = input('Input verification code (%s): ' % (verification_code, ))
    time.sleep(random.randint(1, 3))
    if verification_code != retrieved_code:
        print('Incorrect verification code')
    elif username == 'user' and password == 'pass':
        interact(banner='Hello, %s' % (username,), exitmsg='Goodbye, %s' % (username,))
    else:
        print('invalid username or password')


if __name__ == '__main__':
    main()
