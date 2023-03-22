########## the PC and condition codes registers #############
register fF { pc:64 = 0; }

# The values in each register were instantiated based on Figure 4.41 on page 424 of the textbook

# Fetch-Decode Pipeline Registers
register fD {
	icode:4 = NOP;
	ifun:4 = NOP;
	valC:64 = 0;
	valP:64 = 0;
	rA:4 = REG_NONE;
	rB:4 = REG_NONE;
	Stat:3 = STAT_AOK;
}

# Decode-Execute Pipeline Registers
register dE {
	icode_dE:4 = NOP;
	#ifun_dE:4 = NOP;
	valA_dE:64 = 0;
	#valB_dE:64 = 0;
	valC_dE:64 = 0;
	dstE_dE:4 = REG_NONE;
	#dstM_dE:4 = REG_NONE;
	#srcA_dE:4 = REG_NONE;
	#srcB_dE:4 = REG_NONE;
	Stat_dE:3 = STAT_AOK; 
}

# Execute-Memory Pipeline Registers
register eM {
	icode_eM:4 = NOP;
	valA_eM:64 = 0;
	valE_eM:64 = 0;
	dstE_eM:4 = REG_NONE;
	#dstM_eM:4 = REG_NONE;
	Stat_eM:3 = STAT_AOK;
}

# Memory-Writeback Pipeline Registers
register mW {
	icode_mW:4 = NOP;
	valE_mW:64 = 0;
	#valM_mW:64 = 0;
	dstE_mW:4 = REG_NONE;
	#dstM_mW:64 = 0;
	Stat_mW:3 = STAT_AOK;
}

########## Fetch #############
pc = F_pc;


f_icode = i10bytes[4..8];
f_ifun = i10bytes[0..4];
f_rA = i10bytes[12..16];
f_rB = i10bytes[8..12];

f_valC = [
	f_icode in { JXX } : i10bytes[8..72];
	1 : i10bytes[16..80];
];

f_Stat = [
	f_icode == HALT : STAT_HLT;
	f_icode > 0xb : STAT_INS;
	1 : STAT_AOK;
];

wire offset:64;
offset = [
	f_icode in { HALT, NOP } : 0;
	f_icode > 0xb : 0;
	f_icode in { NOP, RET } : 1;
	f_icode in { RRMOVQ, OPQ, PUSHQ, POPQ } : 2;
	f_icode in { JXX, CALL } : 9;
	1 : 10;
];

f_valP = F_pc + offset;

########## Decode #############

d_Stat_dE = D_Stat;
d_icode_dE = D_icode;
d_valC_dE = D_valC;

# source selection
reg_srcA = [
	d_icode_dE in {RRMOVQ} : D_rA;
	1 : REG_NONE;
];

reg_srcB = [
	d_icode_dE in {OPQ, RMMOVQ, MRMOVQ} : D_rB;
	d_icode_dE in { PUSHQ, POPQ, CALL, RET } : 4;
	1 : REG_NONE;	
];

d_valA_dE = [
	(reg_dstE == reg_srcA) && reg_dstE != REG_NONE : reg_inputE;
	1 : reg_outputA;
];

d_dstE_dE = [
	d_icode_dE in {IRMOVQ, RRMOVQ} : D_rB;
	1 : REG_NONE;
];

########## Execute #############

e_Stat_eM = E_Stat_dE;
e_icode_eM = E_icode_dE;
e_valA_eM = E_valA_dE;
#e_valC_eM = E_valC_dE;
e_dstE_eM = E_dstE_dE;

e_valE_eM = [
	e_icode_eM in {RRMOVQ} : E_valC_dE + reg_outputB;
	1: 0;
];


########## Memory #############
m_icode_mW = M_icode_eM;
m_Stat_mW = M_Stat_eM;
m_valE_mW = M_valE_eM;
m_dstE_mW = M_dstE_eM;


########## Writeback #############
# destination selection
reg_dstE = W_dstE_mW;

reg_inputE = [ # unlike book, we handle the "forwarding" actions (something + 0) here
	W_icode_mW == RRMOVQ : M_valA_eM;
	W_icode_mW in {IRMOVQ} : E_valC_dE;
    1: 0xBADBADBAD;
];

########## PC update ########
f_pc = D_valP;


########## Status update ########

Stat = W_Stat_mW;



