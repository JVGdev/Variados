
section .text
global _start
_start:
    	mov	rax, 9	    ; mmap2
    	xor 	rdi, rdi    ; addr = NULL
    	mov 	rsi, 4096   ; len = 4096
    	mov 	rdx, 0o7     ; prot = PROT_READ|PROT_WRITE|PROT_EXEC
    	mov 	r10, 0x22   ; flags = MAP_PRIVATE|MAP_ANONYMOUS
    	mov 	r8, 0     ; fd = -1
    	xor 	r9, r9    ; offset = 0 (4096*0)
	syscall
	
	mov 	[frst_alloc], rax

	xor 	rdi, rdi
	mov 	rax, 60
	syscall


section .bss
	frst_alloc resq 1

