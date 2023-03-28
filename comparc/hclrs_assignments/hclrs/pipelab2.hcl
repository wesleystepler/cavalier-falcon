# Collaborated with Dagim Tekle (ddt8ee)

########## the PC and condition codes registers #############
register fF { pc:64 = 0; }


########## Fetch #############
pc = F_pc;

register fD {
	icode: 4 = NOP;
	ifun: 4 = 0;
	rA: 4 = REG_NONE;
	rB: 4 = REG_NONE; 
	valC: 64 = 0;
	Stat: 3 = 0;
}


f_icode = i10bytes[4..8];
f_ifun = i10bytes[0..4];
f_rA = i10bytes[12..16];
f_rB = i10bytes[8..12];


f_valC = [
	f_icode in { JXX, CALL } : i10bytes[8..72];
	1 : i10bytes[16..80];
];


wire offset:64, valP:64;
offset = [
	f_icode in { HALT, NOP, RET } : 1;
	f_icode in { RRMOVQ, OPQ, PUSHQ, POPQ } : 2;
	f_icode in { JXX, CALL } : 9;
	1 : 10;
];

valP = F_pc + offset;
f_pc = valP;

stall_F = [
	loadUse: 1;
	f_Stat == STAT_AOK: 0;
	1: 1;
];

f_Stat = [ 
	f_icode == HALT : STAT_HLT;
	f_icode > 0xb : STAT_INS;
	1 : STAT_AOK;
];

########## Decode #############

# source selection

wire loadUse:1;
loadUse = [
	e_icode == MRMOVQ && d_rB == e_rA: 1;
	1: 0;
];
stall_D = loadUse;

register dE {
	outA: 64 = 0;
	outB: 64 = 0;
	icode: 4 = NOP;
	ifun: 4 = 0;
	rA: 4 = REG_NONE;
	rB: 4 = REG_NONE; 
	valC: 64 = 0;
	Stat: 3 = 0;

}

d_icode = D_icode;
d_ifun = D_ifun;
d_rA = D_rA;
d_rB = D_rB;
d_valC = D_valC;
d_Stat = D_Stat;

reg_srcA = [
	1 : d_rA;
];

d_outA = [ 
	EccMet && E_icode in {IRMOVQ, RRMOVQ, OPQ, MRMOVQ} && E_rB == reg_srcA: e_valE;
	MccMet && M_icode in {IRMOVQ, RRMOVQ, OPQ, MRMOVQ} && M_rB == reg_srcA: M_valE;
	WccMet && W_icode in {IRMOVQ, RRMOVQ, OPQ, MRMOVQ} && W_rB == reg_srcA: reg_inputE;
	M_icode == MRMOVQ && M_rA == reg_srcA: m_memOut;
	W_icode == MRMOVQ && W_rA == reg_srcA: W_memOut;
	1: reg_outputA;
];


reg_srcB = [
	1:d_rB;
];

d_outB = [
	EccMet && E_icode in {IRMOVQ, RRMOVQ, OPQ} && E_rB == reg_srcB: e_valE;
	MccMet && M_icode in {IRMOVQ, RRMOVQ, OPQ} && M_rB == reg_srcB: M_valE;
	WccMet && W_icode in {IRMOVQ, RRMOVQ, OPQ} && W_rB == reg_srcB: reg_inputE;
	M_icode == MRMOVQ && M_rA == reg_srcB: m_memOut;
	W_icode == MRMOVQ && W_rA == reg_srcB: W_memOut;
	1: reg_outputB;
];


########## Execute #############

bubble_E = loadUse;

register eM {

	outA: 64 = 0;
	outB: 64 = 0;
	icode: 4 = NOP;
	ifun: 4 = 0;
	rA: 4 = REG_NONE;
	rB: 4 = REG_NONE; 
	valC: 64 = 0;
	valE: 64 = 0;
	Stat: 3 = 0;

	SF:1 = 0;
    ZF:1 = 0;
}

e_icode = E_icode;
e_ifun = E_ifun;
e_rA = E_rA;
e_rB = E_rB;
e_valC = E_valC;
e_Stat = E_Stat;
e_outA = [
	1: E_outA;
];
e_outB = [
	1: E_outB;
];

