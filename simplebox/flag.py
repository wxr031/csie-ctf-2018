#!/usr/bin/env python3

import base64, re
bfdict = {'B': '>', 'a': '<', 'm': '+', 'b': '-', 'o': '.', 'O': ',', 'F': '[', 'x': ']', '\n': ''}
pat = 'BBFaamBBbxB(m*)Fa(m*)Bbxa(m*)aFbBbaxmBFabBFbxx'
re_pat = re.compile(pat)
flag = ''
with open('data-6a04a913cf94d5869e9e90b22fcb5543', 'r') as fp:
    code = fp.read()
    code = base64.b64decode(code.encode()).decode()
    flag_list = code.split('O')
    for f in flag_list:
        pat = re_pat.search(f)
        if pat is not None:
            n1, n2, n3 = len(pat.group(1)), len(pat.group(2)), len(pat.group(3))
            flag += chr(n1 * n2 + n3)
print(flag)
