#!/usr/bin/env python3

import base64
bfdict = {'B': '>', 'a': '<', 'm': '+', 'b': '-', 'o': '.', 'O': ',', 'F': '[', 'x': ']', '\n': ''}
with open('data', 'r') as f_data:
    code_b64 = f_data.read()
    code = base64.b64decode(code_b64.encode()).decode()
    code = ''.join(bfdict[x] for x in code)
    with open('brainfuck', 'w') as f_code:
        f_code.write(code)
