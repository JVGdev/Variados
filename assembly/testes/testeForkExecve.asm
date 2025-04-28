
section .text

extern forkj

global _start
_start:
			
	;mov rax, 57		;; número do Fork 
	;syscall			;; 
	
	lea rax, .pai
	call forkj

	mov [pid], rax	

	xor rdi, rdi		;; Fork retorna 0 se for o processo filho, logo
	cmp rax, rdi		;; zero o rdi e comparo com o retorno pra checar
	jg .pai 		;; se o processo atual é o filho
	jz .filho

		
	mov rdi, 1
	mov rax, 60
	syscall
	
	.filho:
	mov rdx, 25		;; Tamanho do buffer
	lea rsi, [teste2]	;; Buffer
	mov rdi, 1		;; File Descriptor (terminal)
	mov rax, 1		;; Syscall write
	syscall			;;
	
	xor rdx, rdx		;; Null no envp
	xor rsi, rsi		;; Null no argv
	lea rdi, [file2]	;; Path pro execv
	mov rax, 59		;; Call do execv
	syscall			;;
	
	mov rdi, 1
	mov rax, 60
	syscall

	.pai:			;; Se for o pai...
	

	mov rdx, len1		;;
	lea rsi, [msg1]		;;
	mov rdi, 1		;;
	mov rax, 1		;;
	syscall
	
	xor r10, r10		;;
	xor rdx, rdx		;;
	lea rsi, [status]	;;
	mov rdi, [pid]		;;
	mov rax, 61		;;
	syscall 

	mov rdx, len2		;;
	lea rsi, [msg2]		;;
	mov rdi, 1		;;
	mov rax, 1		;;
	syscall
	

	.end:
	mov rdi, 0
	mov rax, 60		;; exit
	syscall			;;

section .data
	file1 dw "testeMmap", 0
	file2 dw "./testes/testeBrk", 0
	
	teste1 db "Este é o processo pai", 10, 0
	teste2 db "Este é o processo ", 40, 41, 42, 61, 70, 10, 0
	
	msg1 db "Esperando o mininu", 10, 0
	len1 equ $ - msg1
	
	msg2 db "Mininu acabou-se", 10, 0
	len2 equ $ - msg2

section .bss
	pid resq 1
	status resb 4
	

