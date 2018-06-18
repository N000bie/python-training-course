# -*- encoding: utf-8 -*-
import re

line = 'Cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*', line)

if matchObj:
    print('matchObj.group():', matchObj.group())
    print('matchObj.group(0):', matchObj.group(0))
    print('matchObj.group(1):', matchObj.group(1))
    print('matchObj.group(2):', matchObj.group(2))
else:
    print('No match!!')
