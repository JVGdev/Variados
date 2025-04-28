
section .text
global _start
_start:
	mov   	rax, 12          
	mov   	rdi, 0          
	syscall              

	mov   	qword [brk1], rax
	
	mov	rdi, [allb]
	add	rax, rdi
	lea   	rdi, [rax]  
	mov   	rax, 12
	syscall          
	
	lea 	rdi, [brk1]
	add 	rdi, 10
	cmp 	rax, rdi
	je .certo		;; Pula se tiver dado certo
	
	mov 	rdx, len2	;;
	lea 	rsi, [deuN]	;;
	mov 	rdi, 1		;; Printa mensagem que não deu
	mov 	rax, 1		;; 
	syscall			;;
	
	mov 	rdi, 1		;;
	mov 	rax, 60		;; Exit(1)
	syscall			;; 

	.certo:
	mov 	rdx, len1	;;
	lea 	rsi, [deu]	;;
	mov 	rdi, 1		;; Printa mensagem que deu
	mov 	rax, 1		;;
	syscall			;;

	mov 	rdx, len2	;;
	lea 	rsi, [deuN]	;;
	mov 	rdi, 1		;;
	mov 	rax, 0		;;
	syscall			;;
	

	xor 	rdi, rdi	;; 
	mov 	rax, 60		;; Exit
	syscall			;;


section .data
	deu dw "Memória alocada com sucesso!", 0xA, 0
	len1 equ $ - deu
	deuN dw "Memória não foi alocada com sucesso", 0xA, 0
	len2 equ $ - deuN
	
	allb db 10
	
section .bss
	brk1 resq 1
