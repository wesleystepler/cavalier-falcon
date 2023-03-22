########## the PC and condition codes registers #############
register fF { pc:64 = 0; }

register dW {
	icode:4 = NOP;
	valA:64 = 0;
	valC:64 = 0;
	rB:4 = REG_NONE;
	dstE:4 = REG_NONE;
	Stat:3 = STAT_AOK;
}

########## Fetch #############
pc = F_pc;

wire ifun:4, rA:4;

d_icode = i10bytes[4..8];
ifun = i10bytes[0..4];
rA = i10bytes[12..16];
d_rB = i10bytes[8..12];

d_valC = [
	d_icode in { JXX } : i10bytes[8..72];
	1 : i10bytes[16..80];
];

wire offset:64, valP:64;
offset = [
	d_icode in { HALT } : 0;
	d_icode in { NOP, RET } : 1;
	d_icode in { RRMOVQ, OPQ, PUSHQ, POPQ } : 2;
	d_icode in { JXX, CALL } : 9;
	1 : 10;
];
valP = F_pc + offset;


########## Decode #############

# source selection
reg_srcA = [
	d_icode in {RRMOVQ} : rA;
	1 : REG_NONE;
];

d_valA = [
	(reg_dstE == reg_srcA) && reg_dstE != REG_NONE : reg_inputE;
	1 : reg_outputA;
];

d_dstE = [
	d_icode in {IRMOVQ, RRMOVQ} : d_rB;
	1 : REG_NONE;
];

d_Stat = [
	d_icode == HALT : STAT_HLT;
	d_icode > 0xb : STAT_INS;
	1 : STAT_AOK;
];

########## Execute #############



########## Memory #############




########## Writeback #############


# destination selection
reg_dstE = W_dstE;

reg_inputE = [ # unlike book, we handle the "forwarding" actions (something + 0) here
	W_icode == RRMOVQ : W_valA;
	W_icode in {IRMOVQ} : W_valC;
        1: 0xBADBADBAD;
];

########## PC update ########
f_pc = valP;


########## Status update ########

Stat = W_Stat;



