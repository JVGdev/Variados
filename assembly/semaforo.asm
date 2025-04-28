
section .text
global _start
_start:
			
	mov rax, 57		;; número do Fork 
	syscall			;; 
	
	xor rdi, rdi		;; Fork retorna 0 se for o processo child, logo
	cmp rax, rdi		;; zero o rdi e comparo com o retorno pra checar
	je .pai			;; se o processo atual é o child
	
	mov rdx, 24		;; Tamanho do buffer
	lea rsi, [teste2]	;; Buffer
	mov rdi, 1		;; File Descriptor (terminal)
	mov rax, 1		;; Syscall write
	syscall			;;
	
	xor rdx, rdx		;; Null no envp
	xor rsi, rsi		;; Null no argv
	lea rdi, [file1]	;; Path pro execv
	mov rax, 59		;; Call do execv
	syscall			;;
	
	.pai:			;; Se for o pai...
	
	mov rdx, 22		;; Tamanho do buffer
	lea rsi, [teste1]	;; Buffer
	mov rdi, 1		;; File descriptor
	mov rax, 1		;; Syscall write
	syscall			;;

	xor rdx, rdx		;; Null no envp
	xor rsi, rsi		;; Null no argv
	lea rdi, [file1]	;; Path pro execv
	mov rax, 59		;; Call do execv
	syscall			;;
	
	.end:
	xor rdi, rdi		;; Code 0
	mov rax, 60		;; exit
	syscall			;;

section .data
	file1 dw "testeOpen", 0
	teste1 db "Este é o processo pai", 10, 0
	teste2 db "Este é o processo filho", 10, 0

