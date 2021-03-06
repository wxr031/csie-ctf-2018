#!/usr/bin/env python3

import base64, re
pat = 'BBFaamBBbxB(m*)Fa(m*)Bbxa(m*)aFbBbaxmBFabBFbxx'
re_pat = re.compile(pat)
flag = ''
with open('data', 'r') as fp:
    code = fp.read()
    code = base64.b64decode(code.encode()).decode()
    flag_list = code.split('O')
    for f in flag_list:
        pat = re_pat.search(f)
        if pat is not None:
            n1, n2, n3 = len(pat.group(1)), len(pat.group(2)), len(pat.group(3))
            flag += chr(n1 * n2 + n3)
print(flag)
