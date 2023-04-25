	.file	"sum_benchmarks.c"
	.text
	.globl	sum_C
	.type	sum_C, @function
sum_C:
.LFB5278:
	.cfi_startproc
	endbr64
	testq	%rdi, %rdi
	jle	.L4
	movl	$0, %eax
	movl	$0, %edx
.L3:
	movslq	%eax, %rcx
	addw	(%rsi,%rcx,2), %dx
	incl	%eax
	movslq	%eax, %rcx
	cmpq	%rdi, %rcx
	jl	.L3
.L1:
	movl	%edx, %eax
	ret
.L4:
	movl	$0, %edx
	jmp	.L1
	.cfi_endproc
.LFE5278:
	.size	sum_C, .-sum_C
	.globl	sum_with_sixteen_accumulators
	.type	sum_with_sixteen_accumulators, @function
sum_with_sixteen_accumulators:
.LFB5279:
	.cfi_startproc
	endbr64
	pushq	%r15
	.cfi_def_cfa_offset 16
	.cfi_offset 15, -16
	pushq	%r14
	.cfi_def_cfa_offset 24
	.cfi_offset 14, -24
	pushq	%r13
	.cfi_def_cfa_offset 32
	.cfi_offset 13, -32
	pushq	%r12
	.cfi_def_cfa_offset 40
	.cfi_offset 12, -40
	pushq	%rbp
	.cfi_def_cfa_offset 48
	.cfi_offset 6, -48
	pushq	%rbx
	.cfi_def_cfa_offset 56
	.cfi_offset 3, -56
	movq	%rdi, -8(%rsp)
	testq	%rdi, %rdi
	jle	.L9
	movl	$0, %eax
	movl	$0, %ecx
	movl	$0, %edi
	movl	$0, %r8d
	movl	$0, %r9d
	movl	$0, %r10d
	movl	$0, %r11d
	movl	$0, %ebx
	movl	$0, %ebp
	movl	$0, %r12d
	movl	$0, %r13d
	movl	$0, %r14d
	movl	$0, %r15d
	movw	$0, -10(%rsp)
	movw	$0, -12(%rsp)
	movw	$0, -14(%rsp)
	movw	$0, -16(%rsp)
