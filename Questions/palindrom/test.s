	.file	"palindrom.c"
	.text
	.def	__main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
.LC0:
	.ascii "Kayak\0"
	.text
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	call	__main
	leaq	.LC0(%rip), %rcx
	call	palindrome
	movq	%rax, %rcx
	call	printf
	movl	$0, %eax
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.section .rdata,"dr"
.LC1:
	.ascii "false\12\0"
.LC2:
	.ascii "true\12\0"
	.text
	.globl	palindrome
	.def	palindrome;	.scl	2;	.type	32;	.endef
	.seh_proc	palindrome
palindrome:
	pushq	%rbp
	.seh_pushreg	%rbp
	pushq	%rbx
	.seh_pushreg	%rbx
	subq	$56, %rsp
	.seh_stackalloc	56
	leaq	128(%rsp), %rbp
	.seh_setframe	%rbp, 128
	.seh_endprologue
	movq	%rcx, -48(%rbp)
	movl	$0, -84(%rbp)
	movq	-48(%rbp), %rcx
	call	strlen
	movl	%eax, -88(%rbp)
	jmp	.L4
.L9:
	movl	-84(%rbp), %eax
	cltq
	movq	-48(%rbp), %rdx
	addq	%rdx, %rax
	movzbl	(%rax), %eax
	movsbl	%al, %eax
	movl	%eax, %ecx
	movq	__imp_isalnum(%rip), %rax
	call	*%rax
	testl	%eax, %eax
	jne	.L5
	addl	$1, -84(%rbp)
	jmp	.L4
.L5:
	movl	-88(%rbp), %eax
	cltq
	leaq	-1(%rax), %rdx
	movq	-48(%rbp), %rax
	addq	%rdx, %rax
	movzbl	(%rax), %eax
	movsbl	%al, %eax
	movl	%eax, %ecx
	movq	__imp_isalnum(%rip), %rax
	call	*%rax
	testl	%eax, %eax
	jne	.L6
	subl	$1, -88(%rbp)
	jmp	.L4
.L6:
	movl	-84(%rbp), %eax
	cltq
	movq	-48(%rbp), %rdx
	addq	%rdx, %rax
	movzbl	(%rax), %eax
	movsbl	%al, %eax
	movl	%eax, %ecx
	movq	__imp_tolower(%rip), %rax
	call	*%rax
	movl	%eax, %ebx
	movl	-88(%rbp), %eax
	cltq
	leaq	-1(%rax), %rdx
	movq	-48(%rbp), %rax
	addq	%rdx, %rax
	movzbl	(%rax), %eax
	movsbl	%al, %eax
	movl	%eax, %ecx
	movq	__imp_tolower(%rip), %rax
	call	*%rax
	cmpl	%eax, %ebx
	je	.L7
	leaq	.LC1(%rip), %rax
	jmp	.L8
.L7:
	addl	$1, -84(%rbp)
	subl	$1, -88(%rbp)
.L4:
	movl	-84(%rbp), %eax
	cmpl	-88(%rbp), %eax
	jl	.L9
	leaq	.LC2(%rip), %rax
.L8:
	addq	$56, %rsp
	popq	%rbx
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (x86_64-posix-seh-rev0, Built by MinGW-W64 project) 8.1.0"
	.def	printf;	.scl	2;	.type	32;	.endef
	.def	strlen;	.scl	2;	.type	32;	.endef
