# Collaborated with Dagim Tekle, Connor Wilson, and Edward.

# An example file in our custom HCL variant, with lots of comments

register pP {  
    # our own internal register. P_pc is its output, p_pc is its input.
	pc:64 = 0; # 64-bits wide; 0 is its default value.
	
	# we could add other registers to the P register bank
	# register bank should be a lower-case letter and an upper-case letter, in that order.
	
	# there are also two other signals we can optionally use:
	# "bubble_P = true" resets every register in P to its default value
	# "stall_P = true" causes P_pc not to change, ignoring p_pc's value
} 

register cC {
    SF:1 = 0;
    ZF:1 = 1;
}

# "pc" is a pre-defined input to the instruction memory and is the 
# address to fetch 10 bytes from (into pre-defined output "i10bytes").
pc = P_pc;

# we can define our own input/output "wires" of any number of 0<bits<=80
wire opcode:8, icode:4, rA : 4, rB: 4, valC: 64, ifun:4, ALU_output:64, conditionsMet:1;

# the x[i..j] means "just the bits between i and j".  x[0..1] is the 
# low-order bit, similar to what the c code "x&1" does; "x&7" is x[0..3]
opcode = i10bytes[0..8];   # first byte read from instruction memory
icode = opcode[4..8];      # top nibble of that byte
ifun = opcode[0..4];

/* we could also have done i10bytes[4..8] directly, but I wanted to
 * demonstrate more bit slicing... and all 3 kinds of comments      */
// this is the third kind of comment

# named constants can help make code readable
const TOO_BIG = 0xC; # the first unused icode in Y86-64

# some named constants are built-in: the icodes, ifuns, STAT_??? and REG_???


# Stat is a built-in output; STAT_HLT means "stop", STAT_AOK means 
# "continue".  The following uses the mux syntax described in the 
# textbook
Stat = [
	icode == HALT : STAT_HLT;
	icode >= TOO_BIG : STAT_INS;
	1             : STAT_AOK;
];

#------------Fetch--------------
rA = i10bytes[12..16];
rB = i10bytes[8..12];

valP = [
     icode == HALT : 1;
     (icode == JXX || icode == CALL) : valC - P_pc;
     icode == RET  : 1;
     (icode == IRMOVQ || icode == MRMOVQ || icode == RMMOVQ) : 10;
     icode == NOP : 1;
     (icode == PUSHQ || icode == POPQ || icode == OPQ || icode == RRMOVQ): 2;
     1: 0xBADBADBAD;
     
];


# ----------- Implement ALU -------------
ALU_output = [
    (icode == OPQ && ifun == XORQ) : reg_outputA ^ reg_outputB;
    (icode == OPQ && ifun == ADDQ) : reg_outputA + reg_outputB;
    (icode == OPQ && ifun == SUBQ) : reg_outputB - reg_outputA;
    (icode == OPQ && ifun == ANDQ) : reg_outputA & reg_outputB;
    icode == RMMOVQ : reg_outputB + valC;
    1 : 0;
];


c_SF = [
    icode == OPQ : (ALU_output >= 0x8000000000000000);
    1 : C_SF;
];

c_ZF = [
    icode == OPQ : (ALU_output == 0);
    1 : C_ZF;
];

wire valP : 64;

#--------------------Read Input--------------------

valC = [
    icode == JXX : i10bytes[8..72];
    1 : i10bytes[16..80];
];

conditionsMet = [
    ifun == LE : C_SF || C_ZF;
    ifun == LT  : C_SF && !C_ZF;
    ifun == EQ  : C_ZF;
    ifun == NE : !C_ZF;
    ifun == GE : !C_SF || C_ZF;
    ifun == GT  : !C_SF && !C_ZF;
    ifun == ALWAYS: 1;
    1 : 0;
];
reg_srcA = [
    icode == CMOVXX || (icode == RRMOVQ && ifun == ALWAYS): rA;
    icode == OPQ : rA;
    1 : 0xF;
];

reg_srcB = [
    icode == OPQ : rB;
    1 : 0xF;
];

reg_inputE = [
    icode == IRMOVQ : valC;
    icode == RRMOVQ : reg_outputA;
    icode == OPQ : ALU_output;
    1: 0xF;
];

reg_inputM = [
    1 : 0xF;
];


#---------------------Write output and update PC------------------------------
reg_dstE = [
    !conditionsMet && icode == CMOVXX : REG_NONE;
    (icode == IRMOVQ || icode == OPQ) : rB;
    (icode == RRMOVQ && conditionsMet) : rB;

    #icode == IRMOVQ : rB;
    #icode == CMOVXX || (icode == RRMOVQ && ifun == ALWAYS)  : rB;
    #icode == OPQ : rB;
    #icode == HALT : REG_NONE;
    1 : REG_NONE;
];

reg_dstM = [
    1 : 0xF;
];

mem_addr = [
    icode == RRMOVQ : reg_outputB + valC;
    1 : 0;
];

mem_input = [
    icode == RRMOVQ: reg_outputA;
    1 : 0;
];


mem_writebit = [
    icode == RMMOVQ : 1;
    1 : 0;
];

mem_readbit = [
    1 : 0;
];

# to make progress, we have to update the PC...
p_pc = P_pc + valP; # you may use math ops directly...