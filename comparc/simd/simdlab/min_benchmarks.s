	.file	"min_benchmarks.c"
	.text
	.globl	min_C
	.type	min_C, @function
min_C:
.LFB5278:
	.cfi_startproc
	endbr64
	testq	%rdi, %rdi
	jle	.L4
	movl	$0, %eax
	movl	$32767, %edx
.L3:
	movslq	%eax, %rcx
	movzwl	(%rsi,%rcx,2), %ecx
	cmpw	%cx, %dx
	cmovg	%ecx, %edx
	incl	%eax
	movslq	%eax, %rcx
	cmpq	%rdi, %rcx
	jl	.L3
.L1:
	movl	%edx, %eax
	ret
.L4:
	movl	$32767, %edx
	jmp	.L1
	.cfi_endproc
.LFE5278:
	.size	min_C, .-min_C
	.globl	functions
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"C (local)"
	.section	.data.rel.local,"aw"
	.align 32
	.type	functions, @object
	.size	functions, 32
functions:
	.quad	min_C
	.quad	.LC0
	.quad	0
	.quad	0
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
