#!/usr/bin/env python3

import pwn

rem = pwn.remote('csie.ctf.tw', 10123)
for _ in range(100):
	rem.recvuntil('left\n')
	nums = rem.recvline().split()
	nums = sorted(map(lambda x: int(bytes.decode(x)), nums))
	result = ' '.join(str(num) for num in nums)
	rem.sendline(result)
rem.recvline()
print(rem.recvline())
