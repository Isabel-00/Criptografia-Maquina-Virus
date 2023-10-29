from host import Host
from instruction import Instruction
from virusmachine import VirusMachine

def GeneracionClavesDSA(p,q,z):
    
    h1 = Host(p)
    h2 = Host(q)
    h3 = Host(z)
    h4 = Host()
    h5 = Host()
    h6 = Host()
    h7 = Host()
    h8 = Host()
    h9 = Host()
    h10 = Host(1)    
    h11 = Host(1)
    h12 = Host()
    h13 = Host()
    h14 = Host()
    h15 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,
             h11,h12,h13,h14,h15,env]
    
    
    i1 = Instruction(h1, h15)
    i2 = Instruction(h9, h10)
    i3 = Instruction(h10, h9,2)
    i4 = Instruction(h9, h12)
    i5 = Instruction(h11, h13)
    i6 = Instruction(h12, h8)
    i7 = Instruction(h13, h11)
    i8 = Instruction(h13, h11)
    i9 = Instruction(h9, h12)
    i10 = Instruction(h12, h14)
    i11 = Instruction(h1, h13)
    i12 = Instruction(h1, h13)
    i13 = Instruction(h12, h14)
    i14 = Instruction(h13, h1)
    i15 = Instruction(h14, h8)
    i16 = Instruction(h14, h4)
    i17 = Instruction(h13, h1)
    i18 = Instruction(h15, h1)
    
    i19 = Instruction(h2, h15)
    i20 = Instruction(h9, h10)
    i21 = Instruction(h10, h9,2)
    i22 = Instruction(h9, h12)
    i23 = Instruction(h11, h13)
    i24 = Instruction(h12, h8)
    i25 = Instruction(h13, h11)
    i26 = Instruction(h13, h11)
    i27 = Instruction(h9, h12)
    i28 = Instruction(h12, h14)
    i29 = Instruction(h2, h13)
    i30 = Instruction(h2, h13)
    i31 = Instruction(h12, h14)
    i32 = Instruction(h13, h2)
    i33 = Instruction(h14, h8)
    i34 = Instruction(h14, h7)
    i35 = Instruction(h13, h2)
    i36 = Instruction(h15, h2)
    
     
    i37 = Instruction(h3,h9)
    i38 = Instruction(h13,h8)
    i39 = Instruction(h10,h13)
    i40 = Instruction(h4,h12,2)
    i41 = Instruction(h12,h4)
    i42 = Instruction(h12,h14)
    i43 = Instruction(h14,h8)
    i44 = Instruction(h13,h12,2)
    i45 = Instruction(h12,h13)
    i46 = Instruction(h12,h10)
    i47 = Instruction(h1,h14) 
    i48 = Instruction(h10,h12)
    i49 = Instruction(h14,h1)
    i50 = Instruction(h12,h8)
    i51 = Instruction(h12,h5)
    i52 = Instruction(h14,h1)
    i53 = Instruction(h13,h8)
     
    i54 = Instruction(h7,h15)
    i55 = Instruction(h13,h8)
    i56 = Instruction(h11,h13)
    i57 = Instruction(h5,h12,2)
    i58 = Instruction(h12,h5)
    i59 = Instruction(h12,h14)
    i60 = Instruction(h14,h8)
    i61 = Instruction(h13,h12,2)
    i62 = Instruction(h12,h13)
    i63 = Instruction(h12,h11)
    i64 = Instruction(h1,h14) 
    i65 = Instruction(h11,h12)
    i66 = Instruction(h14,h1)
    i67 = Instruction(h12,h8)
    i68 = Instruction(h12,h6)
    i69 = Instruction(h14,h1)
    i70 = Instruction(h13,h8)
    i71 = Instruction(None, None)
    
      
   
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,
                    i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,
                    i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,
                    i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,
                    i41,i42,i43,i44,i45,i46,i47,i48,i49,i50,
                    i51,i52,i53,i54,i55,i56,i57,i58,i59,i60,
                    i61,i62,i63,i64,i65,i66,i67,i68,i69,i70,
                    i71]
    
    instruction_connections = [(i1,i2,1),(i2,i3,1),(i3,i2,1),(i2,i4,1),(i4,i6,1),
                        (i4,i5,2),(i5,i4,2),(i6,i7,1),(i7,i2,1),
                        (i5,i8,1),(i8,i9,1),(i9,i9,2),(i9,i10,1),
                        (i10,i11,2),(i11,i10,2),(i10,i12,1),(i11,i13,1),
                        (i12,i13,1),(i13,i13,2),(i13,i14,1),(i14,i14,2),
                        (i14,i15,1),(i15,i15,2),(i15,i2,1),(i12,i16,2),
                        (i16,i16,2),(i16,i17,1),(i17,i17,2),(i17,i18,1),(i18,i19,1),
                               
                        (i19,i20,1),(i20,i21,1),(i21,i20,1),(i20,i22,1),(i22,i24,1),
                        (i22,i23,2),(i23,i22,2),(i24,i25,1),(i25,i20,1),
                        (i23,i26,1),(i26,i27,1),(i27,i27,2),(i27,i28,1),
                        (i28,i29,2),(i29,i28,2),(i28,i30,1),(i29,i31,1),
                        (i30,i31,1),(i31,i31,2),(i31,i32,1),(i32,i32,2),
                        (i32,i33,1),(i33,i33,2),(i33,i20,1),(i30,i34,2),
                        (i34,i34,2),(i34,i35,1),(i35,i35,2),(i35,i36,1),(i36,i37,1),
                              
                        (i37,i38,2),(i37,i47,1),(i38,i38,2),(i38,i39,1),
                        (i39,i39,2),(i39,i40,1),(i40,i40,2),(i40,i41,1),
                        (i41,i42,2),(i41,i43,1),(i42,i41,1),
                        (i43,i44,2),(i43,i37,1),(i44,i44,2),(i44,i45,1),
                        (i45,i46,2),(i45,i43,1),(i46,i45,1),
                        (i47,i48,2),(i48,i47,2),(i47,i49,1),(i49,i47,1),
                        (i49,i50,2),(i50,i49,1),(i48,i51,1),(i51,i51,2),
                        (i51,i52,1),(i52,i52,2),(i52,i53,1), (i53,i53,2),(i53,i54,1),
                               
                        
                        (i54,i55,2),(i54,i64,1),(i55,i55,2),(i55,i56,1),
                        (i56,i56,2),(i56,i57,1),(i57,i57,2),(i57,i58,1),
                        (i58,i59,2),(i58,i60,1),(i59,i58,1),
                        (i60,i61,2),(i60,i54,1),(i61,i61,2),(i61,i62,1),
                        (i62,i63,2),(i62,i60,1),(i63,i62,1),
                        (i64,i65,2),(i65,i64,2),(i64,i66,1),(i66,i64,1),
                        (i66,i67,2),(i67,i66,1),(i65,i68,1),(i68,i68,2),
                        (i68,i69,1),(i69,i69,2),(i69,i70,1), (i70,i70,2),(i70,i71,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections, True)

    return vm