########## the PC and condition codes registers #############
register fF { predPC:64 = 0; }


########## Fetch #############
wire keep_same:1, mispredicted:1;
keep_same = [
    f_icode in {HALT} : 1;
    1 : 0;
];

mispredicted = [
    !m_EccMet && m_icode == JXX: 1;
    1 : 0;
];

pc = [
    mispredicted : M_valP;
    1 : F_predPC;
];

register fD {
	icode: 4 = NOP;
	ifun: 4 = 0;
	rA: 4 = REG_NONE;
	rB: 4 = REG_NONE; 
	valC: 64 = 0;
	Stat: 3 = 0;
    valP:64 = 0;
}


f_icode = i10bytes[4..8];
f_ifun = i10bytes[0..4];
f_rA = i10bytes[12..16];
f_rB = i10bytes[8..12];


f_valC = [
	f_icode in { JXX, CALL } : i10bytes[8..72];
	1 : i10bytes[16..80];
];


wire offset:64;
offset = [
	f_icode in { HALT, NOP, RET } : 1;
	f_icode in { RRMOVQ, OPQ, PUSHQ, POPQ } : 2;
	f_icode in { JXX, CALL } : 9;
	1 : 10;
];

f_valP = [
    mispredicted : pc + offset;
    !e_EccMet && e_icode == JXX: pc;
    1 : F_predPC + offset;
];

f_predPC = [
    keep_same : pc;
    f_icode == JXX : f_valC;
    1 : f_valP;
];

stall_F = [
	loadUse: 1;
	f_Stat == STAT_AOK: 0;
	1: 0;
];

f_Stat = [ 
	f_icode == HALT : STAT_HLT;
	f_icode > 0xb : STAT_INS;
	1 : STAT_AOK;
];

########## Decode #############

bubble_D = [
    !e_EccMet && e_icode == JXX : 1;
    1 : loadUse;
];

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
    valP:64 = 0;
	Stat: 3 = 0;

}

d_icode = D_icode;
d_ifun = D_ifun;
d_rA = D_rA;
d_rB = D_rB;
d_valC = D_valC;
d_valP = D_valP;
d_Stat = D_Stat;

reg_srcA = [
	1 : d_rA;
];

d_outA = [ 
	e_EccMet && E_icode in {IRMOVQ, RRMOVQ, OPQ, MRMOVQ} && E_rB == reg_srcA: e_valE;
	m_EccMet && M_icode in {IRMOVQ, RRMOVQ, OPQ, MRMOVQ} && M_rB == reg_srcA: M_valE;
	WccMet && W_icode in {IRMOVQ, RRMOVQ, OPQ, MRMOVQ} && W_rB == reg_srcA: reg_inputE;
	M_icode == MRMOVQ && M_rA == reg_srcA: m_memOut;
	W_icode == MRMOVQ && W_rA == reg_srcA: W_memOut;
	1: reg_outputA;
];


reg_srcB = [
	1:d_rB;
];

d_outB = [
	e_EccMet && E_icode in {IRMOVQ, RRMOVQ, OPQ} && E_rB == reg_srcB: e_valE;
	m_EccMet && M_icode in {IRMOVQ, RRMOVQ, OPQ} && M_rB == reg_srcB: M_valE;
	WccMet && W_icode in {IRMOVQ, RRMOVQ, OPQ} && W_rB == reg_srcB: reg_inputE;
	M_icode == MRMOVQ && M_rA == reg_srcB: m_memOut;
	W_icode == MRMOVQ && W_rA == reg_srcB: W_memOut;
	1: reg_outputB;
];


########## Execute #############

bubble_E = [
    !e_EccMet && e_icode == JXX : 1;
    1 : loadUse;
];

register eM {

	outA: 64 = 0;
	outB: 64 = 0;
	icode: 4 = NOP;
	ifun: 4 = 0;
	rA: 4 = REG_NONE;
	rB: 4 = REG_NONE; 
	valC: 64 = 0;
	valE: 64 = 0;
    valP:64 = 0;
	Stat: 3 = 0;
    EccMet:1 = 0;

	SF:1 = 0;
    ZF:1 = 0;
}

e_icode = E_icode;
e_ifun = E_ifun;
e_rA = E_rA;
e_rB = E_rB;
e_valC = E_valC;
e_valP = E_valP;
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
	e_icode in {IRMOVQ}: E_valC;
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

e_EccMet = [
	
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
    valP:64 = 0;
	Stat: 3 = 0;
    EccMet:1 = 0;

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
m_valP = M_valP;
m_Stat = M_Stat;
m_EccMet = M_EccMet;

m_ZF = M_ZF;
m_SF = M_SF;

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
WccMet = W_EccMet;

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