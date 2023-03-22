## SEQLAB solution for HCL3
# Please do not consult this unless you've turned in HCL2 and HCL3.

########## the PC and condition codes registers #############
register fF { 
	pc:64 = 0; 
}

register cC {
	SF:1 = 0;
	ZF:1 = 1;
}


########## Fetch #############
pc = F_pc;

wire icode:4, ifun:4, rA:4, rB:4, valC:64;

icode = i10bytes[4..8];
ifun = i10bytes[0..4];
rA = i10bytes[12..16];
rB = i10bytes[8..12];

valC = [
	icode in { JXX, CALL } : i10bytes[8..72];
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


########## Decode #############

reg_srcA = [
	icode in {RRMOVQ, RMMOVQ, OPQ, MRMOVQ, PUSHQ, POPQ } : rA;
	1 : REG_NONE;
];

reg_srcB = [
	icode in {OPQ, RMMOVQ, MRMOVQ} : rB;
	icode in { PUSHQ, POPQ, CALL, RET } : 4;
	1 : REG_NONE;
];


########## Execute #############

wire conditionsMet:1;
conditionsMet = [
	ifun == ALWAYS : true;
	ifun == LE : C_SF || C_ZF;
	ifun == LT : C_SF;
	ifun == EQ : C_ZF;
	ifun == NE : !C_ZF;
	ifun == GE : !C_SF;
	ifun == GT : !C_SF && !C_ZF;
	1 : false;
];

wire valE:64;
valE = [
	icode == OPQ && ifun == ADDQ : reg_outputA + reg_outputB;
	icode == OPQ && ifun == SUBQ : reg_outputB - reg_outputA;
	icode == OPQ && ifun == ANDQ : reg_outputA & reg_outputB;
	icode == OPQ && ifun == XORQ : reg_outputA ^ reg_outputB;
	icode in { RMMOVQ, MRMOVQ } : valC + reg_outputB;
	icode in {PUSHQ, CALL } : reg_outputB - 0x8;
	icode in { POPQ, RET } : reg_outputB + 0x8;
	1 : 0;
];

### simplified condition codes
c_ZF = valE == 0;
c_SF = valE >= 0x8000000000000000;
stall_C = icode != OPQ;


########## Memory #############

mem_readbit = icode in { MRMOVQ, POPQ, RET };
mem_writebit = icode in { RMMOVQ, PUSHQ, CALL };
mem_addr = [
	icode in { POPQ, RET } : reg_outputB;
	1 : valE;
];
mem_input = [
	icode in { CALL } : valP;
	1 : reg_outputA;
];


########## Writeback #############

reg_dstE = [
	icode == RRMOVQ && conditionsMet : rB;
	icode in {IRMOVQ, OPQ} : rB;
	icode in { MRMOVQ } : rA;
	icode in { PUSHQ, POPQ, CALL, RET } : 4;
	1 : REG_NONE;
];


reg_inputE = [
	icode == RRMOVQ : reg_outputA;
	icode in { OPQ } : valE;
	icode in {IRMOVQ} : valC;
	icode in { MRMOVQ } : mem_output;
	icode in { PUSHQ, POPQ, CALL, RET } : valE;
	1 : 0xbadbadbadbad;
];

reg_dstM = [
	icode in { POPQ } : rA;
	1 : REG_NONE;
];

reg_inputM = [
	icode in { POPQ } : mem_output;
	1 : 0xbadbadbadbad;
];


Stat = [
	icode == HALT : STAT_HLT;
	icode > 0xb : STAT_INS;
	1 : STAT_AOK;
];



########## PC Update #############

f_pc = [
	icode == JXX && conditionsMet : valC;
	icode in { CALL } : valC;
	icode in { RET } : mem_output;
	1 : valP;
];