e_valE = [
	e_icode == OPQ && e_ifun == ADDQ: e_outB + e_outA;
	e_icode == OPQ && e_ifun == SUBQ: e_outB - e_outA;
	e_icode == OPQ && e_ifun == ANDQ: e_outB & e_outA;
	e_icode == OPQ && e_ifun == XORQ: e_outB ^ e_outA;
	e_icode in {RRMOVQ}: e_outA;
	e_icode in {IRMOVQ}: e_valC;
	e_icode in {RMMOVQ, MRMOVQ}: e_valC + e_outB;
	1:0
];

# F D E M W
#   F D E M W

 register cC {
     SF:1 = 0;
     ZF:1 = 0;
 }


e_ZF = c_ZF;
e_SF = c_SF;

 c_ZF = [
     e_icode == OPQ : (e_valE == 0);
     1 : C_ZF;
 ];

  c_SF = [
     e_icode == OPQ : (e_valE >= 0x8000000000000000);
     1 : C_SF;
 ];

wire EccMet: 1;
EccMet = [
	
	E_ifun == ALWAYS: 1;
	E_ifun == LE: (c_SF || c_ZF);
	E_ifun == LT: (c_SF && !c_ZF);
	E_ifun == EQ: c_ZF ;
	E_ifun == NE: !c_ZF ;
	E_ifun == GE: (!c_SF || c_ZF) ;
	E_ifun == GT: (!c_SF && !c_ZF);
	1: 0;
];


########## Memory #############

register mW {
	memOut: 64 = 0;
	outA: 64 = 0;
	outB: 64 = 0;
	icode: 4 = NOP;
	ifun: 4 = 0;
	rA: 4 = REG_NONE;
	rB: 4 = REG_NONE; 
	valC: 64 = 0;
	valE: 64 = 0;
	Stat: 3 = 0;

	SF:1 = 0;
    ZF:1 = 0;
}

m_outA = M_outA;
m_outB = M_outB;
m_icode = M_icode;
m_ifun = M_ifun;
m_rA = M_rA;
m_rB = M_rB;
m_valC = M_valC;
m_valE = M_valE;
m_Stat = M_Stat;

m_ZF = M_ZF;
m_SF = M_SF;

wire MccMet: 1;
MccMet = [
	
	M_ifun == ALWAYS: 1;
	M_ifun == LE: (M_SF || M_ZF)  ;
	M_ifun == LT: (M_SF && !M_ZF);
	W_ifun == EQ: M_ZF ;
	M_ifun == NE: !M_ZF ;
	M_ifun == GE: (!M_SF || M_ZF) ;
	M_ifun == GT: (!M_SF && !M_ZF);
	1: 0;
];


mem_addr = [
	1: m_valE;
]; 

mem_readbit = [
	m_icode == MRMOVQ: 1;
	1:0;
];
m_memOut = [
	W_icode == RMMOVQ && m_rA == W_rA: W_outA;
	1:mem_output;
];

mem_writebit = [
	m_icode == RMMOVQ: 1;
	1:0;
];
mem_input =  [
	W_icode == MRMOVQ && m_rA == W_rA: W_memOut;
	1: m_outA;
];  


               

########## Writeback #############


# destination selection

wire WccMet: 1;
WccMet = [
	
	W_ifun == ALWAYS: 1;
	W_ifun == LE: (W_SF || W_ZF)  ;
	W_ifun == LT: (W_SF && !W_ZF);
	W_ifun == EQ: W_ZF ;
	W_ifun == NE: !W_ZF ;
	W_ifun == GE: (!W_SF || W_ZF) ;
	W_ifun == GT: (!W_SF && !W_ZF);
	1: 0;
];

reg_dstE = [
	W_icode in {IRMOVQ, OPQ}: W_rB;
	W_icode == RRMOVQ && WccMet: W_rB;
	W_icode == MRMOVQ: W_rA;
	1: REG_NONE;
];
reg_inputE = [
	W_icode in {IRMOVQ, RRMOVQ, OPQ}: W_valE;
	W_icode == MRMOVQ: W_memOut;
	1: 0;
];

########## Status update ########
Stat = W_Stat