.L8:
	movslq	%eax, %rdx
	movzwl	(%rsi,%rdx,2), %edx
	addw	%dx, -16(%rsp)
	leal	1(%rax), %edx
	movslq	%edx, %rdx
	movzwl	(%rsi,%rdx,2), %edx
	addw	%dx, -14(%rsp)
	leal	2(%rax), %edx
	movslq	%edx, %rdx
	movzwl	(%rsi,%rdx,2), %edx
	addw	%dx, -12(%rsp)
	leal	3(%rax), %edx
	movslq	%edx, %rdx
	movzwl	(%rsi,%rdx,2), %edx
	addw	%dx, -10(%rsp)
	leal	4(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %r15w
	leal	5(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %r14w
	leal	6(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %r13w
	leal	7(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %r12w
	leal	8(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %bp
	leal	9(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %bx
	leal	10(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %r11w
	leal	11(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %r10w
	leal	12(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %r9w
	leal	13(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %r8w
	leal	14(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %di
	leal	15(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %cx
	addl	$16, %eax
	movslq	%eax, %rdx
	cmpq	-8(%rsp), %rdx
	jl	.L8
.L7:
	movzwl	-12(%rsp), %eax
	addw	-10(%rsp), %ax
	addl	%r15d, %eax
	addl	%r14d, %eax
	addl	%r13d, %eax
	addl	%r12d, %eax
	addl	%ebp, %eax
	addl	%ebx, %eax
	addl	%r11d, %eax
	addl	%r10d, %eax
	addl	%r9d, %eax
	addl	%r8d, %eax
	addl	%edi, %eax
	addl	%eax, %ecx
	movzwl	-16(%rsp), %eax
	addw	-14(%rsp), %ax
	addl	%ecx, %eax
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 48
	popq	%rbp
	.cfi_def_cfa_offset 40
	popq	%r12
	.cfi_def_cfa_offset 32
	popq	%r13
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%r15
	.cfi_def_cfa_offset 8
	ret
.L9:
	.cfi_restore_state
	movl	$0, %ecx
	movl	$0, %edi
	movl	$0, %r8d
	movl	$0, %r9d
	movl	$0, %r10d
	movl	$0, %r11d
	movl	$0, %ebx
	movl	$0, %ebp
	movl	$0, %r12d
	movl	$0, %r13d
	movl	$0, %r14d
	movl	$0, %r15d
	movw	$0, -10(%rsp)
	movw	$0, -12(%rsp)
	movw	$0, -14(%rsp)
	movw	$0, -16(%rsp)
	jmp	.L7
	.cfi_endproc
.LFE5279:
	.size	sum_with_sixteen_accumulators, .-sum_with_sixteen_accumulators
	.globl	sum_AVX
	.type	sum_AVX, @function
sum_AVX:
.LFB5280:
	.cfi_startproc
	endbr64
	testq	%rdi, %rdi
	jle	.L13
	movl	$0, %eax
.L14:
	addl	$16, %eax
	movslq	%eax, %rdx
	cmpq	%rdi, %rdx
	jl	.L14
.L13:
	movl	$0, %eax
	ret
	.cfi_endproc
.LFE5280:
	.size	sum_AVX, .-sum_AVX
	.globl	sum_with_eight_accumulators
	.type	sum_with_eight_accumulators, @function
sum_with_eight_accumulators:
.LFB5281:
	.cfi_startproc
	endbr64
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	testq	%rdi, %rdi
	jle	.L19
	movl	$0, %eax
	movl	$0, %r10d
	movl	$0, %r11d
	movl	$0, %ebx
	movl	$0, %ebp
	movl	$0, %r12d
	movl	$0, %ecx
	movl	$0, %r9d
	movl	$0, %r8d
.L18:
	movslq	%eax, %rdx
	addw	(%rsi,%rdx,2), %r8w
	leal	1(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %r9w
	leal	2(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %cx
	leal	3(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %r12w
	leal	4(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %bp
	leal	5(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %bx
	leal	6(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %r11w
	leal	7(%rax), %edx
	movslq	%edx, %rdx
	addw	(%rsi,%rdx,2), %r10w
	addl	$8, %eax
	movslq	%eax, %rdx
	cmpq	%rdi, %rdx
	jl	.L18
.L17:
	leal	(%rcx,%r12), %eax
	addl	%ebp, %eax
	addl	%ebx, %eax
	addl	%r11d, %eax
	addl	%eax, %r10d
	addl	%r9d, %r8d
	leal	(%r10,%r8), %eax
	popq	%rbx
	.cfi_remember_state
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
.L19:
	.cfi_restore_state
	movl	$0, %r10d
	movl	$0, %r11d
	movl	$0, %ebx
	movl	$0, %ebp
	movl	$0, %r12d
	movl	$0, %ecx
	movl	$0, %r9d
	movl	$0, %r8d
	jmp	.L17
	.cfi_endproc
.LFE5281:
	.size	sum_with_eight_accumulators, .-sum_with_eight_accumulators
	.globl	functions
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"C (local)"
.LC1:
	.string	"C (clang6 -O)"
.LC2:
	.string	"sixteen accumulators (C)"
.LC3:
	.string	"eight accumulators (C)"
.LC4:
	.string	"lol"
	.section	.data.rel,"aw"
	.align 32
	.type	functions, @object
	.size	functions, 96
functions:
	.quad	sum_C
	.quad	.LC0
	.quad	sum_clang6_O
	.quad	.LC1
	.quad	sum_with_sixteen_accumulators
	.quad	.LC2
	.quad	sum_with_eight_accumulators
	.quad	.LC3
	.quad	sum_AVX
	.quad	.LC4
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
