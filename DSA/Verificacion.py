from host import Host
from instruction import Instruction
from virusmachine import VirusMachine
from modulosAux import Inverso

def VerificacionDSA(p,q,g,y,hm,r,s):
    
    vm = Inverso(s,q)
    sol=vm.compute()
    w=sol[1][-1]
    
    h1 = Host(p)
    h2 = Host(q)
    h3 = Host(g)
    h4 = Host(y)
    h5 = Host(hm)
    h6 = Host(r)
    h7 = Host(w)
    h8 = Host()
    h9 = Host()
    h10 = Host()
    
    h11 = Host()
    h12 = Host()
    h13 = Host()
    h14 = Host(1)
    h15 = Host(1)
    h16 = Host(1)
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,
             h11,h12,h13,h14,h15,h16,env]
    
    i1 = Instruction(h5, h11)
    i2 = Instruction(h7, h12, 2)
    i3 = Instruction(h12, h7)
    i4 = Instruction(h12, h13)   
    
    i5 = Instruction(h2,h5)
    i6 = Instruction(h13,h12)
    i7 = Instruction(h5,h2)
    i8 = Instruction(h12,h11)
    i9 = Instruction(h12,h8) 
    i10 = Instruction(h5, h2)
    
    i11 = Instruction(h7, h11)
    i12 = Instruction(h6, h12, 2)
    i13 = Instruction(h12, h6)
    i14 = Instruction(h12, h13)   
    
    i15 = Instruction(h2,h7)
    i16 = Instruction(h13,h12)
    i17 = Instruction(h7,h2)
    i18 = Instruction(h12,h11)
    i19 = Instruction(h12,h9) 
    i20 = Instruction(h7, h2)
     
    i21 = Instruction(h8,h11)
    i22 = Instruction(h7,h11)
    i23 = Instruction(h14,h7)
    i24 = Instruction(h3,h5,2)
    i25 = Instruction(h5,h3)
    i26 = Instruction(h5,h12)
    i27 = Instruction(h12,h11)
    i28 = Instruction(h7,h5,2)
    i29 = Instruction(h5,h7)
    i30 = Instruction(h5,h14)
    i31 = Instruction(h14,h13)
    
    i32 = Instruction(h15,h14)
    i33 = Instruction(h13,h15)
    
    i34 = Instruction(h9,h11)
    i35 = Instruction(h7,h11)
    i36 = Instruction(h14,h7)
    i37 = Instruction(h4,h5,2)
    i38 = Instruction(h5,h4)
    i39 = Instruction(h5,h12)
    i40 = Instruction(h12,h11)
    i41 = Instruction(h7,h5,2)
    i42 = Instruction(h5,h7)
    i43 = Instruction(h5,h14)
    i44 = Instruction(h14,h13)
    
    i45 = Instruction(h15,h11)
    i46 = Instruction(h13,h5,2)
    i47 = Instruction(h5,h13)
    i48 = Instruction(h5,h14)
    
    i49 = Instruction(h1,h12)
    i50 = Instruction(h14,h5)
    i51 = Instruction(h12,h1)
    i52 = Instruction(h5,h11)
    i53 = Instruction(h12,h1)
     
    i54 = Instruction(h5,h14)

    i55 = Instruction(h2,h12)
    i56 = Instruction(h14,h5)
    i57 = Instruction(h12,h2)
    i58 = Instruction(h5,h11)    
    i59 = Instruction(h12,h2)
    
    i60 = Instruction(h5,h10)
    i61 = Instruction(h7,h11)
    i62 = Instruction(h13,h11)
     
    i63 = Instruction(h10, h16)
    i64 = Instruction(h6, h16)
    i65 = Instruction(h6, h16)
    i66 = Instruction(None, None)    
    i67 = Instruction(h16, env)
        
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,
                    i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,
                    i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,
                    i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,
                    i41,i42,i43,i44,i45,i46,i47,i48,i49,i50,
                    i51,i52,i53,i54,i55,i56,i57,i58,i59,i60,
                    i61,i62,i63,i64,i65,i66,i67]
    
    instruction_connections = [(i1,i2,2),(i2,i2,2),(i2,i3,1),(i3,i4,1),(i4,i3,2),(i4,i1,1),(i1,i5,1),                         
                              (i5,i6,2),(i6,i5,2),(i5,i7,1),(i7,i5,1),(i7,i8,2),(i8,i7,1),
                              (i6,i9,1),(i9,i9,2),(i9,i10,1),(i10,i10,2),(i10,i11,1),
                               
                              (i11,i12,2),(i12,i12,2),(i12,i13,1),(i13,i14,1),(i14,i13,2),(i14,i11,1),(i11,i15,1),                         
                              (i15,i16,2),(i16,i15,2),(i15,i17,1),(i17,i15,1),(i17,i18,2),(i18,i17,1),
                              (i16,i19,1),(i19,i19,2),(i19,i20,1),(i20,i20,2),(i20,i21,1),
                               
                                (i21,i22,2),(i21,i31,1),(i22,i22,2),(i22,i23,1),(i23,i23,2),(i23,i24,1),(i24,i24,2),(i24,i25,1),
                                (i25,i26,2),(i25,i27,1),(i26,i25,1),(i27,i28,2),(i27,i21,1),(i28,i28,2),(i28,i29,1),(i29,i30,2),
                                (i29,i27,1),(i30,i29,1),(i31,i31,2),(i31,i32,1),
                                (i32,i33,1),(i33,i33,2),(i33,i34,1),
                                (i34,i35,2),(i34,i44,1),(i35,i35,2),(i35,i36,1),(i36,i36,2),(i36,i37,1),(i37,i37,2),(i37,i38,1),
                                (i38,i39,2),(i38,i40,1),(i39,i38,1),(i40,i41,2),(i40,i34,1),(i41,i41,2),(i41,i42,1),(i42,i43,2),
                                (i42,i40,1),(i43,i42,1),(i44,i44,2),(i44,i45,1),
                                (i45,i46,2),(i46,i46,2),(i46,i47,1),(i47,i48,1),(i48,i47,2),(i48,i45,1),(i45,i49,1),
                                (i49,i50,2),(i50,i49,2),(i49,i51,1),(i51,i49,1),(i51,i52,2),(i52,i51,1),(i50,i53,1),
                                (i53,i53,2),(i53,i54,1),(i54,i54,2),(i54,i55,1),
                                (i55,i56,2),(i56,i55,2),(i55,i57,1),(i57,i55,1),(i57,i58,2),(i58,i57,1),(i56,i59,1),(i59,i59,2),
                                (i59,i60,1),(i60,i60,2),(i60,i61,1),(i61,i61,2),(i61,i62,1),(i62,i62,2),(i62,i63,1),
                                 
                                (i63,i64,2),(i64,i63,2),(i63,i65,1),(i65,i66,2),(i65,i67,1),(i64,i66,1)
    ]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm