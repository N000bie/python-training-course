# -*- encoding: utf-8 -*-
import re

line = 'Cats are smarter than dogs'

matchObj = re.match(r'dogs', line)

if matchObj:
    print('matchObj.group():', matchObj.group())
else:
    print('No match!!')


searchObj = re.search(r'dogs', line)
if searchObj:
    print('search --> searchObj.group():', searchObj.group())
else:
    print('Nothing found!!')
