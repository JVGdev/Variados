section .text

extern sbobf
extern print

global _start
_start:
	
	mov rax, out1
	mov rdi, buff1
	mov rsi, 6123
	mov [out1], dword 60;
	call sbobf

	lea rdi, [buff1]
	call print
	mov rdi, 1
	lea rsi, [rax]
	mov rdx, 20
	mov rax, 1
	syscall

	mov rax, 60
	xor rdi, rdi
	syscall

section .data
buff1: db "Alo, estou printando uma mensagem %d isso veio depois da concatenação.", 10, 0
str1: db "(isso está sendo 'concatenado' em runtime)", 0

section .bss
out1: resb 60


