########## the PC and condition codes registers #############
register fF { pc:64 = 0; }

# The values in each register were instantiated based on Figure 4.41 on page 424 of the textbook

# Fetch-Decode Pipeline Registers
register fD {
	icode:4 = NOP;
	valC:64 = 0;
	Stat:3 = STAT_AOK;
}

# Decode-Execute Pipeline Registers
register dE {
	icode:4 = NOP;
	valA:64 = 0;
	valC:64 = 0;
	dstE:4 = REG_NONE;
	Stat:3 = STAT_AOK; 
}

# Execute-Memory Pipeline Registers
register eM {
	icode:4 = NOP;
	valA:64 = 0;
	valC:64 = 0;
	valE:64 = 0;
	dstE:4 = REG_NONE;
	Stat:3 = STAT_AOK;
}

# Memory-Writeback Pipeline Registers
register mW {
	icode:4 = NOP;
	valE:64 = 0;
	dstE:4 = REG_NONE;
	Stat:3 = STAT_AOK;
}

########## Fetch #############
pc = F_pc;

wire rA:4, rB:4;
f_icode = i10bytes[4..8];
#f_ifun = i10bytes[0..4];
rA = i10bytes[12..16];
rB = i10bytes[8..12];

f_valC = [
	f_icode in { JXX, CALL } : i10bytes[8..72];
	1 : i10bytes[16..80];
];

f_Stat = [
	f_icode == HALT : STAT_HLT;
	f_icode > 0xb : STAT_INS;
	1 : STAT_AOK;
];

wire offset:64, valP:64;
offset = [
	f_icode in { HALT } : 0;
	f_icode > 0xb : 0;
	f_icode in { NOP } : 1;
	f_icode in { RRMOVQ, OPQ, PUSHQ, POPQ } : 2;
	f_icode in { JXX, CALL } : 9;
	1 : 10;
];

valP = F_pc + offset;

########## Decode #############

d_Stat = D_Stat;
d_icode = D_icode;
d_valC = D_valC;

# source selection

reg_srcA = [
	d_icode in {RRMOVQ} : rA;
	1 : REG_NONE;
];

reg_srcB = [
	1: REG_NONE;
];

d_valA = [
	(reg_dstE == reg_srcA) && reg_dstE != REG_NONE : reg_inputE;
	1 : reg_outputA;
];

d_dstE = [
	d_icode in {IRMOVQ, RRMOVQ} : rB;
	1 : REG_NONE;
];

########## Execute #############

e_Stat = E_Stat;
e_icode = E_icode;
e_valA = E_valA;
e_valC = E_valC;
e_dstE = E_dstE;

e_valE = [
	e_icode in { RMMOVQ, MRMOVQ } : e_valC + reg_outputB;
	1 : 0;
];


########## Memory #############
m_icode = M_icode;
m_valE = M_valE;
m_Stat = M_Stat;
m_dstE = E_dstE;



########## Writeback #############
# destination selection
reg_dstE = W_dstE;

reg_inputE = [ # unlike book, we handle the "forwarding" actions (something + 0) here
	W_icode == RRMOVQ : M_valA;
	W_icode in {IRMOVQ} : E_valC;
    1: 0xBADBADBAD;
];

########## PC update ########
f_pc = valP;

########## Status update ########

Stat = W_Stat;




