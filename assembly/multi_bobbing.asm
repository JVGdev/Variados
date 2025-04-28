
section .text

;; forkj:
;;	} Começa um fork e pula para determinada etiqueta(label)
;;
;; Argumentos: 
;;	rax -> recebe a etiqueta
;;
;; Retorna:
;;	rax <- retorna o PID
;;
global forkj
forkj:
	push rax
	
	mov rax, 57
	syscall

	cmp rax, 0x00
	pop rdi
	je .pai
	jl .erro
	jmp rdi

	.erro:
	
	
	
	.pai:
	ret
	
