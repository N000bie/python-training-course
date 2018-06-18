# -*- encoding: utf-8 -*-
import string
import pprint

rot13 = {
    k: chr((ord(k) - ord('a') + 13) % 26 + ord('a')) for k in string.ascii_lowercase
}

pprint.pprint(rot13)

cipher = 'sbe pbecbengr erny rfgngr naq snpvyvgvrf znantrzrag, genqvgvbany ohvyqvat pbageby flfgrzf ner zbivat gb gur ' \
         'vbg naq pbtavgvir cyngsbezf '

print(''.join(rot13.get(c, c) for c in cipher))
