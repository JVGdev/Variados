

section .data
	path: db "./teste.txt"
	openError: db "Deu não man", 10	

section .text
global _start
_start:
	
	mov rdx, 010000
	mov rsi, 010000
	lea rdi, [path] 
	mov rax, 2
	syscall

	cmp rax, -1
	jne .opened
	
	mov rdx, 13
	lea rsi, [openError]
	mov rdi, 1
	mov rax, 1
	syscall


	.opened:

	mov rax, 60
	xor rdi, rdi
	syscall
