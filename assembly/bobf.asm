
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
	
 	mov  	rdx, rax
	pop 	rsi
	mov 	rdi, 1
	mov 	rax, 1
	syscall
	
	ret


global sbobf
;; loopar cada byte do buffer, transformando digitos em chars, e quando aparecer uma '%', pular para a área de tratamento para printar um int, ou string, ou algo mais.
;; rax <- Endereço de memória do buffer destino  
;; rdi <- Endereço do Buffer máscara
;; rsi <- Ínicio da 'lista' de preenchimentos
sbobf: 
	
	mov 	r10, rdi
	mov 	rdx, rax
	
	.loop:
	mov 	r9b, byte [r10]
	
	cmp	r9b, 0
	je sbobf.end
	
	cmp	r9b, '%'
	jne sbobf.pass
	
	inc r10
	mov 	r9b, byte [r10]
	inc r10	

	; ***Switch cases*** ;
	cmp	r9b, 'd'		;; Usar 'and' e 'or' ou 'bt' e checar a 'CF' para criar uma 'itoa'?
	je sbobf.int			;; SERIA A DIVISÃO A LUZ NO FIM DO TÚNEL?
					;; A cada divisão por 100, 1000, e tal, checar se o resultado é maior que zero, se não for, significa que acabou?
					;; Ok mano do futuras, essa desgraça VAI funcionar. Se n deu certo é pq tu fez errado. EU tenho CERTEZA que funfa.
					
	cmp	r9b, 's'		;; Ajeitar o fato disso estar escrevendo em memória não reservada
	je sbobf.carr			;;
	
	ret
	
	.pass:	
	mov 	[rdx], r9b
	
	inc rdx
	inc r10
	jmp sbobf.loop
	

	.end:
	mov 	rdi, rax
	call print
	ret
	
	.int:
	
	xor r8d, r8d
	mov r8d, esi
	
	push rax
	push rsi

	xor rax, rax
	xor rsi, rsi
	mov r11d, 10
	
	.itoa:
	push rdx

	mov eax, r8d
	cdq 
	idiv r11d	
	mov r8d, eax	

	cmp dl, 0
	je sbobf.intend
	
	mov al, dl
	add al, '0'
	pop rdx
	mov [rdx], al
	inc rdx	

	jmp .itoa
	
	.intend:
	pop rdx
	pop rsi
	pop rax

	jmp sbobf.loop
	
	.carr:
	mov 	r8b, byte [rsi]
	
	cmp 	r8b, 0
	je sbobf.loop
		
	mov 	[rdx], r8b
	
	inc rdx
	inc rsi
	jmp sbobf.carr
	


global strlen
;;
;; char*
;;
;; rax -> Tamanho da string
;; rdi <- buffer de chars para contar (tem que terminar em 0)
;;
strlen:
	xor 	rax, rax	
	.loop:
	cmp 	byte [rdi], 0
	je strlen.end
	
	inc rdi
	inc rax
	
	jmp strlen.loop

	.end:
	ret
	
	
	mov 	r9b, byte [r10]
