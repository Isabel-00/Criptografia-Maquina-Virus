from host import Host
from instruction import Instruction
from virusmachine import VirusMachine

#En este archivo aparecen las máquinas de cifrado y descifrado en 3 casos distintos

#Texto longitud 25 y clave longitud 2

def Vig_Codificacion_25_2(t,c):
    c1,c2 = c
    t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25 = t
    
    h1 = Host(26)
    h2 = Host()
    h3 = Host()
    h4 = Host()
    h5 = Host(t1)
    h6 = Host(t2)
    h7 = Host(t3)
    h8 = Host(t4)
    h9 = Host(t5)
    h10 = Host(t6)
    h11 = Host(t7)
    h12 = Host(t8)
    h13 = Host(t9)
    h14 = Host(t10)
    h15 = Host(t11)
    h16 = Host(t12)
    h17 = Host(t13)
    h18 = Host(t14)
    h19 = Host(t15)
    h20 = Host(t16)
    h21 = Host(t17)
    h22 = Host(t18)
    h23 = Host(t19)
    h24 = Host(t20)
    h25 = Host(t21)
    h26 = Host(t22) 
    h27 = Host(t23)
    h28 = Host(t24)
    h29 = Host(t25)
    h30 = Host()
    h31 = Host()
    h32 = Host()
    h33 = Host()
    h34 = Host()
    h35 = Host()
    h36 = Host() 
    h37 = Host()
    h38 = Host()
    h39 = Host()
    h40 = Host()
    h41 = Host()
    h42 = Host()
    h43 = Host()
    h44 = Host()
    h45 = Host()
    h46 = Host() 
    h47 = Host()
    h48 = Host()
    h49 = Host()
    h50 = Host()
    h51 = Host()
    h52 = Host() 
    h53 = Host()
    h54 = Host()
    h55 = Host(c1)
    h56 = Host(c2)    
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,
             h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,
             h21,h22,h23,h24,h25,h26,h27,h28,h29,h30,
             h31,h32,h33,h34,h35,h36,h37,h38,h39,h40,
             h41,h42,h43,h44,h45,h46,h47,h48,h49,h50,
             h51,h52,h53,h54,h55,h56,env]
    
    i1 = Instruction(h55, h3, 2)
    i2 = Instruction(h3, h55)
    i3 = Instruction(h3, h5)
    
    i4 = Instruction(h56, h3, 2)
    i5 = Instruction(h3, h56)
    i6 = Instruction(h3, h6)
    
    i7 = Instruction(h55, h3, 2)
    i8 = Instruction(h3, h55)
    i9 = Instruction(h3, h7)
    
    i10 = Instruction(h56, h3, 2)
    i11 = Instruction(h3, h56)
    i12 = Instruction(h3, h8)
    
    i13 = Instruction(h55, h3, 2)
    i14 = Instruction(h3, h55)
    i15 = Instruction(h3, h9) 
    
    i16 = Instruction(h56, h3, 2)
    i17 = Instruction(h3, h56)
    i18 = Instruction(h3, h10)
    
    i19 = Instruction(h55, h3, 2)
    i20 = Instruction(h3, h55)
    i21 = Instruction(h3, h11)
    
    i22 = Instruction(h56, h3, 2)
    i23 = Instruction(h3, h56)
    i24 = Instruction(h3, h12)
    
    i25 = Instruction(h55, h3, 2)
    i26 = Instruction(h3, h55)
    i27 = Instruction(h3, h13)
    
    i28 = Instruction(h56, h3, 2)
    i29 = Instruction(h3, h56)
    i30 = Instruction(h3, h14) 
    
    i31 = Instruction(h55, h3, 2)
    i32 = Instruction(h3, h55)
    i33 = Instruction(h3, h15)
    
    i34 = Instruction(h56, h3, 2)
    i35 = Instruction(h3, h56)
    i36 = Instruction(h3, h16)
    
    i37 = Instruction(h55, h3, 2)
    i38 = Instruction(h3, h55)
    i39 = Instruction(h3, h17)
    
    i40 = Instruction(h56, h3, 2)
    i41 = Instruction(h3, h56)
    i42 = Instruction(h3, h18)
    
    i43 = Instruction(h55, h3, 2)
    i44 = Instruction(h3, h55)
    i45 = Instruction(h3, h19) 
    
    i46 = Instruction(h56, h3, 2)
    i47 = Instruction(h3, h56)
    i48 = Instruction(h3, h20)
    
    i49 = Instruction(h55, h3, 2)
    i50 = Instruction(h3, h55)
    i51 = Instruction(h3, h21)
    
    i52 = Instruction(h56, h3, 2)
    i53 = Instruction(h3, h56)
    i54 = Instruction(h3, h22)
    
    i55 = Instruction(h55, h3, 2)
    i56 = Instruction(h3, h55)
    i57 = Instruction(h3, h23)

    i58 = Instruction(h56, h3, 2)
    i59 = Instruction(h3, h56)
    i60 = Instruction(h3, h24) 
    
    i61 = Instruction(h55, h3, 2)
    i62 = Instruction(h3, h55)
    i63 = Instruction(h3, h25)
    
    i64 = Instruction(h56, h3, 2)
    i65 = Instruction(h3, h56)
    i66 = Instruction(h3, h26)
    
    i67 = Instruction(h55, h3, 2)
    i68 = Instruction(h3, h55)
    i69 = Instruction(h3, h27)
    
    i70 = Instruction(h56, h3, 2)
    i71 = Instruction(h3, h56)
    i72 = Instruction(h3, h28)
    
    i73 = Instruction(h55, h3, 2)
    i74 = Instruction(h3, h55)
    i75 = Instruction(h3, h29) 
    
    
    #-----2 parte--------------
    
    i76 = Instruction(h1, h2)
    i77 = Instruction(h5, h3)
    i78 = Instruction(h2, h1)
    i79 = Instruction(h3, h4)
    i80 = Instruction(h3, h30)
    i81 = Instruction(h2, h1)
    
    i82 = Instruction(h1, h2)
    i83 = Instruction(h6, h3)
    i84 = Instruction(h2, h1)
    i85 = Instruction(h3, h4)
    i86 = Instruction(h3, h31)
    i87 = Instruction(h2, h1)
    
    i88 = Instruction(h1, h2)
    i89 = Instruction(h7, h3)
    i90 = Instruction(h2, h1)
    i91 = Instruction(h3, h4)
    i92 = Instruction(h3, h32)
    i93 = Instruction(h2, h1)

    i94 = Instruction(h1, h2)
    i95 = Instruction(h8, h3)
    i96 = Instruction(h2, h1)
    i97 = Instruction(h3, h4)
    i98 = Instruction(h3, h33)
    i99 = Instruction(h2, h1)
    
    i100 = Instruction(h1, h2)
    i101 = Instruction(h9, h3)
    i102 = Instruction(h2, h1)
    i103 = Instruction(h3, h4)
    i104 = Instruction(h3, h34)
    i105 = Instruction(h2, h1)
    
    i106 = Instruction(h1, h2)
    i107 = Instruction(h10, h3)
    i108 = Instruction(h2, h1)
    i109 = Instruction(h3, h4)
    i110 = Instruction(h3, h35)
    i111 = Instruction(h2, h1)
    
    i112 = Instruction(h1, h2)
    i113 = Instruction(h11, h3)
    i114 = Instruction(h2, h1)
    i115 = Instruction(h3, h4)
    i116 = Instruction(h3, h36)
    i117 = Instruction(h2, h1)
    
    i118 = Instruction(h1, h2)
    i119 = Instruction(h12, h3)
    i120 = Instruction(h2, h1)
    i121 = Instruction(h3, h4)
    i122 = Instruction(h3, h37)
    i123 = Instruction(h2, h1)

    i124 = Instruction(h1, h2)
    i125 = Instruction(h13, h3)
    i126 = Instruction(h2, h1)
    i127 = Instruction(h3, h4)
    i128 = Instruction(h3, h38)
    i129 = Instruction(h2, h1)
    
    i130 = Instruction(h1, h2)
    i131 = Instruction(h14, h3)
    i132 = Instruction(h2, h1)
    i133 = Instruction(h3, h4)
    i134 = Instruction(h3, h39)
    i135 = Instruction(h2, h1)
    
    i136 = Instruction(h1, h2)
    i137 = Instruction(h15, h3)
    i138 = Instruction(h2, h1)
    i139 = Instruction(h3, h4)
    i140 = Instruction(h3, h40)
    i141 = Instruction(h2, h1)
    
    i142 = Instruction(h1, h2)
    i143 = Instruction(h16, h3)
    i144 = Instruction(h2, h1)
    i145 = Instruction(h3, h4)
    i146 = Instruction(h3, h41)
    i147 = Instruction(h2, h1)
    
    i148 = Instruction(h1, h2)
    i149 = Instruction(h17, h3)
    i150 = Instruction(h2, h1)
    i151 = Instruction(h3, h4)
    i152 = Instruction(h3, h42)
    i153 = Instruction(h2, h1)

    i154 = Instruction(h1, h2)
    i155 = Instruction(h18, h3)
    i156 = Instruction(h2, h1)
    i157 = Instruction(h3, h4)
    i158 = Instruction(h3, h43)
    i159 = Instruction(h2, h1)
    
    i160 = Instruction(h1, h2)
    i161 = Instruction(h19, h3)
    i162 = Instruction(h2, h1)
    i163 = Instruction(h3, h4)
    i164 = Instruction(h3, h44)
    i165 = Instruction(h2, h1)
    
    i166 = Instruction(h1, h2)
    i167 = Instruction(h20, h3)
    i168 = Instruction(h2, h1)
    i169 = Instruction(h3, h4)
    i170 = Instruction(h3, h45)
    i171 = Instruction(h2, h1)
    
    i172 = Instruction(h1, h2)
    i173 = Instruction(h21, h3)
    i174 = Instruction(h2, h1)
    i175 = Instruction(h3, h4)
    i176 = Instruction(h3, h46)
    i177 = Instruction(h2, h1)
    
    i178 = Instruction(h1, h2)
    i179 = Instruction(h22, h3)
    i180 = Instruction(h2, h1)
    i181 = Instruction(h3, h4)
    i182 = Instruction(h3, h47)
    i183 = Instruction(h2, h1)

    i184 = Instruction(h1, h2)
    i185 = Instruction(h23, h3)
    i186 = Instruction(h2, h1)
    i187 = Instruction(h3, h4)
    i188 = Instruction(h3, h48)
    i189 = Instruction(h2, h1)
    
    i190 = Instruction(h1, h2)
    i191 = Instruction(h24, h3)
    i192 = Instruction(h2, h1)
    i193 = Instruction(h3, h4)
    i194 = Instruction(h3, h49)
    i195 = Instruction(h2, h1)
    
    i196 = Instruction(h1, h2)
    i197 = Instruction(h25, h3)
    i198 = Instruction(h2, h1)
    i199 = Instruction(h3, h4)
    i200 = Instruction(h3, h50)
    i201 = Instruction(h2, h1)
    
    i202 = Instruction(h1, h2)
    i203 = Instruction(h26, h3)
    i204 = Instruction(h2, h1)
    i205 = Instruction(h3, h4)
    i206 = Instruction(h3, h51)
    i207 = Instruction(h2, h1)
    
    i208 = Instruction(h1, h2)
    i209 = Instruction(h27, h3)
    i210 = Instruction(h2, h1)
    i211 = Instruction(h3, h4)
    i212 = Instruction(h3, h52)
    i213 = Instruction(h2, h1)

    i214 = Instruction(h1, h2)
    i215 = Instruction(h28, h3)
    i216 = Instruction(h2, h1)
    i217 = Instruction(h3, h4)
    i218 = Instruction(h3, h53)
    i219 = Instruction(h2, h1)
    
    i220 = Instruction(h1, h2)
    i221 = Instruction(h29, h3)
    i222 = Instruction(h2, h1)
    i223 = Instruction(h3, h4)
    i224 = Instruction(h3, h54)
    i225 = Instruction(h2, h1)
    
    i226 = Instruction(None,None)

    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,
                    i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,
                    i41,i42,i43,i44,i45,i46,i47,i48,i49,i50,i51,i52,i53,i54,i55,i56,i57,i58,i59,i60,
                    i61,i62,i63,i64,i65,i66,i67,i68,i69,i70,i71,i72,i73,i74,i75,i76,i77,i78,i79,i80,
                    i81,i82,i83,i84,i85,i86,i87,i88,i89,i90,i91,i92,i93,i94,i95,i96,i97,i98,i99,i100,
                    
                    i101,i102,i103,i104,i105,i106,i107,i108,i109,i110,i111,i112,i113,i114,i115,i116,i117,i118,i119,i120,
                    i121,i122,i123,i124,i125,i126,i127,i128,i129,i130,i131,i132,i133,i134,i135,i136,i137,i138,i139,i140,
                    i141,i142,i143,i144,i145,i146,i147,i148,i149,i150,i151,i152,i153,i154,i155,i156,i157,i158,i159,i160,
                    i161,i162,i163,i164,i165,i166,i167,i168,i169,i170,i171,i172,i173,i174,i175,i176,i177,i178,i179,i180,
                    i181,i182,i183,i184,i185,i186,i187,i188,i189,i190,i191,i192,i193,i194,i195,i196,i197,i198,i199,i200,
                    
                    i201,i202,i203,i204,i205,i206,i207,i208,i209,i210,i211,i212,i213,i214,i215,i216,i217,i218,i219,i220,
                    i221,i222,i223,i224,i225,i226]
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),(i2,i3,2),(i3,i2,1),(i2,i4,1),
                               (i4,i4,2),(i4,i5,1),(i5,i6,2),(i6,i5,1),(i5,i7,1),
                               (i7,i7,2),(i7,i8,1),(i8,i9,2),(i9,i8,1),(i8,i10,1),
                               (i10,i10,2),(i10,i11,1),(i11,i12,2),(i12,i11,1),(i11,i13,1),
                               (i13,i13,2),(i13,i14,1),(i14,i15,2),(i15,i14,1),(i14,i16,1),
                               
                               (i16,i16,2),(i16,i17,1),(i17,i18,2),(i18,i17,1),(i17,i19,1),
                               (i19,i19,2),(i19,i20,1),(i20,i21,2),(i21,i20,1),(i20,i22,1),
                               (i22,i22,2),(i22,i23,1),(i23,i24,2),(i24,i23,1),(i23,i25,1),
                               (i25,i25,2),(i25,i26,1),(i26,i27,2),(i27,i26,1),(i26,i28,1),
                               (i28,i28,2),(i28,i29,1),(i29,i30,2),(i30,i29,1),(i29,i31,1),

                               (i31,i31,2),(i31,i32,1),(i32,i33,2),(i33,i32,1),(i32,i34,1),
                               (i34,i34,2),(i34,i35,1),(i35,i36,2),(i36,i35,1),(i35,i37,1),
                               (i37,i37,2),(i37,i38,1),(i38,i39,2),(i39,i38,1),(i38,i40,1),
                               (i40,i40,2),(i40,i41,1),(i41,i42,2),(i42,i41,1),(i41,i43,1),
                               (i43,i43,2),(i43,i44,1),(i44,i45,2),(i45,i44,1),(i44,i46,1),
                               
                               (i46,i46,2),(i46,i47,1),(i47,i48,2),(i48,i47,1),(i47,i49,1),
                               (i49,i49,2),(i49,i50,1),(i50,i51,2),(i51,i50,1),(i50,i52,1),
                               (i52,i52,2),(i52,i53,1),(i53,i54,2),(i54,i53,1),(i53,i55,1),
                               (i55,i55,2),(i55,i56,1),(i56,i57,2),(i57,i56,1),(i56,i58,1),
                               (i58,i58,2),(i58,i59,1),(i59,i60,2),(i60,i59,1),(i59,i61,1),
                               
                               (i61,i61,2),(i61,i62,1),(i62,i63,2),(i63,i62,1),(i62,i64,1),
                               (i64,i64,2),(i64,i65,1),(i65,i66,2),(i66,i65,1),(i65,i67,1),
                               (i67,i67,2),(i67,i68,1),(i68,i69,2),(i69,i68,1),(i68,i70,1),
                               (i70,i70,2),(i70,i71,1),(i71,i72,2),(i72,i71,1),(i71,i73,1),
                               (i73,i73,2),(i73,i74,1),(i74,i75,2),(i75,i74,1),(i74,i76,1),
                              
                               #A continuación la segunda parte que aplica módulo a la suma obtenida
                               (i76,i77,2),(i77,i76,2),(i76,i78,1),(i78,i76,1),(i78,i79,2),
                               (i79,i78,1),(i77,i80,1),(i80,i80,2),(i80,i81,1),(i81,i81,2),(i81,i82,1),                               
                               (i82,i83,2),(i83,i82,2),(i82,i84,1),(i84,i82,1),(i84,i85,2),
                               (i85,i84,1),(i83,i86,1),(i86,i86,2),(i86,i87,1),(i87,i87,2),(i87,i88,1),                               
                               (i88,i89,2),(i89,i88,2),(i88,i90,1),(i90,i88,1),(i90,i91,2),
                               (i91,i90,1),(i89,i92,1),(i92,i92,2),(i92,i93,1),(i93,i93,2),(i93,i94,1),                                                                
                               (i94,i95,2),(i95,i94,2),(i94,i96,1),(i96,i94,1),(i96,i97,2),
                               (i97,i96,1),(i95,i98,1),(i98,i98,2),(i98,i99,1),(i99,i99,2),(i99,i100,1),                              
                               (i100,i101,2),(i101,i100,2),(i100,i102,1),(i102,i100,1),(i102,i103,2),
                               (i103,i102,1),(i101,i104,1),(i104,i104,2),(i104,i105,1),(i105,i105,2),(i105,i106,1),
                                                       
                               (i106,i107,2),(i107,i106,2),(i106,i108,1),(i108,i106,1),(i108,i109,2),
                               (i109,i108,1),(i107,i110,1),(i110,i110,2),(i110,i111,1),(i111,i111,2),(i111,i112,1),                               
                               (i112,i113,2),(i113,i112,2),(i112,i114,1),(i114,i112,1),(i114,i115,2),
                               (i115,i114,1),(i113,i116,1),(i116,i116,2),(i116,i117,1),(i117,i117,2),(i117,i118,1),                               
                               (i118,i119,2),(i119,i118,2),(i118,i120,1),(i120,i118,1),(i120,i121,2),
                               (i121,i120,1),(i119,i122,1),(i122,i122,2),(i122,i123,1),(i123,i123,2),(i123,i124,1),                                                                                      
                               (i124,i125,2),(i125,i124,2),(i124,i126,1),(i126,i124,1),(i126,i127,2),
                               (i127,i126,1),(i125,i128,1),(i128,i128,2),(i128,i129,1),(i129,i129,2),(i129,i130,1),                      
                               (i130,i131,2),(i131,i130,2),(i130,i132,1),(i132,i130,1),(i132,i133,2),
                               (i133,i132,1),(i131,i134,1),(i134,i134,2),(i134,i135,1),(i135,i135,2),(i135,i136,1),
                               
                               (i136,i137,2),(i137,i136,2),(i136,i138,1),(i138,i136,1),(i138,i139,2),
                               (i139,i138,1),(i137,i140,1),(i140,i140,2),(i140,i141,1),(i141,i141,2),(i141,i142,1),     
                               (i142,i143,2),(i143,i142,2),(i142,i144,1),(i144,i142,1),(i144,i145,2),
                               (i145,i144,1),(i143,i146,1),(i146,i146,2),(i146,i147,1),(i147,i147,2),(i147,i148,1),                               
                               (i148,i149,2),(i149,i148,2),(i148,i150,1),(i150,i148,1),(i150,i151,2),
                               (i151,i150,1),(i149,i152,1),(i152,i152,2),(i152,i153,1),(i153,i153,2),(i153,i154,1),                                                                                      
                               (i154,i155,2),(i155,i154,2),(i154,i156,1),(i156,i154,1),(i156,i157,2),
                               (i157,i156,1),(i155,i158,1),(i158,i158,2),(i158,i159,1),(i159,i159,2),(i159,i160,1),                      
                               (i160,i161,2),(i161,i160,2),(i160,i162,1),(i162,i160,1),(i162,i163,2),
                               (i163,i162,1),(i161,i164,1),(i164,i164,2),(i164,i165,1),(i165,i165,2),(i165,i166,1),
                               
                               (i166,i167,2),(i167,i166,2),(i166,i168,1),(i168,i166,1),(i168,i169,2),
                               (i169,i168,1),(i167,i170,1),(i170,i170,2),(i170,i171,1),(i171,i171,2),(i171,i172,1),                               
                               (i172,i173,2),(i173,i172,2),(i172,i174,1),(i174,i172,1),(i174,i175,2),
                               (i175,i174,1),(i173,i176,1),(i176,i176,2),(i176,i177,1),(i177,i177,2),(i177,i178,1),                               
                               (i178,i179,2),(i179,i178,2),(i178,i180,1),(i180,i178,1),(i180,i181,2),
                               (i181,i180,1),(i179,i182,1),(i182,i182,2),(i182,i183,1),(i183,i183,2),(i183,i184,1),                                                                                      
                               (i184,i185,2),(i185,i184,2),(i184,i186,1),(i186,i184,1),(i186,i187,2),
                               (i187,i186,1),(i185,i188,1),(i188,i188,2),(i188,i189,1),(i189,i189,2),(i189,i190,1),                      
                               (i190,i191,2),(i191,i190,2),(i190,i192,1),(i192,i190,1),(i192,i193,2),
                               (i193,i192,1),(i191,i194,1),(i194,i194,2),(i194,i195,1),(i195,i195,2),(i195,i196,1),
                               
                               (i196,i197,2),(i197,i196,2),(i196,i198,1),(i198,i196,1),(i198,i199,2),
                               (i199,i198,1),(i197,i200,1),(i200,i200,2),(i200,i201,1),(i201,i201,2),(i201,i202,1),                               
                               (i202,i203,2),(i203,i202,2),(i202,i204,1),(i204,i202,1),(i204,i205,2),
                               (i205,i204,1),(i203,i206,1),(i206,i206,2),(i206,i207,1),(i207,i207,2),(i207,i208,1),                               
                               (i208,i209,2),(i209,i208,2),(i208,i210,1),(i210,i208,1),(i210,i211,2),
                               (i211,i210,1),(i209,i212,1),(i212,i212,2),(i212,i213,1),(i213,i213,2),(i213,i214,1),                                                                                      
                               (i214,i215,2),(i215,i214,2),(i214,i216,1),(i216,i214,1),(i216,i217,2),
                               (i217,i216,1),(i215,i218,1),(i218,i218,2),(i218,i219,1),(i219,i219,2),(i219,i220,1),                      
                               (i220,i221,2),(i221,i220,2),(i220,i222,1),(i222,i220,1),(i222,i223,2),
                               (i223,i222,1),(i221,i224,1),(i224,i224,2),(i224,i225,1),(i225,i225,2),(i225,i226,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def Vig_Decodificacion_25_2(t,c):
    c1,c2 = c
    t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25 = t
    h1 = Host(26)
    h2 = Host()
    h3 = Host()
    h4 = Host()
    h5 = Host(t1)
    h6 = Host(t2)
    h7 = Host(t3)
    h8 = Host(t4)
    h9 = Host(t5)
    h10 = Host(t6)
    h11 = Host(t7)
    h12 = Host(t8)
    h13 = Host(t9)
    h14 = Host(t10)
    h15 = Host(t11)
    h16 = Host(t12)
    h17 = Host(t13)
    h18 = Host(t14)
    h19 = Host(t15)
    h20 = Host(t16)
    h21 = Host(t17)
    h22 = Host(t18)
    h23 = Host(t19)
    h24 = Host(t20)
    h25 = Host(t21)
    h26 = Host(t22) 
    h27 = Host(t23)
    h28 = Host(t24)
    h29 = Host(t25)
    h30 = Host()
    h31 = Host()
    h32 = Host()
    h33 = Host()
    h34 = Host()
    h35 = Host()
    h36 = Host() 
    h37 = Host()
    h38 = Host()
    h39 = Host()
    h40 = Host()
    h41 = Host()
    h42 = Host()
    h43 = Host()
    h44 = Host()
    h45 = Host()
    h46 = Host() 
    h47 = Host()
    h48 = Host()
    h49 = Host()
    h50 = Host()
    h51 = Host()
    h52 = Host() 
    h53 = Host()
    h54 = Host()
    h55 = Host(c1)
    h56 = Host(c2)    
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,
             h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,
             h21,h22,h23,h24,h25,h26,h27,h28,h29,h30,
             h31,h32,h33,h34,h35,h36,h37,h38,h39,h40,
             h41,h42,h43,h44,h45,h46,h47,h48,h49,h50,
             h51,h52,h53,h54,h55,h56,env]
    
    i1 = Instruction(h1, h2, 2)
    i2 = Instruction(h2, h5)
    i3 = Instruction(h2, h1)
    
    i4 = Instruction(h1, h2, 2)
    i5 = Instruction(h2, h6)
    i6 = Instruction(h2, h1)
    
    i7 = Instruction(h1, h2, 2)
    i8 = Instruction(h2, h7)
    i9 = Instruction(h2, h1)
    
    i10 = Instruction(h1, h2, 2)
    i11 = Instruction(h2, h8)
    i12 = Instruction(h2, h1)
    
    i13 = Instruction(h1, h2, 2)
    i14 = Instruction(h2, h9)
    i15 = Instruction(h2, h1) 
    
    i16 = Instruction(h1, h2, 2)
    i17 = Instruction(h2, h10)
    i18 = Instruction(h2, h1)
    
    i19 = Instruction(h1, h2, 2)
    i20 = Instruction(h2, h11)
    i21 = Instruction(h2, h1)
    
    i22 = Instruction(h1, h2, 2)
    i23 = Instruction(h2, h12)
    i24 = Instruction(h2, h1)
    
    i25 = Instruction(h1, h2, 2)
    i26 = Instruction(h2, h13)
    i27 = Instruction(h2, h1)
    
    i28 = Instruction(h1, h2, 2)
    i29 = Instruction(h2, h14)
    i30 = Instruction(h2, h1) 
    
    i31 = Instruction(h1, h2, 2)
    i32 = Instruction(h2, h15)
    i33 = Instruction(h2, h1)
    
    i34 = Instruction(h1, h2, 2)
    i35 = Instruction(h2, h16)
    i36 = Instruction(h2, h1)
    
    i37 = Instruction(h1, h2, 2)
    i38 = Instruction(h2, h17)
    i39 = Instruction(h2, h1)
    
    i40 = Instruction(h1, h2, 2)
    i41 = Instruction(h2, h18)
    i42 = Instruction(h2, h1)
    
    i43 = Instruction(h1, h2, 2)
    i44 = Instruction(h2, h19)
    i45 = Instruction(h2, h1) 
    
    i46 = Instruction(h1, h2, 2)
    i47 = Instruction(h2, h20)
    i48 = Instruction(h2, h1)
    
    i49 = Instruction(h1, h2, 2)
    i50 = Instruction(h2, h21)
    i51 = Instruction(h2, h1)
    
    i52 = Instruction(h1, h2, 2)
    i53 = Instruction(h2, h22)
    i54 = Instruction(h2, h1)
    
    i55 = Instruction(h1, h2, 2)
    i56 = Instruction(h2, h23)
    i57 = Instruction(h2, h1)
    
    i58 = Instruction(h1, h2, 2)
    i59 = Instruction(h2, h24)
    i60 = Instruction(h2, h1) 
    
    i61 = Instruction(h1, h2, 2)
    i62 = Instruction(h2, h25)
    i63 = Instruction(h2, h1)
    
    i64 = Instruction(h1, h2, 2)
    i65 = Instruction(h2, h26)
    i66 = Instruction(h2, h1)
    
    i67 = Instruction(h1, h2, 2)
    i68 = Instruction(h2, h27)
    i69 = Instruction(h2, h1)
    
    i70 = Instruction(h1, h2, 2)
    i71 = Instruction(h2, h28)
    i72 = Instruction(h2, h1)
    
    i73 = Instruction(h1, h2, 2)
    i74 = Instruction(h2, h29)
    i75 = Instruction(h2, h1) 
    
    #----------- 2 parte---------------
    
    i76 = Instruction(h55, h3, 2)
    i77 = Instruction(h3, h4)
    i78 = Instruction(h3, h55)
    i79 = Instruction(h5, h4)
    
    i80 = Instruction(h56, h3, 2)
    i81 = Instruction(h3, h4)
    i82 = Instruction(h3, h56)
    i83 = Instruction(h6, h4)

    i84 = Instruction(h55, h3, 2)
    i85 = Instruction(h3, h4)
    i86 = Instruction(h3, h55)
    i87 = Instruction(h7, h4)

    i88 = Instruction(h56, h3, 2)
    i89 = Instruction(h3, h4)
    i90 = Instruction(h3, h56)
    i91 = Instruction(h8, h4)
    
    i92 = Instruction(h55, h3, 2)
    i93 = Instruction(h3, h4)
    i94 = Instruction(h3, h55)
    i95 = Instruction(h9, h4)
 
    i96 = Instruction(h56, h3, 2)
    i97 = Instruction(h3, h4)
    i98 = Instruction(h3, h56)
    i99 = Instruction(h10, h4)
    
    i100 = Instruction(h55, h3, 2)
    i101 = Instruction(h3, h4)
    i102 = Instruction(h3, h55)
    i103 = Instruction(h11, h4)

    i104 = Instruction(h56, h3, 2)
    i105 = Instruction(h3, h4)
    i106 = Instruction(h3, h56)
    i107 = Instruction(h12, h4)

    i108 = Instruction(h55, h3, 2)
    i109 = Instruction(h3, h4)
    i110 = Instruction(h3, h55)
    i111 = Instruction(h13, h4)

    i112 = Instruction(h56, h3, 2)
    i113 = Instruction(h3, h4)
    i114 = Instruction(h3, h56)
    i115 = Instruction(h14, h4)
    
    i116 = Instruction(h55, h3, 2)
    i117 = Instruction(h3, h4)
    i118 = Instruction(h3, h55)
    i119 = Instruction(h15, h4)
    
    i120 = Instruction(h56, h3, 2)
    i121 = Instruction(h3, h4)
    i122 = Instruction(h3, h56)
    i123 = Instruction(h16, h4)

    i124 = Instruction(h55, h3, 2)
    i125 = Instruction(h3, h4)
    i126 = Instruction(h3, h55)
    i127 = Instruction(h17, h4)

    i128 = Instruction(h56, h3, 2)
    i129 = Instruction(h3, h4)
    i130 = Instruction(h3, h56)
    i131 = Instruction(h18, h4)
    
    i132 = Instruction(h55, h3, 2)
    i133 = Instruction(h3, h4)
    i134 = Instruction(h3, h55)
    i135 = Instruction(h19, h4)
 
    i136 = Instruction(h56, h3, 2)
    i137 = Instruction(h3, h4)
    i138 = Instruction(h3, h56)
    i139 = Instruction(h20, h4)
    
    i140 = Instruction(h55, h3, 2)
    i141 = Instruction(h3, h4)
    i142 = Instruction(h3, h55)
    i143 = Instruction(h21, h4)

    i144 = Instruction(h56, h3, 2)
    i145 = Instruction(h3, h4)
    i146 = Instruction(h3, h56)
    i147 = Instruction(h22, h4)

    i148 = Instruction(h55, h3, 2)
    i149 = Instruction(h3, h4)
    i150 = Instruction(h3, h55)
    i151 = Instruction(h23, h4)

    i152 = Instruction(h56, h3, 2)
    i153 = Instruction(h3, h4)
    i154 = Instruction(h3, h56)
    i155 = Instruction(h24, h4)    

    i156 = Instruction(h55, h3, 2)
    i157 = Instruction(h3, h4)
    i158 = Instruction(h3, h55)
    i159 = Instruction(h25, h4)
    
    i160 = Instruction(h56, h3, 2)
    i161 = Instruction(h3, h4)
    i162 = Instruction(h3, h56)
    i163 = Instruction(h26, h4)

    i164 = Instruction(h55, h3, 2)
    i165 = Instruction(h3, h4)
    i166 = Instruction(h3, h55)
    i167 = Instruction(h27, h4)

    i168 = Instruction(h56, h3, 2)
    i169 = Instruction(h3, h4)
    i170 = Instruction(h3, h56)
    i171 = Instruction(h28, h4)
    
    i172 = Instruction(h55, h3, 2)
    i173 = Instruction(h3, h4)
    i174 = Instruction(h3, h55)
    i175 = Instruction(h29, h4)
 
   #--------------3 parte------------------ 
    
    i176 = Instruction(h1, h2)
    i177 = Instruction(h5, h3)
    i178 = Instruction(h2, h1)
    i179 = Instruction(h3, h4)
    i180 = Instruction(h3, h30)
    i181 = Instruction(h2, h1)
    
    i182 = Instruction(h1, h2)
    i183 = Instruction(h6, h3)
    i184 = Instruction(h2, h1)
    i185 = Instruction(h3, h4)
    i186 = Instruction(h3, h31)
    i187 = Instruction(h2, h1)
    
    i188 = Instruction(h1, h2)
    i189 = Instruction(h7, h3)
    i190 = Instruction(h2, h1)
    i191 = Instruction(h3, h4)
    i192 = Instruction(h3, h32)
    i193 = Instruction(h2, h1)

    i194 = Instruction(h1, h2)
    i195 = Instruction(h8, h3)
    i196 = Instruction(h2, h1)
    i197 = Instruction(h3, h4)
    i198 = Instruction(h3, h33)
    i199 = Instruction(h2, h1)
    
    i200 = Instruction(h1, h2)
    i201 = Instruction(h9, h3)
    i202 = Instruction(h2, h1)
    i203 = Instruction(h3, h4)
    i204 = Instruction(h3, h34)
    i205 = Instruction(h2, h1)
    
    i206 = Instruction(h1, h2)
    i207 = Instruction(h10, h3)
    i208 = Instruction(h2, h1)
    i209 = Instruction(h3, h4)
    i210 = Instruction(h3, h35)
    i211 = Instruction(h2, h1)
    
    i212 = Instruction(h1, h2)
    i213 = Instruction(h11, h3)
    i214 = Instruction(h2, h1)
    i215 = Instruction(h3, h4)
    i216 = Instruction(h3, h36)
    i217 = Instruction(h2, h1)
    
    i218 = Instruction(h1, h2)
    i219 = Instruction(h12, h3)
    i220 = Instruction(h2, h1)
    i221 = Instruction(h3, h4)
    i222 = Instruction(h3, h37)
    i223 = Instruction(h2, h1)

    i224 = Instruction(h1, h2)
    i225 = Instruction(h13, h3)
    i226 = Instruction(h2, h1)
    i227 = Instruction(h3, h4)
    i228 = Instruction(h3, h38)
    i229 = Instruction(h2, h1)
    
    i230 = Instruction(h1, h2)
    i231 = Instruction(h14, h3)
    i232 = Instruction(h2, h1)
    i233 = Instruction(h3, h4)
    i234 = Instruction(h3, h39)
    i235 = Instruction(h2, h1)
    
    i236 = Instruction(h1, h2)
    i237 = Instruction(h15, h3)
    i238 = Instruction(h2, h1)
    i239 = Instruction(h3, h4)
    i240 = Instruction(h3, h40)
    i241 = Instruction(h2, h1)
    
    i242 = Instruction(h1, h2)
    i243 = Instruction(h16, h3)
    i244 = Instruction(h2, h1)
    i245 = Instruction(h3, h4)
    i246 = Instruction(h3, h41)
    i247 = Instruction(h2, h1)
    
    i248 = Instruction(h1, h2)
    i249 = Instruction(h17, h3)
    i250 = Instruction(h2, h1)
    i251 = Instruction(h3, h4)
    i252 = Instruction(h3, h42)
    i253 = Instruction(h2, h1)

    i254 = Instruction(h1, h2)
    i255 = Instruction(h18, h3)
    i256 = Instruction(h2, h1)
    i257 = Instruction(h3, h4)
    i258 = Instruction(h3, h43)
    i259 = Instruction(h2, h1)
    
    i260 = Instruction(h1, h2)
    i261 = Instruction(h19, h3)
    i262 = Instruction(h2, h1)
    i263 = Instruction(h3, h4)
    i264 = Instruction(h3, h44)
    i265 = Instruction(h2, h1)
    
    i266 = Instruction(h1, h2)
    i267 = Instruction(h20, h3)
    i268 = Instruction(h2, h1)
    i269 = Instruction(h3, h4)
    i270 = Instruction(h3, h45)
    i271 = Instruction(h2, h1)
    
    i272 = Instruction(h1, h2)
    i273 = Instruction(h21, h3)
    i274 = Instruction(h2, h1)
    i275 = Instruction(h3, h4)
    i276 = Instruction(h3, h46)
    i277 = Instruction(h2, h1)
    
    i278 = Instruction(h1, h2)
    i279 = Instruction(h22, h3)
    i280 = Instruction(h2, h1)
    i281 = Instruction(h3, h4)
    i282 = Instruction(h3, h47)
    i283 = Instruction(h2, h1)

    i284 = Instruction(h1, h2)
    i285 = Instruction(h23, h3)
    i286 = Instruction(h2, h1)
    i287 = Instruction(h3, h4)
    i288 = Instruction(h3, h48)
    i289 = Instruction(h2, h1)
    
    i290 = Instruction(h1, h2)
    i291 = Instruction(h24, h3)
    i292 = Instruction(h2, h1)
    i293 = Instruction(h3, h4)
    i294 = Instruction(h3, h49)
    i295 = Instruction(h2, h1)
    
    i296 = Instruction(h1, h2)
    i297 = Instruction(h25, h3)
    i298 = Instruction(h2, h1)
    i299 = Instruction(h3, h4)
    i300 = Instruction(h3, h50)
    i301 = Instruction(h2, h1)
    
    i302 = Instruction(h1, h2)
    i303 = Instruction(h26, h3)
    i304 = Instruction(h2, h1)
    i305 = Instruction(h3, h4)
    i306 = Instruction(h3, h51)
    i307 = Instruction(h2, h1)
    
    i308 = Instruction(h1, h2)
    i309 = Instruction(h27, h3)
    i310 = Instruction(h2, h1)
    i311 = Instruction(h3, h4)
    i312 = Instruction(h3, h52)
    i313 = Instruction(h2, h1)

    i314 = Instruction(h1, h2)
    i315 = Instruction(h28, h3)
    i316 = Instruction(h2, h1)
    i317 = Instruction(h3, h4)
    i318 = Instruction(h3, h53)
    i319 = Instruction(h2, h1)
    
    i320 = Instruction(h1, h2)
    i321 = Instruction(h29, h3)
    i322 = Instruction(h2, h1)
    i323 = Instruction(h3, h4)
    i324 = Instruction(h3, h54)
    i325 = Instruction(h2, h1)
    
    i326 = Instruction(None,None)

     
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,
                    i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,
                    i41,i42,i43,i44,i45,i46,i47,i48,i49,i50,i51,i52,i53,i54,i55,i56,i57,i58,i59,i60,
                    i61,i62,i63,i64,i65,i66,i67,i68,i69,i70,i71,i72,i73,i74,i75,i76,i77,i78,i79,i80,
                    i81,i82,i83,i84,i85,i86,i87,i88,i89,i90,i91,i92,i93,i94,i95,i96,i97,i98,i99,i100,
                    
                    i101,i102,i103,i104,i105,i106,i107,i108,i109,i110,i111,i112,i113,i114,i115,i116,i117,i118,i119,i120,
                    i121,i122,i123,i124,i125,i126,i127,i128,i129,i130,i131,i132,i133,i134,i135,i136,i137,i138,i139,i140,
                    i141,i142,i143,i144,i145,i146,i147,i148,i149,i150,i151,i152,i153,i154,i155,i156,i157,i158,i159,i160,
                    i161,i162,i163,i164,i165,i166,i167,i168,i169,i170,i171,i172,i173,i174,i175,i176,i177,i178,i179,i180,
                    i181,i182,i183,i184,i185,i186,i187,i188,i189,i190,i191,i192,i193,i194,i195,i196,i197,i198,i199,i200,
                    
                    i201,i202,i203,i204,i205,i206,i207,i208,i209,i210,i211,i212,i213,i214,i215,i216,i217,i218,i219,i220,
                    i221,i222,i223,i224,i225,i226,i227,i228,i229,i230,i231,i232,i233,i234,i235,i236,i237,i238,i239,i240,
                    i241,i242,i243,i244,i245,i246,i247,i248,i249,i250,i251,i252,i253,i254,i255,i256,i257,i258,i259,i260,
                    i261,i262,i263,i264,i265,i266,i267,i268,i269,i270,i271,i272,i273,i274,i275,i276,i277,i278,i279,i280,
                    i281,i282,i283,i284,i285,i286,i287,i288,i289,i290,i291,i292,i293,i294,i295,i296,i297,i298,i299,i300,
                    
                    i301,i302,i303,i304,i305,i306,i307,i308,i309,i310,i311,i312,i313,i314,i315,i316,i317,i318,i319,i320,
                    i321,i322,i323,i324,i325,i326]
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),(i2,i3,2),(i3,i2,1),(i2,i4,1),
                               (i4,i4,2),(i4,i5,1),(i5,i6,2),(i6,i5,1),(i5,i7,1),
                               (i7,i7,2),(i7,i8,1),(i8,i9,2),(i9,i8,1),(i8,i10,1),
                               (i10,i10,2),(i10,i11,1),(i11,i12,2),(i12,i11,1),(i11,i13,1),
                               (i13,i13,2),(i13,i14,1),(i14,i15,2),(i15,i14,1),(i14,i16,1),
                               
                               (i16,i16,2),(i16,i17,1),(i17,i18,2),(i18,i17,1),(i17,i19,1),
                               (i19,i19,2),(i19,i20,1),(i20,i21,2),(i21,i20,1),(i20,i22,1),
                               (i22,i22,2),(i22,i23,1),(i23,i24,2),(i24,i23,1),(i23,i25,1),
                               (i25,i25,2),(i25,i26,1),(i26,i27,2),(i27,i26,1),(i26,i28,1),
                               (i28,i28,2),(i28,i29,1),(i29,i30,2),(i30,i29,1),(i29,i31,1),
                               
                               (i31,i31,2),(i31,i32,1),(i32,i33,2),(i33,i32,1),(i32,i34,1),
                               (i34,i34,2),(i34,i35,1),(i35,i36,2),(i36,i35,1),(i35,i37,1),
                               (i37,i37,2),(i37,i38,1),(i38,i39,2),(i39,i38,1),(i38,i40,1),
                               (i40,i40,2),(i40,i41,1),(i41,i42,2),(i42,i41,1),(i41,i43,1),
                               (i43,i43,2),(i43,i44,1),(i44,i45,2),(i45,i44,1),(i44,i46,1),
                               
                               (i46,i46,2),(i46,i47,1),(i47,i48,2),(i48,i47,1),(i47,i49,1),
                               (i49,i49,2),(i49,i50,1),(i50,i51,2),(i51,i50,1),(i50,i52,1),
                               (i52,i52,2),(i52,i53,1),(i53,i54,2),(i54,i53,1),(i53,i55,1),
                               (i55,i55,2),(i55,i56,1),(i56,i57,2),(i57,i56,1),(i56,i58,1),
                               (i58,i58,2),(i58,i59,1),(i59,i60,2),(i60,i59,1),(i59,i61,1),
                               
                               (i61,i61,2),(i61,i62,1),(i62,i63,2),(i63,i62,1),(i62,i64,1),
                               (i64,i64,2),(i64,i65,1),(i65,i66,2),(i66,i65,1),(i65,i67,1),
                               (i67,i67,2),(i67,i68,1),(i68,i69,2),(i69,i68,1),(i68,i70,1),
                               (i70,i70,2),(i70,i71,1),(i71,i72,2),(i72,i71,1),(i71,i73,1),
                               (i73,i73,2),(i73,i74,1),(i74,i75,2),(i75,i74,1),(i74,i76,1),
                              
                               #La segunda parte que resta la clave
                              (i76,i76,2),(i76,i77,1),(i77,i78,2),(i78,i79,1),(i79,i77,1),(i77,i80,1),
                              (i80,i80,2),(i80,i81,1),(i81,i82,2),(i82,i83,1),(i83,i81,1),(i81,i84,1),
                              (i84,i84,2),(i84,i85,1),(i85,i86,2),(i86,i87,1),(i87,i85,1),(i85,i88,1),
                              (i88,i88,2),(i88,i89,1),(i89,i90,2),(i90,i91,1),(i91,i89,1),(i89,i92,1),
                              (i92,i92,2),(i92,i93,1),(i93,i94,2),(i94,i95,1),(i95,i93,1),(i93,i96,1),
                               
                              (i96,i96,2),(i96,i97,1),(i97,i98,2),(i98,i99,1),(i99,i97,1),(i97,i100,1),
                              (i100,i100,2),(i100,i101,1),(i101,i102,2),(i102,i103,1),(i103,i101,1),(i101,i104,1),
                              (i104,i104,2),(i104,i105,1),(i105,i106,2),(i106,i107,1),(i107,i105,1),(i105,i108,1),
                              (i108,i108,2),(i108,i109,1),(i109,i110,2),(i110,i111,1),(i111,i109,1),(i109,i112,1),
                              (i112,i112,2),(i112,i113,1),(i113,i114,2),(i114,i115,1),(i115,i113,1),(i113,i116,1),
                               
                              (i116,i116,2),(i116,i117,1),(i117,i118,2),(i118,i119,1),(i119,i117,1),(i117,i120,1),
                              (i120,i120,2),(i120,i121,1),(i121,i122,2),(i122,i123,1),(i123,i121,1),(i121,i124,1),
                              (i124,i124,2),(i124,i125,1),(i125,i126,2),(i126,i127,1),(i127,i125,1),(i125,i128,1),
                              (i128,i128,2),(i128,i129,1),(i129,i130,2),(i130,i131,1),(i131,i129,1),(i129,i132,1),
                              (i132,i132,2),(i132,i133,1),(i133,i134,2),(i134,i135,1),(i135,i133,1),(i133,i136,1),
                               
                              (i136,i136,2),(i136,i137,1),(i137,i138,2),(i138,i139,1),(i139,i137,1),(i137,i140,1),
                              (i140,i140,2),(i140,i141,1),(i141,i142,2),(i142,i143,1),(i143,i141,1),(i141,i144,1),
                              (i144,i144,2),(i144,i145,1),(i145,i146,2),(i146,i147,1),(i147,i145,1),(i145,i148,1),
                              (i148,i148,2),(i148,i149,1),(i149,i150,2),(i150,i151,1),(i151,i149,1),(i149,i152,1),
                              (i152,i152,2),(i152,i153,1),(i153,i154,2),(i154,i155,1),(i155,i153,1),(i153,i156,1),
                            
                              (i156,i156,2),(i156,i157,1),(i157,i158,2),(i158,i159,1),(i159,i157,1),(i157,i160,1),
                              (i160,i160,2),(i160,i161,1),(i161,i162,2),(i162,i163,1),(i163,i161,1),(i161,i164,1),
                              (i164,i164,2),(i164,i165,1),(i165,i166,2),(i166,i167,1),(i167,i165,1),(i165,i168,1),
                              (i168,i168,2),(i168,i169,1),(i169,i170,2),(i170,i171,1),(i171,i169,1),(i169,i172,1),
                              (i172,i172,2),(i172,i173,1),(i173,i174,2),(i174,i175,1),(i175,i173,1),(i173,i176,1),
                               
                            #A continuación la tecera parte que aplica módulo a la resta
                           (i176,i177,2),(i177,i176,2),(i176,i178,1),(i178,i176,1),(i178,i179,2),
                           (i179,i178,1),(i177,i180,1),(i180,i180,2),(i180,i181,1),(i181,i181,2),(i181,i182,1),
                           (i182,i183,2),(i183,i182,2),(i182,i184,1),(i184,i182,1),(i184,i185,2),
                           (i185,i184,1),(i183,i186,1),(i186,i186,2),(i186,i187,1),(i187,i187,2),(i187,i188,1),
                           (i188,i189,2),(i189,i188,2),(i188,i190,1),(i190,i188,1),(i190,i191,2),
                           (i191,i190,1),(i189,i192,1),(i192,i192,2),(i192,i193,1),(i193,i193,2),(i193,i194,1), 
                           (i194,i195,2),(i195,i194,2),(i194,i196,1),(i196,i194,1),(i196,i197,2),
                           (i197,i196,1),(i195,i198,1),(i198,i198,2),(i198,i199,1),(i199,i199,2),(i199,i200,1),
                           (i200,i201,2),(i201,i200,2),(i200,i202,1),(i202,i200,1),(i202,i203,2),
                           (i203,i202,1),(i201,i204,1),(i204,i204,2),(i204,i205,1),(i205,i205,2),(i205,i206,1),
                               
                           (i206,i207,2),(i207,i206,2),(i206,i208,1),(i208,i206,1),(i208,i209,2),
                           (i209,i208,1),(i207,i210,1),(i210,i210,2),(i210,i211,1),(i211,i211,2),(i211,i212,1),
                           (i212,i213,2),(i213,i212,2),(i212,i214,1),(i214,i212,1),(i214,i215,2),
                           (i215,i214,1),(i213,i216,1),(i216,i216,2),(i216,i217,1),(i217,i217,2),(i217,i218,1),
                           (i218,i219,2),(i219,i218,2),(i218,i220,1),(i220,i218,1),(i220,i221,2),
                           (i221,i220,1),(i219,i222,1),(i222,i222,2),(i222,i223,1),(i223,i223,2),(i223,i224,1), 
                           (i224,i225,2),(i225,i224,2),(i224,i226,1),(i226,i224,1),(i226,i227,2),
                           (i227,i226,1),(i225,i228,1),(i228,i228,2),(i228,i229,1),(i229,i229,2),(i229,i230,1),
                           (i230,i231,2),(i231,i230,2),(i230,i232,1),(i232,i230,1),(i232,i233,2),
                           (i233,i232,1),(i231,i234,1),(i234,i234,2),(i234,i235,1),(i235,i235,2),(i235,i236,1),
                               
                           (i236,i237,2),(i237,i236,2),(i236,i238,1),(i238,i236,1),(i238,i239,2),
                           (i239,i238,1),(i237,i240,1),(i240,i240,2),(i240,i241,1),(i241,i241,2),(i241,i242,1),
                           (i242,i243,2),(i243,i242,2),(i242,i244,1),(i244,i242,1),(i244,i245,2),
                           (i245,i244,1),(i243,i246,1),(i246,i246,2),(i246,i247,1),(i247,i247,2),(i247,i248,1),
                           (i248,i249,2),(i249,i248,2),(i248,i250,1),(i250,i248,1),(i250,i251,2),
                           (i251,i250,1),(i249,i252,1),(i252,i252,2),(i252,i253,1),(i253,i253,2),(i253,i254,1), 
                           (i254,i255,2),(i255,i254,2),(i254,i256,1),(i256,i254,1),(i256,i257,2),
                           (i257,i256,1),(i255,i258,1),(i258,i258,2),(i258,i259,1),(i259,i259,2),(i259,i260,1),
                           (i260,i261,2),(i261,i260,2),(i260,i262,1),(i262,i260,1),(i262,i263,2),
                           (i263,i262,1),(i261,i264,1),(i264,i264,2),(i264,i265,1),(i265,i265,2),(i265,i266,1),
                               
                           (i266,i267,2),(i267,i266,2),(i266,i268,1),(i268,i266,1),(i268,i269,2),
                           (i269,i268,1),(i267,i270,1),(i270,i270,2),(i270,i271,1),(i271,i271,2),(i271,i272,1),
                           (i272,i273,2),(i273,i272,2),(i272,i274,1),(i274,i272,1),(i274,i275,2),
                           (i275,i274,1),(i273,i276,1),(i276,i276,2),(i276,i277,1),(i277,i277,2),(i277,i278,1),
                           (i278,i279,2),(i279,i278,2),(i278,i280,1),(i280,i278,1),(i280,i281,2),
                           (i281,i280,1),(i279,i282,1),(i282,i282,2),(i282,i283,1),(i283,i283,2),(i283,i284,1), 
                           (i284,i285,2),(i285,i284,2),(i284,i286,1),(i286,i284,1),(i286,i287,2),
                           (i287,i286,1),(i285,i288,1),(i288,i288,2),(i288,i289,1),(i289,i289,2),(i289,i290,1),
                           (i290,i291,2),(i291,i290,2),(i290,i292,1),(i292,i290,1),(i292,i293,2),
                           (i293,i292,1),(i291,i294,1),(i294,i294,2),(i294,i295,1),(i295,i295,2),(i295,i296,1),
                               
                           (i296,i297,2),(i297,i296,2),(i296,i298,1),(i298,i296,1),(i298,i299,2),
                           (i299,i298,1),(i297,i300,1),(i300,i300,2),(i300,i301,1),(i301,i301,2),(i301,i302,1),
                           (i302,i303,2),(i303,i302,2),(i302,i304,1),(i304,i302,1),(i304,i305,2),
                           (i305,i304,1),(i303,i306,1),(i306,i306,2),(i306,i307,1),(i307,i307,2),(i307,i308,1),
                           (i308,i309,2),(i309,i308,2),(i308,i310,1),(i310,i308,1),(i310,i311,2),
                           (i311,i310,1),(i309,i312,1),(i312,i312,2),(i312,i313,1),(i313,i313,2),(i313,i314,1), 
                           (i314,i315,2),(i315,i314,2),(i314,i316,1),(i316,i314,1),(i316,i317,2),
                           (i317,i316,1),(i315,i318,1),(i318,i318,2),(i318,i319,1),(i319,i319,2),(i319,i320,1),
                           (i320,i321,2),(i321,i320,2),(i320,i322,1),(i322,i320,1),(i322,i323,2),
                           (i323,i322,1),(i321,i324,1),(i324,i324,2),(i324,i325,1),(i325,i325,2),(i325,i326,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm


#Texto 25, clave 3

def Vig_Codificacion_25_3(t,c):
    c1,c2,c3 = c
    t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25 = t
    
    h1 = Host(26)
    h2 = Host()
    h3 = Host()
    h4 = Host()
    h5 = Host(t1)
    h6 = Host(t2)
    h7 = Host(t3)
    h8 = Host(t4)
    h9 = Host(t5)
    h10 = Host(t6)
    h11 = Host(t7)
    h12 = Host(t8)
    h13 = Host(t9)
    h14 = Host(t10)
    h15 = Host(t11)
    h16 = Host(t12)
    h17 = Host(t13)
    h18 = Host(t14)
    h19 = Host(t15)
    h20 = Host(t16)
    h21 = Host(t17)
    h22 = Host(t18)
    h23 = Host(t19)
    h24 = Host(t20)
    h25 = Host(t21)
    h26 = Host(t22) 
    h27 = Host(t23)
    h28 = Host(t24)
    h29 = Host(t25)
    h30 = Host()
    h31 = Host()
    h32 = Host()
    h33 = Host()
    h34 = Host()
    h35 = Host()
    h36 = Host() 
    h37 = Host()
    h38 = Host()
    h39 = Host()
    h40 = Host()
    h41 = Host()
    h42 = Host()
    h43 = Host()
    h44 = Host()
    h45 = Host()
    h46 = Host() 
    h47 = Host()
    h48 = Host()
    h49 = Host()
    h50 = Host()
    h51 = Host()
    h52 = Host() 
    h53 = Host()
    h54 = Host()
    h55 = Host(c1)
    h56 = Host(c2) 
    h57 = Host(c3)
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,
             h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,
             h21,h22,h23,h24,h25,h26,h27,h28,h29,h30,
             h31,h32,h33,h34,h35,h36,h37,h38,h39,h40,
             h41,h42,h43,h44,h45,h46,h47,h48,h49,h50,
             h51,h52,h53,h54,h55,h56,h57,env]
    
    i1 = Instruction(h55, h3, 2)
    i2 = Instruction(h3, h55)
    i3 = Instruction(h3, h5)
    
    i4 = Instruction(h56, h3, 2)
    i5 = Instruction(h3, h56)
    i6 = Instruction(h3, h6)
    
    i7 = Instruction(h57, h3, 2)
    i8 = Instruction(h3, h57)
    i9 = Instruction(h3, h7)
    
    i10 = Instruction(h55, h3, 2)
    i11 = Instruction(h3, h55)
    i12 = Instruction(h3, h8)
    
    i13 = Instruction(h56, h3, 2)
    i14 = Instruction(h3, h56)
    i15 = Instruction(h3, h9) 
    
    i16 = Instruction(h57, h3, 2)
    i17 = Instruction(h3, h57)
    i18 = Instruction(h3, h10)
    
    i19 = Instruction(h55, h3, 2)
    i20 = Instruction(h3, h55)
    i21 = Instruction(h3, h11)
    
    i22 = Instruction(h56, h3, 2)
    i23 = Instruction(h3, h56)
    i24 = Instruction(h3, h12)
    
    i25 = Instruction(h57, h3, 2)
    i26 = Instruction(h3, h57)
    i27 = Instruction(h3, h13)
    
    i28 = Instruction(h55, h3, 2)
    i29 = Instruction(h3, h55)
    i30 = Instruction(h3, h14) 
    
    i31 = Instruction(h56, h3, 2)
    i32 = Instruction(h3, h56)
    i33 = Instruction(h3, h15)
    
    i34 = Instruction(h57, h3, 2)
    i35 = Instruction(h3, h57)
    i36 = Instruction(h3, h16)
    
    i37 = Instruction(h55, h3, 2)
    i38 = Instruction(h3, h55)
    i39 = Instruction(h3, h17)
    
    i40 = Instruction(h56, h3, 2)
    i41 = Instruction(h3, h56)
    i42 = Instruction(h3, h18)
    
    i43 = Instruction(h57, h3, 2)
    i44 = Instruction(h3, h57)
    i45 = Instruction(h3, h19) 
    
    i46 = Instruction(h55, h3, 2)
    i47 = Instruction(h3, h55)
    i48 = Instruction(h3, h20)
    
    i49 = Instruction(h56, h3, 2)
    i50 = Instruction(h3, h56)
    i51 = Instruction(h3, h21)
    
    i52 = Instruction(h57, h3, 2)
    i53 = Instruction(h3, h57)
    i54 = Instruction(h3, h22)
    
    i55 = Instruction(h55, h3, 2)
    i56 = Instruction(h3, h55)
    i57 = Instruction(h3, h23)

    i58 = Instruction(h56, h3, 2)
    i59 = Instruction(h3, h56)
    i60 = Instruction(h3, h24) 
    
    i61 = Instruction(h57, h3, 2)
    i62 = Instruction(h3, h57)
    i63 = Instruction(h3, h25)
    
    i64 = Instruction(h55, h3, 2)
    i65 = Instruction(h3, h55)
    i66 = Instruction(h3, h26)
    
    i67 = Instruction(h56, h3, 2)
    i68 = Instruction(h3, h56)
    i69 = Instruction(h3, h27)
    
    i70 = Instruction(h57, h3, 2)
    i71 = Instruction(h3, h57)
    i72 = Instruction(h3, h28)
    
    i73 = Instruction(h55, h3, 2)
    i74 = Instruction(h3, h55)
    i75 = Instruction(h3, h29) 
    
    
    #-----2 parte--------------
    
    i76 = Instruction(h1, h2)
    i77 = Instruction(h5, h3)
    i78 = Instruction(h2, h1)
    i79 = Instruction(h3, h4)
    i80 = Instruction(h3, h30)
    i81 = Instruction(h2, h1)
    
    i82 = Instruction(h1, h2)
    i83 = Instruction(h6, h3)
    i84 = Instruction(h2, h1)
    i85 = Instruction(h3, h4)
    i86 = Instruction(h3, h31)
    i87 = Instruction(h2, h1)
    
    i88 = Instruction(h1, h2)
    i89 = Instruction(h7, h3)
    i90 = Instruction(h2, h1)
    i91 = Instruction(h3, h4)
    i92 = Instruction(h3, h32)
    i93 = Instruction(h2, h1)

    i94 = Instruction(h1, h2)
    i95 = Instruction(h8, h3)
    i96 = Instruction(h2, h1)
    i97 = Instruction(h3, h4)
    i98 = Instruction(h3, h33)
    i99 = Instruction(h2, h1)
    
    i100 = Instruction(h1, h2)
    i101 = Instruction(h9, h3)
    i102 = Instruction(h2, h1)
    i103 = Instruction(h3, h4)
    i104 = Instruction(h3, h34)
    i105 = Instruction(h2, h1)
    
    i106 = Instruction(h1, h2)
    i107 = Instruction(h10, h3)
    i108 = Instruction(h2, h1)
    i109 = Instruction(h3, h4)
    i110 = Instruction(h3, h35)
    i111 = Instruction(h2, h1)
    
    i112 = Instruction(h1, h2)
    i113 = Instruction(h11, h3)
    i114 = Instruction(h2, h1)
    i115 = Instruction(h3, h4)
    i116 = Instruction(h3, h36)
    i117 = Instruction(h2, h1)
    
    i118 = Instruction(h1, h2)
    i119 = Instruction(h12, h3)
    i120 = Instruction(h2, h1)
    i121 = Instruction(h3, h4)
    i122 = Instruction(h3, h37)
    i123 = Instruction(h2, h1)

    i124 = Instruction(h1, h2)
    i125 = Instruction(h13, h3)
    i126 = Instruction(h2, h1)
    i127 = Instruction(h3, h4)
    i128 = Instruction(h3, h38)
    i129 = Instruction(h2, h1)
    
    i130 = Instruction(h1, h2)
    i131 = Instruction(h14, h3)
    i132 = Instruction(h2, h1)
    i133 = Instruction(h3, h4)
    i134 = Instruction(h3, h39)
    i135 = Instruction(h2, h1)
    
    i136 = Instruction(h1, h2)
    i137 = Instruction(h15, h3)
    i138 = Instruction(h2, h1)
    i139 = Instruction(h3, h4)
    i140 = Instruction(h3, h40)
    i141 = Instruction(h2, h1)
    
    i142 = Instruction(h1, h2)
    i143 = Instruction(h16, h3)
    i144 = Instruction(h2, h1)
    i145 = Instruction(h3, h4)
    i146 = Instruction(h3, h41)
    i147 = Instruction(h2, h1)
    
    i148 = Instruction(h1, h2)
    i149 = Instruction(h17, h3)
    i150 = Instruction(h2, h1)
    i151 = Instruction(h3, h4)
    i152 = Instruction(h3, h42)
    i153 = Instruction(h2, h1)

    i154 = Instruction(h1, h2)
    i155 = Instruction(h18, h3)
    i156 = Instruction(h2, h1)
    i157 = Instruction(h3, h4)
    i158 = Instruction(h3, h43)
    i159 = Instruction(h2, h1)
    
    i160 = Instruction(h1, h2)
    i161 = Instruction(h19, h3)
    i162 = Instruction(h2, h1)
    i163 = Instruction(h3, h4)
    i164 = Instruction(h3, h44)
    i165 = Instruction(h2, h1)
    
    i166 = Instruction(h1, h2)
    i167 = Instruction(h20, h3)
    i168 = Instruction(h2, h1)
    i169 = Instruction(h3, h4)
    i170 = Instruction(h3, h45)
    i171 = Instruction(h2, h1)
    
    i172 = Instruction(h1, h2)
    i173 = Instruction(h21, h3)
    i174 = Instruction(h2, h1)
    i175 = Instruction(h3, h4)
    i176 = Instruction(h3, h46)
    i177 = Instruction(h2, h1)
    
    i178 = Instruction(h1, h2)
    i179 = Instruction(h22, h3)
    i180 = Instruction(h2, h1)
    i181 = Instruction(h3, h4)
    i182 = Instruction(h3, h47)
    i183 = Instruction(h2, h1)

    i184 = Instruction(h1, h2)
    i185 = Instruction(h23, h3)
    i186 = Instruction(h2, h1)
    i187 = Instruction(h3, h4)
    i188 = Instruction(h3, h48)
    i189 = Instruction(h2, h1)
    
    i190 = Instruction(h1, h2)
    i191 = Instruction(h24, h3)
    i192 = Instruction(h2, h1)
    i193 = Instruction(h3, h4)
    i194 = Instruction(h3, h49)
    i195 = Instruction(h2, h1)
    
    i196 = Instruction(h1, h2)
    i197 = Instruction(h25, h3)
    i198 = Instruction(h2, h1)
    i199 = Instruction(h3, h4)
    i200 = Instruction(h3, h50)
    i201 = Instruction(h2, h1)
    
    i202 = Instruction(h1, h2)
    i203 = Instruction(h26, h3)
    i204 = Instruction(h2, h1)
    i205 = Instruction(h3, h4)
    i206 = Instruction(h3, h51)
    i207 = Instruction(h2, h1)
    
    i208 = Instruction(h1, h2)
    i209 = Instruction(h27, h3)
    i210 = Instruction(h2, h1)
    i211 = Instruction(h3, h4)
    i212 = Instruction(h3, h52)
    i213 = Instruction(h2, h1)

    i214 = Instruction(h1, h2)
    i215 = Instruction(h28, h3)
    i216 = Instruction(h2, h1)
    i217 = Instruction(h3, h4)
    i218 = Instruction(h3, h53)
    i219 = Instruction(h2, h1)
    
    i220 = Instruction(h1, h2)
    i221 = Instruction(h29, h3)
    i222 = Instruction(h2, h1)
    i223 = Instruction(h3, h4)
    i224 = Instruction(h3, h54)
    i225 = Instruction(h2, h1)
    
    i226 = Instruction(None,None)

    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,
                    i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,
                    i41,i42,i43,i44,i45,i46,i47,i48,i49,i50,i51,i52,i53,i54,i55,i56,i57,i58,i59,i60,
                    i61,i62,i63,i64,i65,i66,i67,i68,i69,i70,i71,i72,i73,i74,i75,i76,i77,i78,i79,i80,
                    i81,i82,i83,i84,i85,i86,i87,i88,i89,i90,i91,i92,i93,i94,i95,i96,i97,i98,i99,i100,
                    
                    i101,i102,i103,i104,i105,i106,i107,i108,i109,i110,i111,i112,i113,i114,i115,i116,i117,i118,i119,i120,
                    i121,i122,i123,i124,i125,i126,i127,i128,i129,i130,i131,i132,i133,i134,i135,i136,i137,i138,i139,i140,
                    i141,i142,i143,i144,i145,i146,i147,i148,i149,i150,i151,i152,i153,i154,i155,i156,i157,i158,i159,i160,
                    i161,i162,i163,i164,i165,i166,i167,i168,i169,i170,i171,i172,i173,i174,i175,i176,i177,i178,i179,i180,
                    i181,i182,i183,i184,i185,i186,i187,i188,i189,i190,i191,i192,i193,i194,i195,i196,i197,i198,i199,i200,
                    
                    i201,i202,i203,i204,i205,i206,i207,i208,i209,i210,i211,i212,i213,i214,i215,i216,i217,i218,i219,i220,
                    i221,i222,i223,i224,i225,i226]
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),(i2,i3,2),(i3,i2,1),(i2,i4,1),
                               (i4,i4,2),(i4,i5,1),(i5,i6,2),(i6,i5,1),(i5,i7,1),
                               (i7,i7,2),(i7,i8,1),(i8,i9,2),(i9,i8,1),(i8,i10,1),
                               (i10,i10,2),(i10,i11,1),(i11,i12,2),(i12,i11,1),(i11,i13,1),
                               (i13,i13,2),(i13,i14,1),(i14,i15,2),(i15,i14,1),(i14,i16,1),
                               
                               (i16,i16,2),(i16,i17,1),(i17,i18,2),(i18,i17,1),(i17,i19,1),
                               (i19,i19,2),(i19,i20,1),(i20,i21,2),(i21,i20,1),(i20,i22,1),
                               (i22,i22,2),(i22,i23,1),(i23,i24,2),(i24,i23,1),(i23,i25,1),
                               (i25,i25,2),(i25,i26,1),(i26,i27,2),(i27,i26,1),(i26,i28,1),
                               (i28,i28,2),(i28,i29,1),(i29,i30,2),(i30,i29,1),(i29,i31,1),

                               (i31,i31,2),(i31,i32,1),(i32,i33,2),(i33,i32,1),(i32,i34,1),
                               (i34,i34,2),(i34,i35,1),(i35,i36,2),(i36,i35,1),(i35,i37,1),
                               (i37,i37,2),(i37,i38,1),(i38,i39,2),(i39,i38,1),(i38,i40,1),
                               (i40,i40,2),(i40,i41,1),(i41,i42,2),(i42,i41,1),(i41,i43,1),
                               (i43,i43,2),(i43,i44,1),(i44,i45,2),(i45,i44,1),(i44,i46,1),
                               
                               (i46,i46,2),(i46,i47,1),(i47,i48,2),(i48,i47,1),(i47,i49,1),
                               (i49,i49,2),(i49,i50,1),(i50,i51,2),(i51,i50,1),(i50,i52,1),
                               (i52,i52,2),(i52,i53,1),(i53,i54,2),(i54,i53,1),(i53,i55,1),
                               (i55,i55,2),(i55,i56,1),(i56,i57,2),(i57,i56,1),(i56,i58,1),
                               (i58,i58,2),(i58,i59,1),(i59,i60,2),(i60,i59,1),(i59,i61,1),
                               
                               (i61,i61,2),(i61,i62,1),(i62,i63,2),(i63,i62,1),(i62,i64,1),
                               (i64,i64,2),(i64,i65,1),(i65,i66,2),(i66,i65,1),(i65,i67,1),
                               (i67,i67,2),(i67,i68,1),(i68,i69,2),(i69,i68,1),(i68,i70,1),
                               (i70,i70,2),(i70,i71,1),(i71,i72,2),(i72,i71,1),(i71,i73,1),
                               (i73,i73,2),(i73,i74,1),(i74,i75,2),(i75,i74,1),(i74,i76,1),
                              
                               #A continuación la segunda parte que aplica módulo a la suma obtenida
                               (i76,i77,2),(i77,i76,2),(i76,i78,1),(i78,i76,1),(i78,i79,2),
                               (i79,i78,1),(i77,i80,1),(i80,i80,2),(i80,i81,1),(i81,i81,2),(i81,i82,1),                               
                               (i82,i83,2),(i83,i82,2),(i82,i84,1),(i84,i82,1),(i84,i85,2),
                               (i85,i84,1),(i83,i86,1),(i86,i86,2),(i86,i87,1),(i87,i87,2),(i87,i88,1),                               
                               (i88,i89,2),(i89,i88,2),(i88,i90,1),(i90,i88,1),(i90,i91,2),
                               (i91,i90,1),(i89,i92,1),(i92,i92,2),(i92,i93,1),(i93,i93,2),(i93,i94,1),                                                                
                               (i94,i95,2),(i95,i94,2),(i94,i96,1),(i96,i94,1),(i96,i97,2),
                               (i97,i96,1),(i95,i98,1),(i98,i98,2),(i98,i99,1),(i99,i99,2),(i99,i100,1),                              
                               (i100,i101,2),(i101,i100,2),(i100,i102,1),(i102,i100,1),(i102,i103,2),
                               (i103,i102,1),(i101,i104,1),(i104,i104,2),(i104,i105,1),(i105,i105,2),(i105,i106,1),
                                                       
                               (i106,i107,2),(i107,i106,2),(i106,i108,1),(i108,i106,1),(i108,i109,2),
                               (i109,i108,1),(i107,i110,1),(i110,i110,2),(i110,i111,1),(i111,i111,2),(i111,i112,1),                               
                               (i112,i113,2),(i113,i112,2),(i112,i114,1),(i114,i112,1),(i114,i115,2),
                               (i115,i114,1),(i113,i116,1),(i116,i116,2),(i116,i117,1),(i117,i117,2),(i117,i118,1),                               
                               (i118,i119,2),(i119,i118,2),(i118,i120,1),(i120,i118,1),(i120,i121,2),
                               (i121,i120,1),(i119,i122,1),(i122,i122,2),(i122,i123,1),(i123,i123,2),(i123,i124,1),                                                                                      
                               (i124,i125,2),(i125,i124,2),(i124,i126,1),(i126,i124,1),(i126,i127,2),
                               (i127,i126,1),(i125,i128,1),(i128,i128,2),(i128,i129,1),(i129,i129,2),(i129,i130,1),                      
                               (i130,i131,2),(i131,i130,2),(i130,i132,1),(i132,i130,1),(i132,i133,2),
                               (i133,i132,1),(i131,i134,1),(i134,i134,2),(i134,i135,1),(i135,i135,2),(i135,i136,1),
                               
                               (i136,i137,2),(i137,i136,2),(i136,i138,1),(i138,i136,1),(i138,i139,2),
                               (i139,i138,1),(i137,i140,1),(i140,i140,2),(i140,i141,1),(i141,i141,2),(i141,i142,1),     
                               (i142,i143,2),(i143,i142,2),(i142,i144,1),(i144,i142,1),(i144,i145,2),
                               (i145,i144,1),(i143,i146,1),(i146,i146,2),(i146,i147,1),(i147,i147,2),(i147,i148,1),                               
                               (i148,i149,2),(i149,i148,2),(i148,i150,1),(i150,i148,1),(i150,i151,2),
                               (i151,i150,1),(i149,i152,1),(i152,i152,2),(i152,i153,1),(i153,i153,2),(i153,i154,1),                                                                                      
                               (i154,i155,2),(i155,i154,2),(i154,i156,1),(i156,i154,1),(i156,i157,2),
                               (i157,i156,1),(i155,i158,1),(i158,i158,2),(i158,i159,1),(i159,i159,2),(i159,i160,1),                      
                               (i160,i161,2),(i161,i160,2),(i160,i162,1),(i162,i160,1),(i162,i163,2),
                               (i163,i162,1),(i161,i164,1),(i164,i164,2),(i164,i165,1),(i165,i165,2),(i165,i166,1),
                               
                               (i166,i167,2),(i167,i166,2),(i166,i168,1),(i168,i166,1),(i168,i169,2),
                               (i169,i168,1),(i167,i170,1),(i170,i170,2),(i170,i171,1),(i171,i171,2),(i171,i172,1),                               
                               (i172,i173,2),(i173,i172,2),(i172,i174,1),(i174,i172,1),(i174,i175,2),
                               (i175,i174,1),(i173,i176,1),(i176,i176,2),(i176,i177,1),(i177,i177,2),(i177,i178,1),                               
                               (i178,i179,2),(i179,i178,2),(i178,i180,1),(i180,i178,1),(i180,i181,2),
                               (i181,i180,1),(i179,i182,1),(i182,i182,2),(i182,i183,1),(i183,i183,2),(i183,i184,1),                                                                                      
                               (i184,i185,2),(i185,i184,2),(i184,i186,1),(i186,i184,1),(i186,i187,2),
                               (i187,i186,1),(i185,i188,1),(i188,i188,2),(i188,i189,1),(i189,i189,2),(i189,i190,1),                      
                               (i190,i191,2),(i191,i190,2),(i190,i192,1),(i192,i190,1),(i192,i193,2),
                               (i193,i192,1),(i191,i194,1),(i194,i194,2),(i194,i195,1),(i195,i195,2),(i195,i196,1),
                               
                               (i196,i197,2),(i197,i196,2),(i196,i198,1),(i198,i196,1),(i198,i199,2),
                               (i199,i198,1),(i197,i200,1),(i200,i200,2),(i200,i201,1),(i201,i201,2),(i201,i202,1),                               
                               (i202,i203,2),(i203,i202,2),(i202,i204,1),(i204,i202,1),(i204,i205,2),
                               (i205,i204,1),(i203,i206,1),(i206,i206,2),(i206,i207,1),(i207,i207,2),(i207,i208,1),                               
                               (i208,i209,2),(i209,i208,2),(i208,i210,1),(i210,i208,1),(i210,i211,2),
                               (i211,i210,1),(i209,i212,1),(i212,i212,2),(i212,i213,1),(i213,i213,2),(i213,i214,1),                                                                                      
                               (i214,i215,2),(i215,i214,2),(i214,i216,1),(i216,i214,1),(i216,i217,2),
                               (i217,i216,1),(i215,i218,1),(i218,i218,2),(i218,i219,1),(i219,i219,2),(i219,i220,1),                      
                               (i220,i221,2),(i221,i220,2),(i220,i222,1),(i222,i220,1),(i222,i223,2),
                               (i223,i222,1),(i221,i224,1),(i224,i224,2),(i224,i225,1),(i225,i225,2),(i225,i226,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm


def Vig_Decodificacion_25_3(t,c):
    c1,c2,c3 = c
    t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25 = t
    h1 = Host(26)
    h2 = Host()
    h3 = Host()
    h4 = Host()
    h5 = Host(t1)
    h6 = Host(t2)
    h7 = Host(t3)
    h8 = Host(t4)
    h9 = Host(t5)
    h10 = Host(t6)
    h11 = Host(t7)
    h12 = Host(t8)
    h13 = Host(t9)
    h14 = Host(t10)
    h15 = Host(t11)
    h16 = Host(t12)
    h17 = Host(t13)
    h18 = Host(t14)
    h19 = Host(t15)
    h20 = Host(t16)
    h21 = Host(t17)
    h22 = Host(t18)
    h23 = Host(t19)
    h24 = Host(t20)
    h25 = Host(t21)
    h26 = Host(t22) 
    h27 = Host(t23)
    h28 = Host(t24)
    h29 = Host(t25)
    h30 = Host()
    h31 = Host()
    h32 = Host()
    h33 = Host()
    h34 = Host()
    h35 = Host()
    h36 = Host() 
    h37 = Host()
    h38 = Host()
    h39 = Host()
    h40 = Host()
    h41 = Host()
    h42 = Host()
    h43 = Host()
    h44 = Host()
    h45 = Host()
    h46 = Host() 
    h47 = Host()
    h48 = Host()
    h49 = Host()
    h50 = Host()
    h51 = Host()
    h52 = Host() 
    h53 = Host()
    h54 = Host()
    h55 = Host(c1)
    h56 = Host(c2)  
    h57 = Host(c3)
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,
             h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,
             h21,h22,h23,h24,h25,h26,h27,h28,h29,h30,
             h31,h32,h33,h34,h35,h36,h37,h38,h39,h40,
             h41,h42,h43,h44,h45,h46,h47,h48,h49,h50,
             h51,h52,h53,h54,h55,h56,h57,env]
    
    i1 = Instruction(h1, h2, 2)
    i2 = Instruction(h2, h5)
    i3 = Instruction(h2, h1)
    
    i4 = Instruction(h1, h2, 2)
    i5 = Instruction(h2, h6)
    i6 = Instruction(h2, h1)
    
    i7 = Instruction(h1, h2, 2)
    i8 = Instruction(h2, h7)
    i9 = Instruction(h2, h1)
    
    i10 = Instruction(h1, h2, 2)
    i11 = Instruction(h2, h8)
    i12 = Instruction(h2, h1)
    
    i13 = Instruction(h1, h2, 2)
    i14 = Instruction(h2, h9)
    i15 = Instruction(h2, h1) 
    
    i16 = Instruction(h1, h2, 2)
    i17 = Instruction(h2, h10)
    i18 = Instruction(h2, h1)
    
    i19 = Instruction(h1, h2, 2)
    i20 = Instruction(h2, h11)
    i21 = Instruction(h2, h1)
    
    i22 = Instruction(h1, h2, 2)
    i23 = Instruction(h2, h12)
    i24 = Instruction(h2, h1)
    
    i25 = Instruction(h1, h2, 2)
    i26 = Instruction(h2, h13)
    i27 = Instruction(h2, h1)
    
    i28 = Instruction(h1, h2, 2)
    i29 = Instruction(h2, h14)
    i30 = Instruction(h2, h1) 
    
    i31 = Instruction(h1, h2, 2)
    i32 = Instruction(h2, h15)
    i33 = Instruction(h2, h1)
    
    i34 = Instruction(h1, h2, 2)
    i35 = Instruction(h2, h16)
    i36 = Instruction(h2, h1)
    
    i37 = Instruction(h1, h2, 2)
    i38 = Instruction(h2, h17)
    i39 = Instruction(h2, h1)
    
    i40 = Instruction(h1, h2, 2)
    i41 = Instruction(h2, h18)
    i42 = Instruction(h2, h1)
    
    i43 = Instruction(h1, h2, 2)
    i44 = Instruction(h2, h19)
    i45 = Instruction(h2, h1) 
    
    i46 = Instruction(h1, h2, 2)
    i47 = Instruction(h2, h20)
    i48 = Instruction(h2, h1)
    
    i49 = Instruction(h1, h2, 2)
    i50 = Instruction(h2, h21)
    i51 = Instruction(h2, h1)
    
    i52 = Instruction(h1, h2, 2)
    i53 = Instruction(h2, h22)
    i54 = Instruction(h2, h1)
    
    i55 = Instruction(h1, h2, 2)
    i56 = Instruction(h2, h23)
    i57 = Instruction(h2, h1)
    
    i58 = Instruction(h1, h2, 2)
    i59 = Instruction(h2, h24)
    i60 = Instruction(h2, h1) 
    
    i61 = Instruction(h1, h2, 2)
    i62 = Instruction(h2, h25)
    i63 = Instruction(h2, h1)
    
    i64 = Instruction(h1, h2, 2)
    i65 = Instruction(h2, h26)
    i66 = Instruction(h2, h1)
    
    i67 = Instruction(h1, h2, 2)
    i68 = Instruction(h2, h27)
    i69 = Instruction(h2, h1)
    
    i70 = Instruction(h1, h2, 2)
    i71 = Instruction(h2, h28)
    i72 = Instruction(h2, h1)
    
    i73 = Instruction(h1, h2, 2)
    i74 = Instruction(h2, h29)
    i75 = Instruction(h2, h1) 
    
    #----------- 2 parte---------------
    
    i76 = Instruction(h55, h3, 2)
    i77 = Instruction(h3, h4)
    i78 = Instruction(h3, h55)
    i79 = Instruction(h5, h4)
    
    i80 = Instruction(h56, h3, 2)
    i81 = Instruction(h3, h4)
    i82 = Instruction(h3, h56)
    i83 = Instruction(h6, h4)

    i84 = Instruction(h57, h3, 2)
    i85 = Instruction(h3, h4)
    i86 = Instruction(h3, h57)
    i87 = Instruction(h7, h4)

    i88 = Instruction(h55, h3, 2)
    i89 = Instruction(h3, h4)
    i90 = Instruction(h3, h55)
    i91 = Instruction(h8, h4)
    
    i92 = Instruction(h56, h3, 2)
    i93 = Instruction(h3, h4)
    i94 = Instruction(h3, h56)
    i95 = Instruction(h9, h4)
 
    i96 = Instruction(h57, h3, 2)
    i97 = Instruction(h3, h4)
    i98 = Instruction(h3, h57)
    i99 = Instruction(h10, h4)
    
    i100 = Instruction(h55, h3, 2)
    i101 = Instruction(h3, h4)
    i102 = Instruction(h3, h55)
    i103 = Instruction(h11, h4)

    i104 = Instruction(h56, h3, 2)
    i105 = Instruction(h3, h4)
    i106 = Instruction(h3, h56)
    i107 = Instruction(h12, h4)

    i108 = Instruction(h57, h3, 2)
    i109 = Instruction(h3, h4)
    i110 = Instruction(h3, h57)
    i111 = Instruction(h13, h4)

    i112 = Instruction(h55, h3, 2)
    i113 = Instruction(h3, h4)
    i114 = Instruction(h3, h55)
    i115 = Instruction(h14, h4)
    
    i116 = Instruction(h56, h3, 2)
    i117 = Instruction(h3, h4)
    i118 = Instruction(h3, h56)
    i119 = Instruction(h15, h4)
    
    i120 = Instruction(h57, h3, 2)
    i121 = Instruction(h3, h4)
    i122 = Instruction(h3, h57)
    i123 = Instruction(h16, h4)

    i124 = Instruction(h55, h3, 2)
    i125 = Instruction(h3, h4)
    i126 = Instruction(h3, h55)
    i127 = Instruction(h17, h4)

    i128 = Instruction(h56, h3, 2)
    i129 = Instruction(h3, h4)
    i130 = Instruction(h3, h56)
    i131 = Instruction(h18, h4)
    
    i132 = Instruction(h57, h3, 2)
    i133 = Instruction(h3, h4)
    i134 = Instruction(h3, h57)
    i135 = Instruction(h19, h4)
 
    i136 = Instruction(h55, h3, 2)
    i137 = Instruction(h3, h4)
    i138 = Instruction(h3, h55)
    i139 = Instruction(h20, h4)
    
    i140 = Instruction(h56, h3, 2)
    i141 = Instruction(h3, h4)
    i142 = Instruction(h3, h56)
    i143 = Instruction(h21, h4)

    i144 = Instruction(h57, h3, 2)
    i145 = Instruction(h3, h4)
    i146 = Instruction(h3, h57)
    i147 = Instruction(h22, h4)

    i148 = Instruction(h55, h3, 2)
    i149 = Instruction(h3, h4)
    i150 = Instruction(h3, h55)
    i151 = Instruction(h23, h4)

    i152 = Instruction(h56, h3, 2)
    i153 = Instruction(h3, h4)
    i154 = Instruction(h3, h56)
    i155 = Instruction(h24, h4)    

    i156 = Instruction(h57, h3, 2)
    i157 = Instruction(h3, h4)
    i158 = Instruction(h3, h57)
    i159 = Instruction(h25, h4)
    
    i160 = Instruction(h55, h3, 2)
    i161 = Instruction(h3, h4)
    i162 = Instruction(h3, h55)
    i163 = Instruction(h26, h4)

    i164 = Instruction(h56, h3, 2)
    i165 = Instruction(h3, h4)
    i166 = Instruction(h3, h56)
    i167 = Instruction(h27, h4)

    i168 = Instruction(h57, h3, 2)
    i169 = Instruction(h3, h4)
    i170 = Instruction(h3, h57)
    i171 = Instruction(h28, h4)
    
    i172 = Instruction(h55, h3, 2)
    i173 = Instruction(h3, h4)
    i174 = Instruction(h3, h55)
    i175 = Instruction(h29, h4)
 
   #--------------3 parte------------------ 
    
    i176 = Instruction(h1, h2)
    i177 = Instruction(h5, h3)
    i178 = Instruction(h2, h1)
    i179 = Instruction(h3, h4)
    i180 = Instruction(h3, h30)
    i181 = Instruction(h2, h1)
    
    i182 = Instruction(h1, h2)
    i183 = Instruction(h6, h3)
    i184 = Instruction(h2, h1)
    i185 = Instruction(h3, h4)
    i186 = Instruction(h3, h31)
    i187 = Instruction(h2, h1)
    
    i188 = Instruction(h1, h2)
    i189 = Instruction(h7, h3)
    i190 = Instruction(h2, h1)
    i191 = Instruction(h3, h4)
    i192 = Instruction(h3, h32)
    i193 = Instruction(h2, h1)

    i194 = Instruction(h1, h2)
    i195 = Instruction(h8, h3)
    i196 = Instruction(h2, h1)
    i197 = Instruction(h3, h4)
    i198 = Instruction(h3, h33)
    i199 = Instruction(h2, h1)
    
    i200 = Instruction(h1, h2)
    i201 = Instruction(h9, h3)
    i202 = Instruction(h2, h1)
    i203 = Instruction(h3, h4)
    i204 = Instruction(h3, h34)
    i205 = Instruction(h2, h1)
    
    i206 = Instruction(h1, h2)
    i207 = Instruction(h10, h3)
    i208 = Instruction(h2, h1)
    i209 = Instruction(h3, h4)
    i210 = Instruction(h3, h35)
    i211 = Instruction(h2, h1)
    
    i212 = Instruction(h1, h2)
    i213 = Instruction(h11, h3)
    i214 = Instruction(h2, h1)
    i215 = Instruction(h3, h4)
    i216 = Instruction(h3, h36)
    i217 = Instruction(h2, h1)
    
    i218 = Instruction(h1, h2)
    i219 = Instruction(h12, h3)
    i220 = Instruction(h2, h1)
    i221 = Instruction(h3, h4)
    i222 = Instruction(h3, h37)
    i223 = Instruction(h2, h1)

    i224 = Instruction(h1, h2)
    i225 = Instruction(h13, h3)
    i226 = Instruction(h2, h1)
    i227 = Instruction(h3, h4)
    i228 = Instruction(h3, h38)
    i229 = Instruction(h2, h1)
    
    i230 = Instruction(h1, h2)
    i231 = Instruction(h14, h3)
    i232 = Instruction(h2, h1)
    i233 = Instruction(h3, h4)
    i234 = Instruction(h3, h39)
    i235 = Instruction(h2, h1)
    
    i236 = Instruction(h1, h2)
    i237 = Instruction(h15, h3)
    i238 = Instruction(h2, h1)
    i239 = Instruction(h3, h4)
    i240 = Instruction(h3, h40)
    i241 = Instruction(h2, h1)
    
    i242 = Instruction(h1, h2)
    i243 = Instruction(h16, h3)
    i244 = Instruction(h2, h1)
    i245 = Instruction(h3, h4)
    i246 = Instruction(h3, h41)
    i247 = Instruction(h2, h1)
    
    i248 = Instruction(h1, h2)
    i249 = Instruction(h17, h3)
    i250 = Instruction(h2, h1)
    i251 = Instruction(h3, h4)
    i252 = Instruction(h3, h42)
    i253 = Instruction(h2, h1)

    i254 = Instruction(h1, h2)
    i255 = Instruction(h18, h3)
    i256 = Instruction(h2, h1)
    i257 = Instruction(h3, h4)
    i258 = Instruction(h3, h43)
    i259 = Instruction(h2, h1)
    
    i260 = Instruction(h1, h2)
    i261 = Instruction(h19, h3)
    i262 = Instruction(h2, h1)
    i263 = Instruction(h3, h4)
    i264 = Instruction(h3, h44)
    i265 = Instruction(h2, h1)
    
    i266 = Instruction(h1, h2)
    i267 = Instruction(h20, h3)
    i268 = Instruction(h2, h1)
    i269 = Instruction(h3, h4)
    i270 = Instruction(h3, h45)
    i271 = Instruction(h2, h1)
    
    i272 = Instruction(h1, h2)
    i273 = Instruction(h21, h3)
    i274 = Instruction(h2, h1)
    i275 = Instruction(h3, h4)
    i276 = Instruction(h3, h46)
    i277 = Instruction(h2, h1)
    
    i278 = Instruction(h1, h2)
    i279 = Instruction(h22, h3)
    i280 = Instruction(h2, h1)
    i281 = Instruction(h3, h4)
    i282 = Instruction(h3, h47)
    i283 = Instruction(h2, h1)

    i284 = Instruction(h1, h2)
    i285 = Instruction(h23, h3)
    i286 = Instruction(h2, h1)
    i287 = Instruction(h3, h4)
    i288 = Instruction(h3, h48)
    i289 = Instruction(h2, h1)
    
    i290 = Instruction(h1, h2)
    i291 = Instruction(h24, h3)
    i292 = Instruction(h2, h1)
    i293 = Instruction(h3, h4)
    i294 = Instruction(h3, h49)
    i295 = Instruction(h2, h1)
    
    i296 = Instruction(h1, h2)
    i297 = Instruction(h25, h3)
    i298 = Instruction(h2, h1)
    i299 = Instruction(h3, h4)
    i300 = Instruction(h3, h50)
    i301 = Instruction(h2, h1)
    
    i302 = Instruction(h1, h2)
    i303 = Instruction(h26, h3)
    i304 = Instruction(h2, h1)
    i305 = Instruction(h3, h4)
    i306 = Instruction(h3, h51)
    i307 = Instruction(h2, h1)
    
    i308 = Instruction(h1, h2)
    i309 = Instruction(h27, h3)
    i310 = Instruction(h2, h1)
    i311 = Instruction(h3, h4)
    i312 = Instruction(h3, h52)
    i313 = Instruction(h2, h1)

    i314 = Instruction(h1, h2)
    i315 = Instruction(h28, h3)
    i316 = Instruction(h2, h1)
    i317 = Instruction(h3, h4)
    i318 = Instruction(h3, h53)
    i319 = Instruction(h2, h1)
    
    i320 = Instruction(h1, h2)
    i321 = Instruction(h29, h3)
    i322 = Instruction(h2, h1)
    i323 = Instruction(h3, h4)
    i324 = Instruction(h3, h54)
    i325 = Instruction(h2, h1)
    
    i326 = Instruction(None,None)

     
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,
                    i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,
                    i41,i42,i43,i44,i45,i46,i47,i48,i49,i50,i51,i52,i53,i54,i55,i56,i57,i58,i59,i60,
                    i61,i62,i63,i64,i65,i66,i67,i68,i69,i70,i71,i72,i73,i74,i75,i76,i77,i78,i79,i80,
                    i81,i82,i83,i84,i85,i86,i87,i88,i89,i90,i91,i92,i93,i94,i95,i96,i97,i98,i99,i100,
                    
                    i101,i102,i103,i104,i105,i106,i107,i108,i109,i110,i111,i112,i113,i114,i115,i116,i117,i118,i119,i120,
                    i121,i122,i123,i124,i125,i126,i127,i128,i129,i130,i131,i132,i133,i134,i135,i136,i137,i138,i139,i140,
                    i141,i142,i143,i144,i145,i146,i147,i148,i149,i150,i151,i152,i153,i154,i155,i156,i157,i158,i159,i160,
                    i161,i162,i163,i164,i165,i166,i167,i168,i169,i170,i171,i172,i173,i174,i175,i176,i177,i178,i179,i180,
                    i181,i182,i183,i184,i185,i186,i187,i188,i189,i190,i191,i192,i193,i194,i195,i196,i197,i198,i199,i200,
                    
                    i201,i202,i203,i204,i205,i206,i207,i208,i209,i210,i211,i212,i213,i214,i215,i216,i217,i218,i219,i220,
                    i221,i222,i223,i224,i225,i226,i227,i228,i229,i230,i231,i232,i233,i234,i235,i236,i237,i238,i239,i240,
                    i241,i242,i243,i244,i245,i246,i247,i248,i249,i250,i251,i252,i253,i254,i255,i256,i257,i258,i259,i260,
                    i261,i262,i263,i264,i265,i266,i267,i268,i269,i270,i271,i272,i273,i274,i275,i276,i277,i278,i279,i280,
                    i281,i282,i283,i284,i285,i286,i287,i288,i289,i290,i291,i292,i293,i294,i295,i296,i297,i298,i299,i300,
                    
                    i301,i302,i303,i304,i305,i306,i307,i308,i309,i310,i311,i312,i313,i314,i315,i316,i317,i318,i319,i320,
                    i321,i322,i323,i324,i325,i326]
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),(i2,i3,2),(i3,i2,1),(i2,i4,1),
                               (i4,i4,2),(i4,i5,1),(i5,i6,2),(i6,i5,1),(i5,i7,1),
                               (i7,i7,2),(i7,i8,1),(i8,i9,2),(i9,i8,1),(i8,i10,1),
                               (i10,i10,2),(i10,i11,1),(i11,i12,2),(i12,i11,1),(i11,i13,1),
                               (i13,i13,2),(i13,i14,1),(i14,i15,2),(i15,i14,1),(i14,i16,1),
                               
                               (i16,i16,2),(i16,i17,1),(i17,i18,2),(i18,i17,1),(i17,i19,1),
                               (i19,i19,2),(i19,i20,1),(i20,i21,2),(i21,i20,1),(i20,i22,1),
                               (i22,i22,2),(i22,i23,1),(i23,i24,2),(i24,i23,1),(i23,i25,1),
                               (i25,i25,2),(i25,i26,1),(i26,i27,2),(i27,i26,1),(i26,i28,1),
                               (i28,i28,2),(i28,i29,1),(i29,i30,2),(i30,i29,1),(i29,i31,1),
                               
                               (i31,i31,2),(i31,i32,1),(i32,i33,2),(i33,i32,1),(i32,i34,1),
                               (i34,i34,2),(i34,i35,1),(i35,i36,2),(i36,i35,1),(i35,i37,1),
                               (i37,i37,2),(i37,i38,1),(i38,i39,2),(i39,i38,1),(i38,i40,1),
                               (i40,i40,2),(i40,i41,1),(i41,i42,2),(i42,i41,1),(i41,i43,1),
                               (i43,i43,2),(i43,i44,1),(i44,i45,2),(i45,i44,1),(i44,i46,1),
                               
                               (i46,i46,2),(i46,i47,1),(i47,i48,2),(i48,i47,1),(i47,i49,1),
                               (i49,i49,2),(i49,i50,1),(i50,i51,2),(i51,i50,1),(i50,i52,1),
                               (i52,i52,2),(i52,i53,1),(i53,i54,2),(i54,i53,1),(i53,i55,1),
                               (i55,i55,2),(i55,i56,1),(i56,i57,2),(i57,i56,1),(i56,i58,1),
                               (i58,i58,2),(i58,i59,1),(i59,i60,2),(i60,i59,1),(i59,i61,1),
                               
                               (i61,i61,2),(i61,i62,1),(i62,i63,2),(i63,i62,1),(i62,i64,1),
                               (i64,i64,2),(i64,i65,1),(i65,i66,2),(i66,i65,1),(i65,i67,1),
                               (i67,i67,2),(i67,i68,1),(i68,i69,2),(i69,i68,1),(i68,i70,1),
                               (i70,i70,2),(i70,i71,1),(i71,i72,2),(i72,i71,1),(i71,i73,1),
                               (i73,i73,2),(i73,i74,1),(i74,i75,2),(i75,i74,1),(i74,i76,1),
                              
                               #La segunda parte que resta la clave
                              (i76,i76,2),(i76,i77,1),(i77,i78,2),(i78,i79,1),(i79,i77,1),(i77,i80,1),
                              (i80,i80,2),(i80,i81,1),(i81,i82,2),(i82,i83,1),(i83,i81,1),(i81,i84,1),
                              (i84,i84,2),(i84,i85,1),(i85,i86,2),(i86,i87,1),(i87,i85,1),(i85,i88,1),
                              (i88,i88,2),(i88,i89,1),(i89,i90,2),(i90,i91,1),(i91,i89,1),(i89,i92,1),
                              (i92,i92,2),(i92,i93,1),(i93,i94,2),(i94,i95,1),(i95,i93,1),(i93,i96,1),
                               
                              (i96,i96,2),(i96,i97,1),(i97,i98,2),(i98,i99,1),(i99,i97,1),(i97,i100,1),
                              (i100,i100,2),(i100,i101,1),(i101,i102,2),(i102,i103,1),(i103,i101,1),(i101,i104,1),
                              (i104,i104,2),(i104,i105,1),(i105,i106,2),(i106,i107,1),(i107,i105,1),(i105,i108,1),
                              (i108,i108,2),(i108,i109,1),(i109,i110,2),(i110,i111,1),(i111,i109,1),(i109,i112,1),
                              (i112,i112,2),(i112,i113,1),(i113,i114,2),(i114,i115,1),(i115,i113,1),(i113,i116,1),
                               
                              (i116,i116,2),(i116,i117,1),(i117,i118,2),(i118,i119,1),(i119,i117,1),(i117,i120,1),
                              (i120,i120,2),(i120,i121,1),(i121,i122,2),(i122,i123,1),(i123,i121,1),(i121,i124,1),
                              (i124,i124,2),(i124,i125,1),(i125,i126,2),(i126,i127,1),(i127,i125,1),(i125,i128,1),
                              (i128,i128,2),(i128,i129,1),(i129,i130,2),(i130,i131,1),(i131,i129,1),(i129,i132,1),
                              (i132,i132,2),(i132,i133,1),(i133,i134,2),(i134,i135,1),(i135,i133,1),(i133,i136,1),
                               
                              (i136,i136,2),(i136,i137,1),(i137,i138,2),(i138,i139,1),(i139,i137,1),(i137,i140,1),
                              (i140,i140,2),(i140,i141,1),(i141,i142,2),(i142,i143,1),(i143,i141,1),(i141,i144,1),
                              (i144,i144,2),(i144,i145,1),(i145,i146,2),(i146,i147,1),(i147,i145,1),(i145,i148,1),
                              (i148,i148,2),(i148,i149,1),(i149,i150,2),(i150,i151,1),(i151,i149,1),(i149,i152,1),
                              (i152,i152,2),(i152,i153,1),(i153,i154,2),(i154,i155,1),(i155,i153,1),(i153,i156,1),
                            
                              (i156,i156,2),(i156,i157,1),(i157,i158,2),(i158,i159,1),(i159,i157,1),(i157,i160,1),
                              (i160,i160,2),(i160,i161,1),(i161,i162,2),(i162,i163,1),(i163,i161,1),(i161,i164,1),
                              (i164,i164,2),(i164,i165,1),(i165,i166,2),(i166,i167,1),(i167,i165,1),(i165,i168,1),
                              (i168,i168,2),(i168,i169,1),(i169,i170,2),(i170,i171,1),(i171,i169,1),(i169,i172,1),
                              (i172,i172,2),(i172,i173,1),(i173,i174,2),(i174,i175,1),(i175,i173,1),(i173,i176,1),
                               
                            #A continuación la tecera parte que aplica módulo a la resta
                           (i176,i177,2),(i177,i176,2),(i176,i178,1),(i178,i176,1),(i178,i179,2),
                           (i179,i178,1),(i177,i180,1),(i180,i180,2),(i180,i181,1),(i181,i181,2),(i181,i182,1),
                           (i182,i183,2),(i183,i182,2),(i182,i184,1),(i184,i182,1),(i184,i185,2),
                           (i185,i184,1),(i183,i186,1),(i186,i186,2),(i186,i187,1),(i187,i187,2),(i187,i188,1),
                           (i188,i189,2),(i189,i188,2),(i188,i190,1),(i190,i188,1),(i190,i191,2),
                           (i191,i190,1),(i189,i192,1),(i192,i192,2),(i192,i193,1),(i193,i193,2),(i193,i194,1), 
                           (i194,i195,2),(i195,i194,2),(i194,i196,1),(i196,i194,1),(i196,i197,2),
                           (i197,i196,1),(i195,i198,1),(i198,i198,2),(i198,i199,1),(i199,i199,2),(i199,i200,1),
                           (i200,i201,2),(i201,i200,2),(i200,i202,1),(i202,i200,1),(i202,i203,2),
                           (i203,i202,1),(i201,i204,1),(i204,i204,2),(i204,i205,1),(i205,i205,2),(i205,i206,1),
                               
                           (i206,i207,2),(i207,i206,2),(i206,i208,1),(i208,i206,1),(i208,i209,2),
                           (i209,i208,1),(i207,i210,1),(i210,i210,2),(i210,i211,1),(i211,i211,2),(i211,i212,1),
                           (i212,i213,2),(i213,i212,2),(i212,i214,1),(i214,i212,1),(i214,i215,2),
                           (i215,i214,1),(i213,i216,1),(i216,i216,2),(i216,i217,1),(i217,i217,2),(i217,i218,1),
                           (i218,i219,2),(i219,i218,2),(i218,i220,1),(i220,i218,1),(i220,i221,2),
                           (i221,i220,1),(i219,i222,1),(i222,i222,2),(i222,i223,1),(i223,i223,2),(i223,i224,1), 
                           (i224,i225,2),(i225,i224,2),(i224,i226,1),(i226,i224,1),(i226,i227,2),
                           (i227,i226,1),(i225,i228,1),(i228,i228,2),(i228,i229,1),(i229,i229,2),(i229,i230,1),
                           (i230,i231,2),(i231,i230,2),(i230,i232,1),(i232,i230,1),(i232,i233,2),
                           (i233,i232,1),(i231,i234,1),(i234,i234,2),(i234,i235,1),(i235,i235,2),(i235,i236,1),
                               
                           (i236,i237,2),(i237,i236,2),(i236,i238,1),(i238,i236,1),(i238,i239,2),
                           (i239,i238,1),(i237,i240,1),(i240,i240,2),(i240,i241,1),(i241,i241,2),(i241,i242,1),
                           (i242,i243,2),(i243,i242,2),(i242,i244,1),(i244,i242,1),(i244,i245,2),
                           (i245,i244,1),(i243,i246,1),(i246,i246,2),(i246,i247,1),(i247,i247,2),(i247,i248,1),
                           (i248,i249,2),(i249,i248,2),(i248,i250,1),(i250,i248,1),(i250,i251,2),
                           (i251,i250,1),(i249,i252,1),(i252,i252,2),(i252,i253,1),(i253,i253,2),(i253,i254,1), 
                           (i254,i255,2),(i255,i254,2),(i254,i256,1),(i256,i254,1),(i256,i257,2),
                           (i257,i256,1),(i255,i258,1),(i258,i258,2),(i258,i259,1),(i259,i259,2),(i259,i260,1),
                           (i260,i261,2),(i261,i260,2),(i260,i262,1),(i262,i260,1),(i262,i263,2),
                           (i263,i262,1),(i261,i264,1),(i264,i264,2),(i264,i265,1),(i265,i265,2),(i265,i266,1),
                               
                           (i266,i267,2),(i267,i266,2),(i266,i268,1),(i268,i266,1),(i268,i269,2),
                           (i269,i268,1),(i267,i270,1),(i270,i270,2),(i270,i271,1),(i271,i271,2),(i271,i272,1),
                           (i272,i273,2),(i273,i272,2),(i272,i274,1),(i274,i272,1),(i274,i275,2),
                           (i275,i274,1),(i273,i276,1),(i276,i276,2),(i276,i277,1),(i277,i277,2),(i277,i278,1),
                           (i278,i279,2),(i279,i278,2),(i278,i280,1),(i280,i278,1),(i280,i281,2),
                           (i281,i280,1),(i279,i282,1),(i282,i282,2),(i282,i283,1),(i283,i283,2),(i283,i284,1), 
                           (i284,i285,2),(i285,i284,2),(i284,i286,1),(i286,i284,1),(i286,i287,2),
                           (i287,i286,1),(i285,i288,1),(i288,i288,2),(i288,i289,1),(i289,i289,2),(i289,i290,1),
                           (i290,i291,2),(i291,i290,2),(i290,i292,1),(i292,i290,1),(i292,i293,2),
                           (i293,i292,1),(i291,i294,1),(i294,i294,2),(i294,i295,1),(i295,i295,2),(i295,i296,1),
                               
                           (i296,i297,2),(i297,i296,2),(i296,i298,1),(i298,i296,1),(i298,i299,2),
                           (i299,i298,1),(i297,i300,1),(i300,i300,2),(i300,i301,1),(i301,i301,2),(i301,i302,1),
                           (i302,i303,2),(i303,i302,2),(i302,i304,1),(i304,i302,1),(i304,i305,2),
                           (i305,i304,1),(i303,i306,1),(i306,i306,2),(i306,i307,1),(i307,i307,2),(i307,i308,1),
                           (i308,i309,2),(i309,i308,2),(i308,i310,1),(i310,i308,1),(i310,i311,2),
                           (i311,i310,1),(i309,i312,1),(i312,i312,2),(i312,i313,1),(i313,i313,2),(i313,i314,1), 
                           (i314,i315,2),(i315,i314,2),(i314,i316,1),(i316,i314,1),(i316,i317,2),
                           (i317,i316,1),(i315,i318,1),(i318,i318,2),(i318,i319,1),(i319,i319,2),(i319,i320,1),
                           (i320,i321,2),(i321,i320,2),(i320,i322,1),(i322,i320,1),(i322,i323,2),
                           (i323,i322,1),(i321,i324,1),(i324,i324,2),(i324,i325,1),(i325,i325,2),(i325,i326,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm


#Texto 25, clave 6

def Vig_Codificacion_25_6(t,c):
    c1,c2,c3,c4,c5,c6 = c
    t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25 = t
    
    h1 = Host(26)
    h2 = Host()
    h3 = Host()
    h4 = Host()
    h5 = Host(t1)
    h6 = Host(t2)
    h7 = Host(t3)
    h8 = Host(t4)
    h9 = Host(t5)
    h10 = Host(t6)
    h11 = Host(t7)
    h12 = Host(t8)
    h13 = Host(t9)
    h14 = Host(t10)
    h15 = Host(t11)
    h16 = Host(t12)
    h17 = Host(t13)
    h18 = Host(t14)
    h19 = Host(t15)
    h20 = Host(t16)
    h21 = Host(t17)
    h22 = Host(t18)
    h23 = Host(t19)
    h24 = Host(t20)
    h25 = Host(t21)
    h26 = Host(t22) 
    h27 = Host(t23)
    h28 = Host(t24)
    h29 = Host(t25)
    h30 = Host()
    h31 = Host()
    h32 = Host()
    h33 = Host()
    h34 = Host()
    h35 = Host()
    h36 = Host() 
    h37 = Host()
    h38 = Host()
    h39 = Host()
    h40 = Host()
    h41 = Host()
    h42 = Host()
    h43 = Host()
    h44 = Host()
    h45 = Host()
    h46 = Host() 
    h47 = Host()
    h48 = Host()
    h49 = Host()
    h50 = Host()
    h51 = Host()
    h52 = Host() 
    h53 = Host()
    h54 = Host()
    h55 = Host(c1)
    h56 = Host(c2) 
    h57 = Host(c3)
    h58 = Host(c4)
    h59 = Host(c5) 
    h60 = Host(c6)
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,
             h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,
             h21,h22,h23,h24,h25,h26,h27,h28,h29,h30,
             h31,h32,h33,h34,h35,h36,h37,h38,h39,h40,
             h41,h42,h43,h44,h45,h46,h47,h48,h49,h50,
             h51,h52,h53,h54,h55,h56,h57,h58,h59,h60,env]
    
    i1 = Instruction(h55, h3, 2)
    i2 = Instruction(h3, h55)
    i3 = Instruction(h3, h5)
    
    i4 = Instruction(h56, h3, 2)
    i5 = Instruction(h3, h56)
    i6 = Instruction(h3, h6)
    
    i7 = Instruction(h57, h3, 2)
    i8 = Instruction(h3, h57)
    i9 = Instruction(h3, h7)
    
    i10 = Instruction(h58, h3, 2)
    i11 = Instruction(h3, h58)
    i12 = Instruction(h3, h8)
    
    i13 = Instruction(h59, h3, 2)
    i14 = Instruction(h3, h59)
    i15 = Instruction(h3, h9) 
    
    i16 = Instruction(h60, h3, 2)
    i17 = Instruction(h3, h60)
    i18 = Instruction(h3, h10)
    
    i19 = Instruction(h55, h3, 2)
    i20 = Instruction(h3, h55)
    i21 = Instruction(h3, h11)
    
    i22 = Instruction(h56, h3, 2)
    i23 = Instruction(h3, h56)
    i24 = Instruction(h3, h12)
    
    i25 = Instruction(h57, h3, 2)
    i26 = Instruction(h3, h57)
    i27 = Instruction(h3, h13)
    
    i28 = Instruction(h58, h3, 2)
    i29 = Instruction(h3, h58)
    i30 = Instruction(h3, h14) 
    
    i31 = Instruction(h59, h3, 2)
    i32 = Instruction(h3, h59)
    i33 = Instruction(h3, h15)
    
    i34 = Instruction(h60, h3, 2)
    i35 = Instruction(h3, h60)
    i36 = Instruction(h3, h16)
    
    i37 = Instruction(h55, h3, 2)
    i38 = Instruction(h3, h55)
    i39 = Instruction(h3, h17)
    
    i40 = Instruction(h56, h3, 2)
    i41 = Instruction(h3, h56)
    i42 = Instruction(h3, h18)
    
    i43 = Instruction(h57, h3, 2)
    i44 = Instruction(h3, h57)
    i45 = Instruction(h3, h19) 
    
    i46 = Instruction(h58, h3, 2)
    i47 = Instruction(h3, h58)
    i48 = Instruction(h3, h20)
    
    i49 = Instruction(h59, h3, 2)
    i50 = Instruction(h3, h59)
    i51 = Instruction(h3, h21)
    
    i52 = Instruction(h60, h3, 2)
    i53 = Instruction(h3, h60)
    i54 = Instruction(h3, h22)
    
    i55 = Instruction(h55, h3, 2)
    i56 = Instruction(h3, h55)
    i57 = Instruction(h3, h23)

    i58 = Instruction(h56, h3, 2)
    i59 = Instruction(h3, h56)
    i60 = Instruction(h3, h24) 
    
    i61 = Instruction(h57, h3, 2)
    i62 = Instruction(h3, h57)
    i63 = Instruction(h3, h25)
    
    i64 = Instruction(h58, h3, 2)
    i65 = Instruction(h3, h58)
    i66 = Instruction(h3, h26)
    
    i67 = Instruction(h59, h3, 2)
    i68 = Instruction(h3, h59)
    i69 = Instruction(h3, h27)
    
    i70 = Instruction(h60, h3, 2)
    i71 = Instruction(h3, h60)
    i72 = Instruction(h3, h28)
    
    i73 = Instruction(h55, h3, 2)
    i74 = Instruction(h3, h55)
    i75 = Instruction(h3, h29) 
    
    
    #-----2 parte--------------
    
    i76 = Instruction(h1, h2)
    i77 = Instruction(h5, h3)
    i78 = Instruction(h2, h1)
    i79 = Instruction(h3, h4)
    i80 = Instruction(h3, h30)
    i81 = Instruction(h2, h1)
    
    i82 = Instruction(h1, h2)
    i83 = Instruction(h6, h3)
    i84 = Instruction(h2, h1)
    i85 = Instruction(h3, h4)
    i86 = Instruction(h3, h31)
    i87 = Instruction(h2, h1)
    
    i88 = Instruction(h1, h2)
    i89 = Instruction(h7, h3)
    i90 = Instruction(h2, h1)
    i91 = Instruction(h3, h4)
    i92 = Instruction(h3, h32)
    i93 = Instruction(h2, h1)

    i94 = Instruction(h1, h2)
    i95 = Instruction(h8, h3)
    i96 = Instruction(h2, h1)
    i97 = Instruction(h3, h4)
    i98 = Instruction(h3, h33)
    i99 = Instruction(h2, h1)
    
    i100 = Instruction(h1, h2)
    i101 = Instruction(h9, h3)
    i102 = Instruction(h2, h1)
    i103 = Instruction(h3, h4)
    i104 = Instruction(h3, h34)
    i105 = Instruction(h2, h1)
    
    i106 = Instruction(h1, h2)
    i107 = Instruction(h10, h3)
    i108 = Instruction(h2, h1)
    i109 = Instruction(h3, h4)
    i110 = Instruction(h3, h35)
    i111 = Instruction(h2, h1)
    
    i112 = Instruction(h1, h2)
    i113 = Instruction(h11, h3)
    i114 = Instruction(h2, h1)
    i115 = Instruction(h3, h4)
    i116 = Instruction(h3, h36)
    i117 = Instruction(h2, h1)
    
    i118 = Instruction(h1, h2)
    i119 = Instruction(h12, h3)
    i120 = Instruction(h2, h1)
    i121 = Instruction(h3, h4)
    i122 = Instruction(h3, h37)
    i123 = Instruction(h2, h1)

    i124 = Instruction(h1, h2)
    i125 = Instruction(h13, h3)
    i126 = Instruction(h2, h1)
    i127 = Instruction(h3, h4)
    i128 = Instruction(h3, h38)
    i129 = Instruction(h2, h1)
    
    i130 = Instruction(h1, h2)
    i131 = Instruction(h14, h3)
    i132 = Instruction(h2, h1)
    i133 = Instruction(h3, h4)
    i134 = Instruction(h3, h39)
    i135 = Instruction(h2, h1)
    
    i136 = Instruction(h1, h2)
    i137 = Instruction(h15, h3)
    i138 = Instruction(h2, h1)
    i139 = Instruction(h3, h4)
    i140 = Instruction(h3, h40)
    i141 = Instruction(h2, h1)
    
    i142 = Instruction(h1, h2)
    i143 = Instruction(h16, h3)
    i144 = Instruction(h2, h1)
    i145 = Instruction(h3, h4)
    i146 = Instruction(h3, h41)
    i147 = Instruction(h2, h1)
    
    i148 = Instruction(h1, h2)
    i149 = Instruction(h17, h3)
    i150 = Instruction(h2, h1)
    i151 = Instruction(h3, h4)
    i152 = Instruction(h3, h42)
    i153 = Instruction(h2, h1)

    i154 = Instruction(h1, h2)
    i155 = Instruction(h18, h3)
    i156 = Instruction(h2, h1)
    i157 = Instruction(h3, h4)
    i158 = Instruction(h3, h43)
    i159 = Instruction(h2, h1)
    
    i160 = Instruction(h1, h2)
    i161 = Instruction(h19, h3)
    i162 = Instruction(h2, h1)
    i163 = Instruction(h3, h4)
    i164 = Instruction(h3, h44)
    i165 = Instruction(h2, h1)
    
    i166 = Instruction(h1, h2)
    i167 = Instruction(h20, h3)
    i168 = Instruction(h2, h1)
    i169 = Instruction(h3, h4)
    i170 = Instruction(h3, h45)
    i171 = Instruction(h2, h1)
    
    i172 = Instruction(h1, h2)
    i173 = Instruction(h21, h3)
    i174 = Instruction(h2, h1)
    i175 = Instruction(h3, h4)
    i176 = Instruction(h3, h46)
    i177 = Instruction(h2, h1)
    
    i178 = Instruction(h1, h2)
    i179 = Instruction(h22, h3)
    i180 = Instruction(h2, h1)
    i181 = Instruction(h3, h4)
    i182 = Instruction(h3, h47)
    i183 = Instruction(h2, h1)

    i184 = Instruction(h1, h2)
    i185 = Instruction(h23, h3)
    i186 = Instruction(h2, h1)
    i187 = Instruction(h3, h4)
    i188 = Instruction(h3, h48)
    i189 = Instruction(h2, h1)
    
    i190 = Instruction(h1, h2)
    i191 = Instruction(h24, h3)
    i192 = Instruction(h2, h1)
    i193 = Instruction(h3, h4)
    i194 = Instruction(h3, h49)
    i195 = Instruction(h2, h1)
    
    i196 = Instruction(h1, h2)
    i197 = Instruction(h25, h3)
    i198 = Instruction(h2, h1)
    i199 = Instruction(h3, h4)
    i200 = Instruction(h3, h50)
    i201 = Instruction(h2, h1)
    
    i202 = Instruction(h1, h2)
    i203 = Instruction(h26, h3)
    i204 = Instruction(h2, h1)
    i205 = Instruction(h3, h4)
    i206 = Instruction(h3, h51)
    i207 = Instruction(h2, h1)
    
    i208 = Instruction(h1, h2)
    i209 = Instruction(h27, h3)
    i210 = Instruction(h2, h1)
    i211 = Instruction(h3, h4)
    i212 = Instruction(h3, h52)
    i213 = Instruction(h2, h1)

    i214 = Instruction(h1, h2)
    i215 = Instruction(h28, h3)
    i216 = Instruction(h2, h1)
    i217 = Instruction(h3, h4)
    i218 = Instruction(h3, h53)
    i219 = Instruction(h2, h1)
    
    i220 = Instruction(h1, h2)
    i221 = Instruction(h29, h3)
    i222 = Instruction(h2, h1)
    i223 = Instruction(h3, h4)
    i224 = Instruction(h3, h54)
    i225 = Instruction(h2, h1)
    
    i226 = Instruction(None,None)

    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,
                    i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,
                    i41,i42,i43,i44,i45,i46,i47,i48,i49,i50,i51,i52,i53,i54,i55,i56,i57,i58,i59,i60,
                    i61,i62,i63,i64,i65,i66,i67,i68,i69,i70,i71,i72,i73,i74,i75,i76,i77,i78,i79,i80,
                    i81,i82,i83,i84,i85,i86,i87,i88,i89,i90,i91,i92,i93,i94,i95,i96,i97,i98,i99,i100,
                    
                    i101,i102,i103,i104,i105,i106,i107,i108,i109,i110,i111,i112,i113,i114,i115,i116,i117,i118,i119,i120,
                    i121,i122,i123,i124,i125,i126,i127,i128,i129,i130,i131,i132,i133,i134,i135,i136,i137,i138,i139,i140,
                    i141,i142,i143,i144,i145,i146,i147,i148,i149,i150,i151,i152,i153,i154,i155,i156,i157,i158,i159,i160,
                    i161,i162,i163,i164,i165,i166,i167,i168,i169,i170,i171,i172,i173,i174,i175,i176,i177,i178,i179,i180,
                    i181,i182,i183,i184,i185,i186,i187,i188,i189,i190,i191,i192,i193,i194,i195,i196,i197,i198,i199,i200,
                    
                    i201,i202,i203,i204,i205,i206,i207,i208,i209,i210,i211,i212,i213,i214,i215,i216,i217,i218,i219,i220,
                    i221,i222,i223,i224,i225,i226]
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),(i2,i3,2),(i3,i2,1),(i2,i4,1),
                               (i4,i4,2),(i4,i5,1),(i5,i6,2),(i6,i5,1),(i5,i7,1),
                               (i7,i7,2),(i7,i8,1),(i8,i9,2),(i9,i8,1),(i8,i10,1),
                               (i10,i10,2),(i10,i11,1),(i11,i12,2),(i12,i11,1),(i11,i13,1),
                               (i13,i13,2),(i13,i14,1),(i14,i15,2),(i15,i14,1),(i14,i16,1),
                               
                               (i16,i16,2),(i16,i17,1),(i17,i18,2),(i18,i17,1),(i17,i19,1),
                               (i19,i19,2),(i19,i20,1),(i20,i21,2),(i21,i20,1),(i20,i22,1),
                               (i22,i22,2),(i22,i23,1),(i23,i24,2),(i24,i23,1),(i23,i25,1),
                               (i25,i25,2),(i25,i26,1),(i26,i27,2),(i27,i26,1),(i26,i28,1),
                               (i28,i28,2),(i28,i29,1),(i29,i30,2),(i30,i29,1),(i29,i31,1),

                               (i31,i31,2),(i31,i32,1),(i32,i33,2),(i33,i32,1),(i32,i34,1),
                               (i34,i34,2),(i34,i35,1),(i35,i36,2),(i36,i35,1),(i35,i37,1),
                               (i37,i37,2),(i37,i38,1),(i38,i39,2),(i39,i38,1),(i38,i40,1),
                               (i40,i40,2),(i40,i41,1),(i41,i42,2),(i42,i41,1),(i41,i43,1),
                               (i43,i43,2),(i43,i44,1),(i44,i45,2),(i45,i44,1),(i44,i46,1),
                               
                               (i46,i46,2),(i46,i47,1),(i47,i48,2),(i48,i47,1),(i47,i49,1),
                               (i49,i49,2),(i49,i50,1),(i50,i51,2),(i51,i50,1),(i50,i52,1),
                               (i52,i52,2),(i52,i53,1),(i53,i54,2),(i54,i53,1),(i53,i55,1),
                               (i55,i55,2),(i55,i56,1),(i56,i57,2),(i57,i56,1),(i56,i58,1),
                               (i58,i58,2),(i58,i59,1),(i59,i60,2),(i60,i59,1),(i59,i61,1),
                               
                               (i61,i61,2),(i61,i62,1),(i62,i63,2),(i63,i62,1),(i62,i64,1),
                               (i64,i64,2),(i64,i65,1),(i65,i66,2),(i66,i65,1),(i65,i67,1),
                               (i67,i67,2),(i67,i68,1),(i68,i69,2),(i69,i68,1),(i68,i70,1),
                               (i70,i70,2),(i70,i71,1),(i71,i72,2),(i72,i71,1),(i71,i73,1),
                               (i73,i73,2),(i73,i74,1),(i74,i75,2),(i75,i74,1),(i74,i76,1),
                              
                               #A continuación la segunda parte que aplica módulo a la suma obtenida
                               (i76,i77,2),(i77,i76,2),(i76,i78,1),(i78,i76,1),(i78,i79,2),
                               (i79,i78,1),(i77,i80,1),(i80,i80,2),(i80,i81,1),(i81,i81,2),(i81,i82,1),                               
                               (i82,i83,2),(i83,i82,2),(i82,i84,1),(i84,i82,1),(i84,i85,2),
                               (i85,i84,1),(i83,i86,1),(i86,i86,2),(i86,i87,1),(i87,i87,2),(i87,i88,1),                               
                               (i88,i89,2),(i89,i88,2),(i88,i90,1),(i90,i88,1),(i90,i91,2),
                               (i91,i90,1),(i89,i92,1),(i92,i92,2),(i92,i93,1),(i93,i93,2),(i93,i94,1),                                                                
                               (i94,i95,2),(i95,i94,2),(i94,i96,1),(i96,i94,1),(i96,i97,2),
                               (i97,i96,1),(i95,i98,1),(i98,i98,2),(i98,i99,1),(i99,i99,2),(i99,i100,1),                              
                               (i100,i101,2),(i101,i100,2),(i100,i102,1),(i102,i100,1),(i102,i103,2),
                               (i103,i102,1),(i101,i104,1),(i104,i104,2),(i104,i105,1),(i105,i105,2),(i105,i106,1),
                                                       
                               (i106,i107,2),(i107,i106,2),(i106,i108,1),(i108,i106,1),(i108,i109,2),
                               (i109,i108,1),(i107,i110,1),(i110,i110,2),(i110,i111,1),(i111,i111,2),(i111,i112,1),                               
                               (i112,i113,2),(i113,i112,2),(i112,i114,1),(i114,i112,1),(i114,i115,2),
                               (i115,i114,1),(i113,i116,1),(i116,i116,2),(i116,i117,1),(i117,i117,2),(i117,i118,1),                               
                               (i118,i119,2),(i119,i118,2),(i118,i120,1),(i120,i118,1),(i120,i121,2),
                               (i121,i120,1),(i119,i122,1),(i122,i122,2),(i122,i123,1),(i123,i123,2),(i123,i124,1),                                                                                      
                               (i124,i125,2),(i125,i124,2),(i124,i126,1),(i126,i124,1),(i126,i127,2),
                               (i127,i126,1),(i125,i128,1),(i128,i128,2),(i128,i129,1),(i129,i129,2),(i129,i130,1),                      
                               (i130,i131,2),(i131,i130,2),(i130,i132,1),(i132,i130,1),(i132,i133,2),
                               (i133,i132,1),(i131,i134,1),(i134,i134,2),(i134,i135,1),(i135,i135,2),(i135,i136,1),
                               
                               (i136,i137,2),(i137,i136,2),(i136,i138,1),(i138,i136,1),(i138,i139,2),
                               (i139,i138,1),(i137,i140,1),(i140,i140,2),(i140,i141,1),(i141,i141,2),(i141,i142,1),     
                               (i142,i143,2),(i143,i142,2),(i142,i144,1),(i144,i142,1),(i144,i145,2),
                               (i145,i144,1),(i143,i146,1),(i146,i146,2),(i146,i147,1),(i147,i147,2),(i147,i148,1),                               
                               (i148,i149,2),(i149,i148,2),(i148,i150,1),(i150,i148,1),(i150,i151,2),
                               (i151,i150,1),(i149,i152,1),(i152,i152,2),(i152,i153,1),(i153,i153,2),(i153,i154,1),                                                                                      
                               (i154,i155,2),(i155,i154,2),(i154,i156,1),(i156,i154,1),(i156,i157,2),
                               (i157,i156,1),(i155,i158,1),(i158,i158,2),(i158,i159,1),(i159,i159,2),(i159,i160,1),                      
                               (i160,i161,2),(i161,i160,2),(i160,i162,1),(i162,i160,1),(i162,i163,2),
                               (i163,i162,1),(i161,i164,1),(i164,i164,2),(i164,i165,1),(i165,i165,2),(i165,i166,1),
                               
                               (i166,i167,2),(i167,i166,2),(i166,i168,1),(i168,i166,1),(i168,i169,2),
                               (i169,i168,1),(i167,i170,1),(i170,i170,2),(i170,i171,1),(i171,i171,2),(i171,i172,1),                               
                               (i172,i173,2),(i173,i172,2),(i172,i174,1),(i174,i172,1),(i174,i175,2),
                               (i175,i174,1),(i173,i176,1),(i176,i176,2),(i176,i177,1),(i177,i177,2),(i177,i178,1),                               
                               (i178,i179,2),(i179,i178,2),(i178,i180,1),(i180,i178,1),(i180,i181,2),
                               (i181,i180,1),(i179,i182,1),(i182,i182,2),(i182,i183,1),(i183,i183,2),(i183,i184,1),                                                                                      
                               (i184,i185,2),(i185,i184,2),(i184,i186,1),(i186,i184,1),(i186,i187,2),
                               (i187,i186,1),(i185,i188,1),(i188,i188,2),(i188,i189,1),(i189,i189,2),(i189,i190,1),                      
                               (i190,i191,2),(i191,i190,2),(i190,i192,1),(i192,i190,1),(i192,i193,2),
                               (i193,i192,1),(i191,i194,1),(i194,i194,2),(i194,i195,1),(i195,i195,2),(i195,i196,1),
                               
                               (i196,i197,2),(i197,i196,2),(i196,i198,1),(i198,i196,1),(i198,i199,2),
                               (i199,i198,1),(i197,i200,1),(i200,i200,2),(i200,i201,1),(i201,i201,2),(i201,i202,1),                               
                               (i202,i203,2),(i203,i202,2),(i202,i204,1),(i204,i202,1),(i204,i205,2),
                               (i205,i204,1),(i203,i206,1),(i206,i206,2),(i206,i207,1),(i207,i207,2),(i207,i208,1),                               
                               (i208,i209,2),(i209,i208,2),(i208,i210,1),(i210,i208,1),(i210,i211,2),
                               (i211,i210,1),(i209,i212,1),(i212,i212,2),(i212,i213,1),(i213,i213,2),(i213,i214,1),                                                                                      
                               (i214,i215,2),(i215,i214,2),(i214,i216,1),(i216,i214,1),(i216,i217,2),
                               (i217,i216,1),(i215,i218,1),(i218,i218,2),(i218,i219,1),(i219,i219,2),(i219,i220,1),                      
                               (i220,i221,2),(i221,i220,2),(i220,i222,1),(i222,i220,1),(i222,i223,2),
                               (i223,i222,1),(i221,i224,1),(i224,i224,2),(i224,i225,1),(i225,i225,2),(i225,i226,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def Vig_Decodificacion_25_6(t,c):
    c1,c2,c3,c4,c5,c6 = c
    t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22,t23,t24,t25 = t
    h1 = Host(26)
    h2 = Host()
    h3 = Host()
    h4 = Host()
    h5 = Host(t1)
    h6 = Host(t2)
    h7 = Host(t3)
    h8 = Host(t4)
    h9 = Host(t5)
    h10 = Host(t6)
    h11 = Host(t7)
    h12 = Host(t8)
    h13 = Host(t9)
    h14 = Host(t10)
    h15 = Host(t11)
    h16 = Host(t12)
    h17 = Host(t13)
    h18 = Host(t14)
    h19 = Host(t15)
    h20 = Host(t16)
    h21 = Host(t17)
    h22 = Host(t18)
    h23 = Host(t19)
    h24 = Host(t20)
    h25 = Host(t21)
    h26 = Host(t22) 
    h27 = Host(t23)
    h28 = Host(t24)
    h29 = Host(t25)
    h30 = Host()
    h31 = Host()
    h32 = Host()
    h33 = Host()
    h34 = Host()
    h35 = Host()
    h36 = Host() 
    h37 = Host()
    h38 = Host()
    h39 = Host()
    h40 = Host()
    h41 = Host()
    h42 = Host()
    h43 = Host()
    h44 = Host()
    h45 = Host()
    h46 = Host() 
    h47 = Host()
    h48 = Host()
    h49 = Host()
    h50 = Host()
    h51 = Host()
    h52 = Host() 
    h53 = Host()
    h54 = Host()
    h55 = Host(c1)
    h56 = Host(c2)  
    h57 = Host(c3)
    h58 = Host(c4)
    h59 = Host(c5)  
    h60 = Host(c6)
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,
             h11,h12,h13,h14,h15,h16,h17,h18,h19,h20,
             h21,h22,h23,h24,h25,h26,h27,h28,h29,h30,
             h31,h32,h33,h34,h35,h36,h37,h38,h39,h40,
             h41,h42,h43,h44,h45,h46,h47,h48,h49,h50,
             h51,h52,h53,h54,h55,h56,h57,h58,h59,h60,env]
    
    i1 = Instruction(h1, h2, 2)
    i2 = Instruction(h2, h5)
    i3 = Instruction(h2, h1)
    
    i4 = Instruction(h1, h2, 2)
    i5 = Instruction(h2, h6)
    i6 = Instruction(h2, h1)
    
    i7 = Instruction(h1, h2, 2)
    i8 = Instruction(h2, h7)
    i9 = Instruction(h2, h1)
    
    i10 = Instruction(h1, h2, 2)
    i11 = Instruction(h2, h8)
    i12 = Instruction(h2, h1)
    
    i13 = Instruction(h1, h2, 2)
    i14 = Instruction(h2, h9)
    i15 = Instruction(h2, h1) 
    
    i16 = Instruction(h1, h2, 2)
    i17 = Instruction(h2, h10)
    i18 = Instruction(h2, h1)
    
    i19 = Instruction(h1, h2, 2)
    i20 = Instruction(h2, h11)
    i21 = Instruction(h2, h1)
    
    i22 = Instruction(h1, h2, 2)
    i23 = Instruction(h2, h12)
    i24 = Instruction(h2, h1)
    
    i25 = Instruction(h1, h2, 2)
    i26 = Instruction(h2, h13)
    i27 = Instruction(h2, h1)
    
    i28 = Instruction(h1, h2, 2)
    i29 = Instruction(h2, h14)
    i30 = Instruction(h2, h1) 
    
    i31 = Instruction(h1, h2, 2)
    i32 = Instruction(h2, h15)
    i33 = Instruction(h2, h1)
    
    i34 = Instruction(h1, h2, 2)
    i35 = Instruction(h2, h16)
    i36 = Instruction(h2, h1)
    
    i37 = Instruction(h1, h2, 2)
    i38 = Instruction(h2, h17)
    i39 = Instruction(h2, h1)
    
    i40 = Instruction(h1, h2, 2)
    i41 = Instruction(h2, h18)
    i42 = Instruction(h2, h1)
    
    i43 = Instruction(h1, h2, 2)
    i44 = Instruction(h2, h19)
    i45 = Instruction(h2, h1) 
    
    i46 = Instruction(h1, h2, 2)
    i47 = Instruction(h2, h20)
    i48 = Instruction(h2, h1)
    
    i49 = Instruction(h1, h2, 2)
    i50 = Instruction(h2, h21)
    i51 = Instruction(h2, h1)
    
    i52 = Instruction(h1, h2, 2)
    i53 = Instruction(h2, h22)
    i54 = Instruction(h2, h1)
    
    i55 = Instruction(h1, h2, 2)
    i56 = Instruction(h2, h23)
    i57 = Instruction(h2, h1)
    
    i58 = Instruction(h1, h2, 2)
    i59 = Instruction(h2, h24)
    i60 = Instruction(h2, h1) 
    
    i61 = Instruction(h1, h2, 2)
    i62 = Instruction(h2, h25)
    i63 = Instruction(h2, h1)
    
    i64 = Instruction(h1, h2, 2)
    i65 = Instruction(h2, h26)
    i66 = Instruction(h2, h1)
    
    i67 = Instruction(h1, h2, 2)
    i68 = Instruction(h2, h27)
    i69 = Instruction(h2, h1)
    
    i70 = Instruction(h1, h2, 2)
    i71 = Instruction(h2, h28)
    i72 = Instruction(h2, h1)
    
    i73 = Instruction(h1, h2, 2)
    i74 = Instruction(h2, h29)
    i75 = Instruction(h2, h1) 
    
    #----------- 2 parte---------------
    
    i76 = Instruction(h55, h3, 2)
    i77 = Instruction(h3, h4)
    i78 = Instruction(h3, h55)
    i79 = Instruction(h5, h4)
    
    i80 = Instruction(h56, h3, 2)
    i81 = Instruction(h3, h4)
    i82 = Instruction(h3, h56)
    i83 = Instruction(h6, h4)

    i84 = Instruction(h57, h3, 2)
    i85 = Instruction(h3, h4)
    i86 = Instruction(h3, h57)
    i87 = Instruction(h7, h4)

    i88 = Instruction(h58, h3, 2)
    i89 = Instruction(h3, h4)
    i90 = Instruction(h3, h58)
    i91 = Instruction(h8, h4)
    
    i92 = Instruction(h59, h3, 2)
    i93 = Instruction(h3, h4)
    i94 = Instruction(h3, h59)
    i95 = Instruction(h9, h4)
 
    i96 = Instruction(h60, h3, 2)
    i97 = Instruction(h3, h4)
    i98 = Instruction(h3, h60)
    i99 = Instruction(h10, h4)
    
    i100 = Instruction(h55, h3, 2)
    i101 = Instruction(h3, h4)
    i102 = Instruction(h3, h55)
    i103 = Instruction(h11, h4)

    i104 = Instruction(h56, h3, 2)
    i105 = Instruction(h3, h4)
    i106 = Instruction(h3, h56)
    i107 = Instruction(h12, h4)

    i108 = Instruction(h57, h3, 2)
    i109 = Instruction(h3, h4)
    i110 = Instruction(h3, h57)
    i111 = Instruction(h13, h4)

    i112 = Instruction(h58, h3, 2)
    i113 = Instruction(h3, h4)
    i114 = Instruction(h3, h58)
    i115 = Instruction(h14, h4)
    
    i116 = Instruction(h59, h3, 2)
    i117 = Instruction(h3, h4)
    i118 = Instruction(h3, h59)
    i119 = Instruction(h15, h4)
    
    i120 = Instruction(h60, h3, 2)
    i121 = Instruction(h3, h4)
    i122 = Instruction(h3, h60)
    i123 = Instruction(h16, h4)

    i124 = Instruction(h55, h3, 2)
    i125 = Instruction(h3, h4)
    i126 = Instruction(h3, h55)
    i127 = Instruction(h17, h4)

    i128 = Instruction(h56, h3, 2)
    i129 = Instruction(h3, h4)
    i130 = Instruction(h3, h56)
    i131 = Instruction(h18, h4)
    
    i132 = Instruction(h57, h3, 2)
    i133 = Instruction(h3, h4)
    i134 = Instruction(h3, h57)
    i135 = Instruction(h19, h4)
 
    i136 = Instruction(h58, h3, 2)
    i137 = Instruction(h3, h4)
    i138 = Instruction(h3, h58)
    i139 = Instruction(h20, h4)
    
    i140 = Instruction(h59, h3, 2)
    i141 = Instruction(h3, h4)
    i142 = Instruction(h3, h59)
    i143 = Instruction(h21, h4)

    i144 = Instruction(h60, h3, 2)
    i145 = Instruction(h3, h4)
    i146 = Instruction(h3, h60)
    i147 = Instruction(h22, h4)

    i148 = Instruction(h55, h3, 2)
    i149 = Instruction(h3, h4)
    i150 = Instruction(h3, h55)
    i151 = Instruction(h23, h4)

    i152 = Instruction(h56, h3, 2)
    i153 = Instruction(h3, h4)
    i154 = Instruction(h3, h56)
    i155 = Instruction(h24, h4)    

    i156 = Instruction(h57, h3, 2)
    i157 = Instruction(h3, h4)
    i158 = Instruction(h3, h57)
    i159 = Instruction(h25, h4)
    
    i160 = Instruction(h58, h3, 2)
    i161 = Instruction(h3, h4)
    i162 = Instruction(h3, h58)
    i163 = Instruction(h26, h4)

    i164 = Instruction(h59, h3, 2)
    i165 = Instruction(h3, h4)
    i166 = Instruction(h3, h59)
    i167 = Instruction(h27, h4)

    i168 = Instruction(h60, h3, 2)
    i169 = Instruction(h3, h4)
    i170 = Instruction(h3, h60)
    i171 = Instruction(h28, h4)
    
    i172 = Instruction(h55, h3, 2)
    i173 = Instruction(h3, h4)
    i174 = Instruction(h3, h55)
    i175 = Instruction(h29, h4)
 
   #--------------3 parte------------------ 
    
    i176 = Instruction(h1, h2)
    i177 = Instruction(h5, h3)
    i178 = Instruction(h2, h1)
    i179 = Instruction(h3, h4)
    i180 = Instruction(h3, h30)
    i181 = Instruction(h2, h1)
    
    i182 = Instruction(h1, h2)
    i183 = Instruction(h6, h3)
    i184 = Instruction(h2, h1)
    i185 = Instruction(h3, h4)
    i186 = Instruction(h3, h31)
    i187 = Instruction(h2, h1)
    
    i188 = Instruction(h1, h2)
    i189 = Instruction(h7, h3)
    i190 = Instruction(h2, h1)
    i191 = Instruction(h3, h4)
    i192 = Instruction(h3, h32)
    i193 = Instruction(h2, h1)

    i194 = Instruction(h1, h2)
    i195 = Instruction(h8, h3)
    i196 = Instruction(h2, h1)
    i197 = Instruction(h3, h4)
    i198 = Instruction(h3, h33)
    i199 = Instruction(h2, h1)
    
    i200 = Instruction(h1, h2)
    i201 = Instruction(h9, h3)
    i202 = Instruction(h2, h1)
    i203 = Instruction(h3, h4)
    i204 = Instruction(h3, h34)
    i205 = Instruction(h2, h1)
    
    i206 = Instruction(h1, h2)
    i207 = Instruction(h10, h3)
    i208 = Instruction(h2, h1)
    i209 = Instruction(h3, h4)
    i210 = Instruction(h3, h35)
    i211 = Instruction(h2, h1)
    
    i212 = Instruction(h1, h2)
    i213 = Instruction(h11, h3)
    i214 = Instruction(h2, h1)
    i215 = Instruction(h3, h4)
    i216 = Instruction(h3, h36)
    i217 = Instruction(h2, h1)
    
    i218 = Instruction(h1, h2)
    i219 = Instruction(h12, h3)
    i220 = Instruction(h2, h1)
    i221 = Instruction(h3, h4)
    i222 = Instruction(h3, h37)
    i223 = Instruction(h2, h1)

    i224 = Instruction(h1, h2)
    i225 = Instruction(h13, h3)
    i226 = Instruction(h2, h1)
    i227 = Instruction(h3, h4)
    i228 = Instruction(h3, h38)
    i229 = Instruction(h2, h1)
    
    i230 = Instruction(h1, h2)
    i231 = Instruction(h14, h3)
    i232 = Instruction(h2, h1)
    i233 = Instruction(h3, h4)
    i234 = Instruction(h3, h39)
    i235 = Instruction(h2, h1)
    
    i236 = Instruction(h1, h2)
    i237 = Instruction(h15, h3)
    i238 = Instruction(h2, h1)
    i239 = Instruction(h3, h4)
    i240 = Instruction(h3, h40)
    i241 = Instruction(h2, h1)
    
    i242 = Instruction(h1, h2)
    i243 = Instruction(h16, h3)
    i244 = Instruction(h2, h1)
    i245 = Instruction(h3, h4)
    i246 = Instruction(h3, h41)
    i247 = Instruction(h2, h1)
    
    i248 = Instruction(h1, h2)
    i249 = Instruction(h17, h3)
    i250 = Instruction(h2, h1)
    i251 = Instruction(h3, h4)
    i252 = Instruction(h3, h42)
    i253 = Instruction(h2, h1)

    i254 = Instruction(h1, h2)
    i255 = Instruction(h18, h3)
    i256 = Instruction(h2, h1)
    i257 = Instruction(h3, h4)
    i258 = Instruction(h3, h43)
    i259 = Instruction(h2, h1)
    
    i260 = Instruction(h1, h2)
    i261 = Instruction(h19, h3)
    i262 = Instruction(h2, h1)
    i263 = Instruction(h3, h4)
    i264 = Instruction(h3, h44)
    i265 = Instruction(h2, h1)
    
    i266 = Instruction(h1, h2)
    i267 = Instruction(h20, h3)
    i268 = Instruction(h2, h1)
    i269 = Instruction(h3, h4)
    i270 = Instruction(h3, h45)
    i271 = Instruction(h2, h1)
    
    i272 = Instruction(h1, h2)
    i273 = Instruction(h21, h3)
    i274 = Instruction(h2, h1)
    i275 = Instruction(h3, h4)
    i276 = Instruction(h3, h46)
    i277 = Instruction(h2, h1)
    
    i278 = Instruction(h1, h2)
    i279 = Instruction(h22, h3)
    i280 = Instruction(h2, h1)
    i281 = Instruction(h3, h4)
    i282 = Instruction(h3, h47)
    i283 = Instruction(h2, h1)

    i284 = Instruction(h1, h2)
    i285 = Instruction(h23, h3)
    i286 = Instruction(h2, h1)
    i287 = Instruction(h3, h4)
    i288 = Instruction(h3, h48)
    i289 = Instruction(h2, h1)
    
    i290 = Instruction(h1, h2)
    i291 = Instruction(h24, h3)
    i292 = Instruction(h2, h1)
    i293 = Instruction(h3, h4)
    i294 = Instruction(h3, h49)
    i295 = Instruction(h2, h1)
    
    i296 = Instruction(h1, h2)
    i297 = Instruction(h25, h3)
    i298 = Instruction(h2, h1)
    i299 = Instruction(h3, h4)
    i300 = Instruction(h3, h50)
    i301 = Instruction(h2, h1)
    
    i302 = Instruction(h1, h2)
    i303 = Instruction(h26, h3)
    i304 = Instruction(h2, h1)
    i305 = Instruction(h3, h4)
    i306 = Instruction(h3, h51)
    i307 = Instruction(h2, h1)
    
    i308 = Instruction(h1, h2)
    i309 = Instruction(h27, h3)
    i310 = Instruction(h2, h1)
    i311 = Instruction(h3, h4)
    i312 = Instruction(h3, h52)
    i313 = Instruction(h2, h1)

    i314 = Instruction(h1, h2)
    i315 = Instruction(h28, h3)
    i316 = Instruction(h2, h1)
    i317 = Instruction(h3, h4)
    i318 = Instruction(h3, h53)
    i319 = Instruction(h2, h1)
    
    i320 = Instruction(h1, h2)
    i321 = Instruction(h29, h3)
    i322 = Instruction(h2, h1)
    i323 = Instruction(h3, h4)
    i324 = Instruction(h3, h54)
    i325 = Instruction(h2, h1)
    
    i326 = Instruction(None,None)

     
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,
                    i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,
                    i41,i42,i43,i44,i45,i46,i47,i48,i49,i50,i51,i52,i53,i54,i55,i56,i57,i58,i59,i60,
                    i61,i62,i63,i64,i65,i66,i67,i68,i69,i70,i71,i72,i73,i74,i75,i76,i77,i78,i79,i80,
                    i81,i82,i83,i84,i85,i86,i87,i88,i89,i90,i91,i92,i93,i94,i95,i96,i97,i98,i99,i100,
                    
                    i101,i102,i103,i104,i105,i106,i107,i108,i109,i110,i111,i112,i113,i114,i115,i116,i117,i118,i119,i120,
                    i121,i122,i123,i124,i125,i126,i127,i128,i129,i130,i131,i132,i133,i134,i135,i136,i137,i138,i139,i140,
                    i141,i142,i143,i144,i145,i146,i147,i148,i149,i150,i151,i152,i153,i154,i155,i156,i157,i158,i159,i160,
                    i161,i162,i163,i164,i165,i166,i167,i168,i169,i170,i171,i172,i173,i174,i175,i176,i177,i178,i179,i180,
                    i181,i182,i183,i184,i185,i186,i187,i188,i189,i190,i191,i192,i193,i194,i195,i196,i197,i198,i199,i200,
                    
                    i201,i202,i203,i204,i205,i206,i207,i208,i209,i210,i211,i212,i213,i214,i215,i216,i217,i218,i219,i220,
                    i221,i222,i223,i224,i225,i226,i227,i228,i229,i230,i231,i232,i233,i234,i235,i236,i237,i238,i239,i240,
                    i241,i242,i243,i244,i245,i246,i247,i248,i249,i250,i251,i252,i253,i254,i255,i256,i257,i258,i259,i260,
                    i261,i262,i263,i264,i265,i266,i267,i268,i269,i270,i271,i272,i273,i274,i275,i276,i277,i278,i279,i280,
                    i281,i282,i283,i284,i285,i286,i287,i288,i289,i290,i291,i292,i293,i294,i295,i296,i297,i298,i299,i300,
                    
                    i301,i302,i303,i304,i305,i306,i307,i308,i309,i310,i311,i312,i313,i314,i315,i316,i317,i318,i319,i320,
                    i321,i322,i323,i324,i325,i326]
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),(i2,i3,2),(i3,i2,1),(i2,i4,1),
                               (i4,i4,2),(i4,i5,1),(i5,i6,2),(i6,i5,1),(i5,i7,1),
                               (i7,i7,2),(i7,i8,1),(i8,i9,2),(i9,i8,1),(i8,i10,1),
                               (i10,i10,2),(i10,i11,1),(i11,i12,2),(i12,i11,1),(i11,i13,1),
                               (i13,i13,2),(i13,i14,1),(i14,i15,2),(i15,i14,1),(i14,i16,1),
                               
                               (i16,i16,2),(i16,i17,1),(i17,i18,2),(i18,i17,1),(i17,i19,1),
                               (i19,i19,2),(i19,i20,1),(i20,i21,2),(i21,i20,1),(i20,i22,1),
                               (i22,i22,2),(i22,i23,1),(i23,i24,2),(i24,i23,1),(i23,i25,1),
                               (i25,i25,2),(i25,i26,1),(i26,i27,2),(i27,i26,1),(i26,i28,1),
                               (i28,i28,2),(i28,i29,1),(i29,i30,2),(i30,i29,1),(i29,i31,1),
                               
                               (i31,i31,2),(i31,i32,1),(i32,i33,2),(i33,i32,1),(i32,i34,1),
                               (i34,i34,2),(i34,i35,1),(i35,i36,2),(i36,i35,1),(i35,i37,1),
                               (i37,i37,2),(i37,i38,1),(i38,i39,2),(i39,i38,1),(i38,i40,1),
                               (i40,i40,2),(i40,i41,1),(i41,i42,2),(i42,i41,1),(i41,i43,1),
                               (i43,i43,2),(i43,i44,1),(i44,i45,2),(i45,i44,1),(i44,i46,1),
                               
                               (i46,i46,2),(i46,i47,1),(i47,i48,2),(i48,i47,1),(i47,i49,1),
                               (i49,i49,2),(i49,i50,1),(i50,i51,2),(i51,i50,1),(i50,i52,1),
                               (i52,i52,2),(i52,i53,1),(i53,i54,2),(i54,i53,1),(i53,i55,1),
                               (i55,i55,2),(i55,i56,1),(i56,i57,2),(i57,i56,1),(i56,i58,1),
                               (i58,i58,2),(i58,i59,1),(i59,i60,2),(i60,i59,1),(i59,i61,1),
                               
                               (i61,i61,2),(i61,i62,1),(i62,i63,2),(i63,i62,1),(i62,i64,1),
                               (i64,i64,2),(i64,i65,1),(i65,i66,2),(i66,i65,1),(i65,i67,1),
                               (i67,i67,2),(i67,i68,1),(i68,i69,2),(i69,i68,1),(i68,i70,1),
                               (i70,i70,2),(i70,i71,1),(i71,i72,2),(i72,i71,1),(i71,i73,1),
                               (i73,i73,2),(i73,i74,1),(i74,i75,2),(i75,i74,1),(i74,i76,1),
                              
                               #La segunda parte que resta la clave
                              (i76,i76,2),(i76,i77,1),(i77,i78,2),(i78,i79,1),(i79,i77,1),(i77,i80,1),
                              (i80,i80,2),(i80,i81,1),(i81,i82,2),(i82,i83,1),(i83,i81,1),(i81,i84,1),
                              (i84,i84,2),(i84,i85,1),(i85,i86,2),(i86,i87,1),(i87,i85,1),(i85,i88,1),
                              (i88,i88,2),(i88,i89,1),(i89,i90,2),(i90,i91,1),(i91,i89,1),(i89,i92,1),
                              (i92,i92,2),(i92,i93,1),(i93,i94,2),(i94,i95,1),(i95,i93,1),(i93,i96,1),
                               
                              (i96,i96,2),(i96,i97,1),(i97,i98,2),(i98,i99,1),(i99,i97,1),(i97,i100,1),
                              (i100,i100,2),(i100,i101,1),(i101,i102,2),(i102,i103,1),(i103,i101,1),(i101,i104,1),
                              (i104,i104,2),(i104,i105,1),(i105,i106,2),(i106,i107,1),(i107,i105,1),(i105,i108,1),
                              (i108,i108,2),(i108,i109,1),(i109,i110,2),(i110,i111,1),(i111,i109,1),(i109,i112,1),
                              (i112,i112,2),(i112,i113,1),(i113,i114,2),(i114,i115,1),(i115,i113,1),(i113,i116,1),
                               
                              (i116,i116,2),(i116,i117,1),(i117,i118,2),(i118,i119,1),(i119,i117,1),(i117,i120,1),
                              (i120,i120,2),(i120,i121,1),(i121,i122,2),(i122,i123,1),(i123,i121,1),(i121,i124,1),
                              (i124,i124,2),(i124,i125,1),(i125,i126,2),(i126,i127,1),(i127,i125,1),(i125,i128,1),
                              (i128,i128,2),(i128,i129,1),(i129,i130,2),(i130,i131,1),(i131,i129,1),(i129,i132,1),
                              (i132,i132,2),(i132,i133,1),(i133,i134,2),(i134,i135,1),(i135,i133,1),(i133,i136,1),
                               
                              (i136,i136,2),(i136,i137,1),(i137,i138,2),(i138,i139,1),(i139,i137,1),(i137,i140,1),
                              (i140,i140,2),(i140,i141,1),(i141,i142,2),(i142,i143,1),(i143,i141,1),(i141,i144,1),
                              (i144,i144,2),(i144,i145,1),(i145,i146,2),(i146,i147,1),(i147,i145,1),(i145,i148,1),
                              (i148,i148,2),(i148,i149,1),(i149,i150,2),(i150,i151,1),(i151,i149,1),(i149,i152,1),
                              (i152,i152,2),(i152,i153,1),(i153,i154,2),(i154,i155,1),(i155,i153,1),(i153,i156,1),
                            
                              (i156,i156,2),(i156,i157,1),(i157,i158,2),(i158,i159,1),(i159,i157,1),(i157,i160,1),
                              (i160,i160,2),(i160,i161,1),(i161,i162,2),(i162,i163,1),(i163,i161,1),(i161,i164,1),
                              (i164,i164,2),(i164,i165,1),(i165,i166,2),(i166,i167,1),(i167,i165,1),(i165,i168,1),
                              (i168,i168,2),(i168,i169,1),(i169,i170,2),(i170,i171,1),(i171,i169,1),(i169,i172,1),
                              (i172,i172,2),(i172,i173,1),(i173,i174,2),(i174,i175,1),(i175,i173,1),(i173,i176,1),
                               
                            #A continuación la tecera parte que aplica módulo a la resta
                           (i176,i177,2),(i177,i176,2),(i176,i178,1),(i178,i176,1),(i178,i179,2),
                           (i179,i178,1),(i177,i180,1),(i180,i180,2),(i180,i181,1),(i181,i181,2),(i181,i182,1),
                           (i182,i183,2),(i183,i182,2),(i182,i184,1),(i184,i182,1),(i184,i185,2),
                           (i185,i184,1),(i183,i186,1),(i186,i186,2),(i186,i187,1),(i187,i187,2),(i187,i188,1),
                           (i188,i189,2),(i189,i188,2),(i188,i190,1),(i190,i188,1),(i190,i191,2),
                           (i191,i190,1),(i189,i192,1),(i192,i192,2),(i192,i193,1),(i193,i193,2),(i193,i194,1), 
                           (i194,i195,2),(i195,i194,2),(i194,i196,1),(i196,i194,1),(i196,i197,2),
                           (i197,i196,1),(i195,i198,1),(i198,i198,2),(i198,i199,1),(i199,i199,2),(i199,i200,1),
                           (i200,i201,2),(i201,i200,2),(i200,i202,1),(i202,i200,1),(i202,i203,2),
                           (i203,i202,1),(i201,i204,1),(i204,i204,2),(i204,i205,1),(i205,i205,2),(i205,i206,1),
                               
                           (i206,i207,2),(i207,i206,2),(i206,i208,1),(i208,i206,1),(i208,i209,2),
                           (i209,i208,1),(i207,i210,1),(i210,i210,2),(i210,i211,1),(i211,i211,2),(i211,i212,1),
                           (i212,i213,2),(i213,i212,2),(i212,i214,1),(i214,i212,1),(i214,i215,2),
                           (i215,i214,1),(i213,i216,1),(i216,i216,2),(i216,i217,1),(i217,i217,2),(i217,i218,1),
                           (i218,i219,2),(i219,i218,2),(i218,i220,1),(i220,i218,1),(i220,i221,2),
                           (i221,i220,1),(i219,i222,1),(i222,i222,2),(i222,i223,1),(i223,i223,2),(i223,i224,1), 
                           (i224,i225,2),(i225,i224,2),(i224,i226,1),(i226,i224,1),(i226,i227,2),
                           (i227,i226,1),(i225,i228,1),(i228,i228,2),(i228,i229,1),(i229,i229,2),(i229,i230,1),
                           (i230,i231,2),(i231,i230,2),(i230,i232,1),(i232,i230,1),(i232,i233,2),
                           (i233,i232,1),(i231,i234,1),(i234,i234,2),(i234,i235,1),(i235,i235,2),(i235,i236,1),
                               
                           (i236,i237,2),(i237,i236,2),(i236,i238,1),(i238,i236,1),(i238,i239,2),
                           (i239,i238,1),(i237,i240,1),(i240,i240,2),(i240,i241,1),(i241,i241,2),(i241,i242,1),
                           (i242,i243,2),(i243,i242,2),(i242,i244,1),(i244,i242,1),(i244,i245,2),
                           (i245,i244,1),(i243,i246,1),(i246,i246,2),(i246,i247,1),(i247,i247,2),(i247,i248,1),
                           (i248,i249,2),(i249,i248,2),(i248,i250,1),(i250,i248,1),(i250,i251,2),
                           (i251,i250,1),(i249,i252,1),(i252,i252,2),(i252,i253,1),(i253,i253,2),(i253,i254,1), 
                           (i254,i255,2),(i255,i254,2),(i254,i256,1),(i256,i254,1),(i256,i257,2),
                           (i257,i256,1),(i255,i258,1),(i258,i258,2),(i258,i259,1),(i259,i259,2),(i259,i260,1),
                           (i260,i261,2),(i261,i260,2),(i260,i262,1),(i262,i260,1),(i262,i263,2),
                           (i263,i262,1),(i261,i264,1),(i264,i264,2),(i264,i265,1),(i265,i265,2),(i265,i266,1),
                               
                           (i266,i267,2),(i267,i266,2),(i266,i268,1),(i268,i266,1),(i268,i269,2),
                           (i269,i268,1),(i267,i270,1),(i270,i270,2),(i270,i271,1),(i271,i271,2),(i271,i272,1),
                           (i272,i273,2),(i273,i272,2),(i272,i274,1),(i274,i272,1),(i274,i275,2),
                           (i275,i274,1),(i273,i276,1),(i276,i276,2),(i276,i277,1),(i277,i277,2),(i277,i278,1),
                           (i278,i279,2),(i279,i278,2),(i278,i280,1),(i280,i278,1),(i280,i281,2),
                           (i281,i280,1),(i279,i282,1),(i282,i282,2),(i282,i283,1),(i283,i283,2),(i283,i284,1), 
                           (i284,i285,2),(i285,i284,2),(i284,i286,1),(i286,i284,1),(i286,i287,2),
                           (i287,i286,1),(i285,i288,1),(i288,i288,2),(i288,i289,1),(i289,i289,2),(i289,i290,1),
                           (i290,i291,2),(i291,i290,2),(i290,i292,1),(i292,i290,1),(i292,i293,2),
                           (i293,i292,1),(i291,i294,1),(i294,i294,2),(i294,i295,1),(i295,i295,2),(i295,i296,1),
                               
                           (i296,i297,2),(i297,i296,2),(i296,i298,1),(i298,i296,1),(i298,i299,2),
                           (i299,i298,1),(i297,i300,1),(i300,i300,2),(i300,i301,1),(i301,i301,2),(i301,i302,1),
                           (i302,i303,2),(i303,i302,2),(i302,i304,1),(i304,i302,1),(i304,i305,2),
                           (i305,i304,1),(i303,i306,1),(i306,i306,2),(i306,i307,1),(i307,i307,2),(i307,i308,1),
                           (i308,i309,2),(i309,i308,2),(i308,i310,1),(i310,i308,1),(i310,i311,2),
                           (i311,i310,1),(i309,i312,1),(i312,i312,2),(i312,i313,1),(i313,i313,2),(i313,i314,1), 
                           (i314,i315,2),(i315,i314,2),(i314,i316,1),(i316,i314,1),(i316,i317,2),
                           (i317,i316,1),(i315,i318,1),(i318,i318,2),(i318,i319,1),(i319,i319,2),(i319,i320,1),
                           (i320,i321,2),(i321,i320,2),(i320,i322,1),(i322,i320,1),(i322,i323,2),
                           (i323,i322,1),(i321,i324,1),(i324,i324,2),(i324,i325,1),(i325,i325,2),(i325,i326,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm