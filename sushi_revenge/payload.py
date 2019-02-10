#!/usr/bin/env python3

cmd = input()

payload = ''

maxval, CHAR_MAX = 0, 256
first = True

for c in cmd:
	expand = (maxval - ord(c)) // CHAR_MAX + 1
	maxval = CHAR_MAX * expand + ord(c)

	payload += '?' if first else '&'
	payload += '🍣[]=' + str(maxval)
	first = False

print(payload)
