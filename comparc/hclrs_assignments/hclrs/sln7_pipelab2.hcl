# -*-sh-*- # this line enables partial syntax highlighting in emacs

######### The PC #############
register fF { predPC:64 = 0; }


########## Fetch #############
pc = F_predPC;

wire icode:4, rA:4, rB:4, valC:64;

icode = i10bytes[4..8];
rA = i10bytes[12..16];
rB = i10bytes[8..12];

valC = [
	icode in { JXX } : i10bytes[8..72];
	1 : i10bytes[16..80];
];

wire offset:64, valP:64;
offset = [
	icode in { HALT, NOP, RET } : 1;
	icode in { RRMOVQ, OPQ, PUSHQ, POPQ } : 2;
	icode in { JXX, CALL } : 9;
	1 : 10;
];
valP = F_pc + offset;
f_predPC = [
	f_icode == JXX : D_valC;
	1 : valP;
];



f_stat = [
	f_icode == HALT : STAT_HLT;
	f_icode > 0xb : STAT_INS;
	1 : STAT_AOK;
];


f_icode = icode;
f_rA = rA;
f_rB = rB;
f_valC = valC;


########## Decode #############
# figure 4.56 on page 426

register fD {
	stat:3 = STAT_BUB;
	icode:4 = NOP;
	rA:4 = REG_NONE;
	rB:4 = REG_NONE;
	valC:64 = 0;
}



reg_srcA = [ # send to register file as read port; creates reg_outputA
	D_icode in {RMMOVQ} : D_rA;
	1 : REG_NONE;
];
reg_srcB = [ # send to register file as read port; creates reg_outputB
	D_icode in {RMMOVQ, MRMOVQ} : D_rB;
	1 : REG_NONE;
];

d_dstM = [
	D_icode in { MRMOVQ } : D_rA;
	1 : REG_NONE;
];

d_valA = [
	reg_srcA == REG_NONE: 0;
	reg_srcA == m_dstM : m_valM; # forward post-memory
	reg_srcA == W_dstM : W_valM; # forward pre-writeback
	1 : reg_outputA; # returned by register file based on reg_srcA
];
d_valB = [
	reg_srcB == REG_NONE: 0;
	# forward from another phase
	reg_srcB == m_dstM : m_valM; # forward post-memory
	reg_srcB == W_dstM : W_valM; # forward pre-writeback
	1 : reg_outputB; # returned by register file based on reg_srcA
];



d_stat = D_stat;
d_icode = D_icode;
d_valC = D_valC;

########## Execute #############

register dE {
	stat:3 = STAT_BUB;
	icode:4 = NOP;
	valC:64 = 0;
	valA:64 = 0;
	valB:64 = 0;
	dstM:4 = REG_NONE;
}


e_valE = [
	E_icode in { RMMOVQ, MRMOVQ } : E_valC + E_valB;
	1 : 0;
];

e_stat =  E_stat;
e_icode = E_icode;
e_valA = E_valA;
e_dstM = E_dstM;

########## Memory #############

register eM {
	stat:3 = STAT_BUB;
	icode:4 = NOP;
	valE:64 = 0;
	valA:64 = 0;
	dstM:4 = REG_NONE;
}


mem_addr = [ # output to memory system
	M_icode in { RMMOVQ, MRMOVQ } : M_valE;
	1 : 0; # Other instructions don't need address
];
mem_readbit =  M_icode in { MRMOVQ }; # output to memory system
mem_writebit = M_icode in { RMMOVQ }; # output to memory system
mem_input = M_valA;

m_stat = M_stat;
m_valM = mem_output; # input from mem_readbit and mem_addr

m_dstM = M_dstM;
m_icode = M_icode;

########## Writeback #############
register mW {
	stat:3 = STAT_BUB;
	icode:4 = NOP;
	valM:64 = 0;
	dstM:4 = REG_NONE;
}

reg_inputM = W_valM; # output: sent to register file
reg_dstM = W_dstM; # output: sent to register file

Stat = W_stat; # output; halts execution and reports errors


################ Pipeline Register Control #########################

wire loadUse:1;

loadUse = (E_icode in {MRMOVQ}) && (E_dstM in {reg_srcA, reg_srcB}); 

### Fetch
stall_F = loadUse || f_stat != STAT_AOK;

### Decode
stall_D = loadUse;

### Execute
bubble_E = loadUse;

### Memory

### Writeback
