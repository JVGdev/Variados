
section .text
global _start
_start:
	
	mov rdx, 0o00777	;; Modos (principalmente permissões?)
	mov rsi, 0o00000102	;; FLAGS
	lea rdi, [path]		;; Carregando caminho
	mov rax, 2		;; Chamada da open
	syscall			;; Syscall
	
	cmp rax, 0		;; Checa se aberta
	jge .opened		;; Pula se aberta
	
	mov rdx, 13		;; Tamanho da mensagem de ERRO
	lea rsi, [openError]	;; Carrega mensagem no reg
	mov rdi, 1		;; Dispositivo de saída? No caso do 1 é o terminal?
	mov rax, 1		;; Chamada write
	syscall			;; Syscall
	
	mov rdi, 1		;; Manda código de erro 1, afinal o código não deu certo
	jmp .end		;; Garante que faz a exit

	
	.opened:

	mov r15, rax		;; Salva FD(file descriptor) pra var
	
	mov rdx, 64		;; tamanho do buffer
	mov rsi, buff		;; buffer que armazena bytes de digitos
	mov rdi, 1		;; FD, terminal
	mov rax, 0		;; Chamada read
	syscall			;; Syscall	
	
	mov rdx, 64		;; Tamanho da escrita
	mov rsi, buff		;; Carrega mensagem no reg
	mov rdi, r15		;; FD arquivo
	mov rax, 1		;; Chamada write
	syscall			;; Syscall
	
	mov rdi, r15	
	mov rax, 60
	syscall



	mov rdi, [fd]		;;
	mov rax, 3 		;;
	syscall			;;
	
	xor rdi, rdi
	.end:
	mov rdi, [fd]
	
	mov rax, 60
	syscall

abreEscreve:
	


section .bss
	buff: resq 64
	fd: resq 2

section .data
	path: db "teste.txt", 0
	openError: db "Deu não man", 10, 0

