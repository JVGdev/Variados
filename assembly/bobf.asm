
section .text

global print
;;
;; void()
;;
;; rdi <- char*
;;
print:
	push rdi	
	call strlen
	
	mov rdx, rax
	pop rsi
	mov rdi, 1
	mov rax, 1
	syscall
	
	ret


global sbobf
;; loopar cada byte do buffer, transformando digitos em chars, e quando aparecer uma '%', pular para a área de tratamento para printar um int, ou string, ou algo mais.
;; rax <- Endereço de memória do buffer destino  
;; rdi <- Endereço do Buffer máscara
;; rsi <- Ínicio da 'lista' de preenchimentos
sbobf: 
	
	mov r10, rdi
	mov rdx, rax
	.loop:
		
	mov r9b, byte [r10]
	
	cmp r9b, 0
	je sbobf.end
	
		
	mov rdi, 1
	mov sil, r9b
	mov rdx, 1
	mov rax, 1
	syscall

	
	mov [rdx], r9b
		
	inc rdx
	inc r10
	jmp sbobf.loop
	

	.end:
	ret


global strlen
;;
;; char*
;;
;; rax -> Tamanho da string
;; rdi <- buffer de chars para contar (tem que terminar em 0)
;;
strlen:
	xor rax, rax	
	.loop:
	cmp byte [rdi], 0
	je strlen.end
	
	inc rdi
	inc rax
	
	jmp strlen.loop

	.end:
	ret
	
	
