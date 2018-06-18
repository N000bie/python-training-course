# -*- encoding: utf-8 -*-
import re
import pprint

pattern = re.compile(r'^(.*?):(?:.*?:){4}(.*?):.*?$', re.MULTILINE)

with open('passwd.txt', 'r') as f:
    content = f.read()
    user_homes = pattern.findall(content)

pprint.pprint(user_homes)
