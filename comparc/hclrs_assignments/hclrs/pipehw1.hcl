########## the PC and condition codes registers #############
register fF { pc:64 = 0; }

# The values in each register were instantiated based on Figure 4.41 on page 424 of the textbook

# Fetch-Decode Pipeline Registers
register fD {
	icode:4 = NOP;
	valP:64 = 0;
	Stat:3 = STAT_AOK;
}

# Decode-Execute Pipeline Registers
register dE {
	icode_dE:4 = NOP;
	Stat_dE:3 = STAT_AOK; 
}

# Execute-Memory Pipeline Registers
register eM {
	icode_eM:4 = NOP;
	Stat_eM:3 = STAT_AOK;
}

# Memory-Writeback Pipeline Registers
register mW {
	icode_mW:4 = NOP;
	Stat_mW:3 = STAT_AOK;
}

########## Fetch #############
pc = F_pc;


f_icode = i10bytes[4..8];
#f_ifun = i10bytes[0..4];
#f_rA = i10bytes[12..16];
#f_rB = i10bytes[8..12];

f_Stat = [
	f_icode == HALT : STAT_HLT;
	f_icode > 0xb : STAT_INS;
	1 : STAT_AOK;
];

wire offset:64;
offset = [
	f_icode in { HALT } : 0;
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

# source selection


########## Execute #############

e_Stat_eM = E_Stat_dE;
e_icode_eM = E_icode_dE;


########## Memory #############
m_icode_mW = M_icode_eM;
m_Stat_mW = M_Stat_eM;



########## Writeback #############
# destination selection


########## PC update ########
f_pc = D_valP;


########## Status update ########

Stat = W_Stat_mW;



