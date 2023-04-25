	.file	"dot_product_benchmarks.c"
	.text
	.globl	dot_product_C
	.type	dot_product_C, @function
dot_product_C:
.LFB5278:
	.cfi_startproc
	endbr64
	testq	%rdi, %rdi
	jle	.L4
	movl	$0, %eax
	movl	$0, %r9d
.L3:
	movslq	%eax, %r8
	movzwl	(%rsi,%r8,2), %ecx
	movzwl	(%rdx,%r8,2), %r8d
	imull	%r8d, %ecx
	addl	%ecx, %r9d
	incl	%eax
	movslq	%eax, %rcx
	cmpq	%rdi, %rcx
	jl	.L3
.L1:
	movl	%r9d, %eax
	ret
.L4:
	movl	$0, %r9d
	jmp	.L1
	.cfi_endproc
.LFE5278:
	.size	dot_product_C, .-dot_product_C
	.globl	functions
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"C (local)"
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC1:
	.string	"C (compiled with GCC7.2 -O3 -mavx2)"
	.section	.data.rel,"aw"
	.align 32
	.type	functions, @object
	.size	functions, 48
functions:
	.quad	dot_product_C
	.quad	.LC0
	.quad	dot_product_gcc7_O3
	.quad	.LC1
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
