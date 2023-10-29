from host import Host
from instruction import Instruction
from virusmachine import VirusMachine

def FirmaDSA(p,q,g,y,hm,x):
    
    h1 = Host(p)
    h2 = Host(q)
    h3 = Host(g)
    h4 = Host(y)
    h5 = Host(hm)
    h6 = Host(x)
    h7 = Host()
    h8 = Host()
    h9 = Host()
    h10 = Host()    
    h11 = Host()
    h12 = Host(1)
    h13 = Host(1)
    h14 = Host()
    h15 = Host()
    h16 = Host()
    h17 = Host()  
    h18 = Host()
    h19 = Host(1)
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,
             h11,h12,h13,h14,h15,h16,h17,h18,h19,env]
    
    i1 = Instruction(h11, h12)
    i2 = Instruction(h12, h11,2)
    i3 = Instruction(h11, h14)
    i4 = Instruction(h13, h15)
    i5 = Instruction(h14, h17)
    i6 = Instruction(h15, h13)
    i7 = Instruction(h15, h13)
    i8 = Instruction(h11, h14)
    i9 = Instruction(h14, h16)
    i10 = Instruction(h2, h15)
    i11 = Instruction(h2, h15)
    i12 = Instruction(h14, h16)
    i13 = Instruction(h15, h2)
    i14 = Instruction(h16, h17)
    i15 = Instruction(h16, h7)
    i16 = Instruction(h15, h2)
    i17 = Instruction(h7,h10)
    i18 = Instruction(h14,h17)
    i19 = Instruction(h12,h14)
    i20 = Instruction(h3,h11,2)
    i21 = Instruction(h11,h3)
    i22 = Instruction(h11,h15)
    i23 = Instruction(h15,h17)
    i24 = Instruction(h14,h11,2)
    i25 = Instruction(h11,h14)
    i26 = Instruction(h11,h12)
    i27 = Instruction(h1,h15)
    i28 = Instruction(h12,h11)
    i29 = Instruction(h15,h1)
    i30 = Instruction(h11,h17)
    i31 = Instruction(h15,h1) 
    i32 = Instruction(h11,h12)
    i33 = Instruction(h2,h15)
    i34 = Instruction(h12,h11)
    i35 = Instruction(h15,h2)
    i36 = Instruction(h11,h17)      
    i37 = Instruction(h11,h8)
    i38 = Instruction(h15,h2)
    i39 = Instruction(h14,h17)
    i40 = Instruction(h10, h14,2)
    i41 = Instruction(h19, h16,2)
    i42 = Instruction(h14, h10)      
    i43 = Instruction(h14, h11)
    i44 = Instruction(h16, h19)
    i45 = Instruction(h16, h12)
    i46 = Instruction(h11, h17)
    i47 = Instruction(h12, h16,2)      
    i48 = Instruction(h16, h12)
    i49 = Instruction(h16, h14)
    i50 = Instruction(h2, h15)
    i51 = Instruction(h14, h11)
    i52 = Instruction(h15, h2)      
    i53 = Instruction(h11, h17)
    i54 = Instruction(h11, h16)
    i55 = Instruction(h15, h2)
    i56 = Instruction(h13, h11, 2)
    i57 = Instruction(h11, h13)
    i58 = Instruction(h11, h17)      
    i59 = Instruction(h16, h17)
    i60 = Instruction(h16, h17)
    i61 = Instruction(h19, h18)
    i62 = Instruction(None, None)
    i63 = Instruction(h12, h17)
    i64 = Instruction(h16, h17)
    i65 = Instruction(h13, h11, 2)      
    i66 = Instruction(h11, h19)
    i67 = Instruction(h11, h13)
    i68 = Instruction(h13,h17)
    i69 = Instruction(h12,h17)  
    i70 = Instruction(h6, h17)
    i71 = Instruction(h8, h11, 2)
    i72 = Instruction(h11, h8)
    i73 = Instruction(h11, h5) 
    i74 = Instruction(h18, h17)
    i75 = Instruction(h5, h11, 2)
    i76 = Instruction(h11, h5)
    i77 = Instruction(h11, h6)
    i78 = Instruction(h2, h18) 
    i79 = Instruction(h6, h11)
    i80 = Instruction(h18, h2)
    i81 = Instruction(h11, h17)
    i82 = Instruction(h11, h9)
    i83 = Instruction(h18, h2)
    i84 = Instruction(h5, h17)
    
      
   
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,
                    i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,
                    i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,
                    i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,
                    i41,i42,i43,i44,i45,i46,i47,i48,i49,i50,
                    i51,i52,i53,i54,i55,i56,i57,i58,i59,i60,
                    i61,i62,i63,i64,i65,i66,i67,i68,i69,i70,
                    i71,i72,i73,i74,i75,i76,i77,i78,i79,i80,
                    i81,i82,i83,i84]
    
    instruction_connections = [(i1,i2,1),(i2,i1,1),(i1,i3,1),(i3,i5,1),
                        (i3,i4,2),(i4,i3,2),(i5,i6,1),(i6,i1,1),
                        (i4,i7,1),(i7,i8,1),(i8,i8,2),(i8,i9,1),
                        (i9,i10,2),(i10,i9,2),(i9,i11,1),(i10,i12,1),
                        (i11,i12,1),(i12,i12,2),(i12,i13,1),(i13,i13,2),
                        (i13,i14,1),(i14,i14,2),(i14,i1,1),(i11,i15,2),
                        (i15,i15,2),(i15,i16,1),(i16,i16,2),(i16,i17,1),
                        (i17,i18,2),(i17,i27,1),(i18,i18,2),(i18,i19,1),
                        (i19,i19,2),(i19,i20,1),(i20,i20,2),(i20,i21,1),
                        (i21,i22,2),(i21,i23,1),(i22,i21,1),(i23,i24,2),
                        (i23,i17,1),(i24,i24,2),(i24,i25,1),(i25,i26,2),
                        (i25,i23,1),(i26,i25,1),(i27,i28,2),(i28,i27,2),
                        (i27,i29,1),(i29,i27,1),(i29,i30,2),(i30,i29,1),
                        (i28,i31,1),(i31,i31,2),(i31,i32,1),(i32,i32,2),
                        (i32,i33,1),(i33,i34,2),(i34,i33,2),(i33,i35,1),
                        (i35,i33,1),(i35,i36,2),(i36,i35,1),(i34,i37,1),
                        (i37,i37,2),(i37,i38,1),(i38,i38,2),(i38,i39,1), 
                        (i39,i39,2),(i39,i40,1),(i40,i40,2),(i40,i41,1),
                        (i41,i41,2),(i41,i42,1),(i42,i43,2),(i43,i42,2),
                        (i42,i44,1),(i44,i45,2),(i45,i44,2),(i44,i46,1),
                        (i46,i47,2),(i47,i47,2),(i47,i48,1),(i48,i49,1),
                        (i49,i48,2),(i49,i46,1),(i46,i50,1),(i50,i51,2),
                        (i51,i50,2),(i50,i52,1),(i52,i50,1),(i52,i53,2),
                        (i53,i52,1),(i51,i54,1),(i54,i54,2),(i54,i55,1),
                        (i55,i55,2),(i55,i56,1),(i56,i57,1),(i57,i58,1),
                        (i58,i59,2),(i59,i58,2),(i59,i63,1),(i58,i60,1),
                        (i60,i61,1),(i61,i61,2),(i60,i63,2),(i63,i63,2),
                        (i63,i64,1),(i64,i64,2),(i64,i65,1),(i65,i66,1),
                        (i66,i67,1),(i67,i40,1),(i61,i68,1),(i68,i68,2),
                        (i68,i69,1),(i69,i69,2),(i69,i70,1),(i70,i71,2),
                        (i71,i71,2),(i71,i72,1),(i72,i73,1),(i73,i72,2),
                        (i73,i70,1),(i70,i74,1),(i74,i75,2),(i75,i75,2),
                        (i75,i76,1),(i76,i77,1),(i77,i76,2),(i77,i74,1),
                        (i74,i78,1),(i78,i79,2),(i79,i78,2),(i78,i80,1),
                        (i80,i78,1),(i80,i81,2),(i81,i80,1),(i79,i82,1),
                        (i82,i82,2),(i82,i83,1),(i83,i83,2),(i83,i84,1),
                        (i84,i84,2),(i84,i62,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections, True)

    return vm

