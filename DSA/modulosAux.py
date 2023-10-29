from host import Host
from instruction import Instruction
from virusmachine import VirusMachine

def Suma(n1, n2):
    h1 = Host(n1)
    h2 = Host(n2)
    env = Host()
    
    hosts = [h1,h2,env]
    
    i1 = Instruction(h1, env)
    i2 = Instruction(h2, env)
    i3 = Instruction(None, None)
    
    instructions = [i1,i2,i3]
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),
                               (i2,i2,2),(i2,i3,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def Suma2(a, b):
    h1 = Host(a)
    h2 = Host(b)
    h3 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,env]
    
    i1 = Instruction(h2, h3, 2)
    i2 = Instruction(h3, env)
    i3 = Instruction(h3, h2)
    i4 = Instruction(h1, env)
    i5 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4,i5]
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),(i2,i3,2),
                               (i3,i2,2),(i2,i4,1),(i4,i4,2),
                               (i4,i5,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def Resta(n1, n2):
    h1 = Host(n1)
    h2 = Host(n2)
    h3 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,env]
     
    i1 = Instruction(h2, h3)
    i2 = Instruction(h1, h3)
    i3 = Instruction(h1, env)
    i4 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4]
    
    instruction_connections = [(i1,i2,2),(i2,i1,2),(i1,i3,1),
                               (i2,i4,1),(i3,i3,2),(i3,i4,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def Resta2(a, b):
    h1 = Host(a)
    h2 = Host(b)
    h3 = Host()
    h4 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,h4,env]
    
    i1 = Instruction(h2, h3, 2)
    i2 = Instruction(h3, h4)
    i3 = Instruction(h1, h4)
    i4 = Instruction(h3, h2)
    i5 = Instruction(h1, env)
    i6 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6]
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),(i2,i3,2),
                               (i3,i4,2),(i4,i2,1),(i2,i5,1),
                               (i5,i5,2),(i5,i6,1),(i3,i6,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def Multiplicacion(n1, n2):
    h1 = Host(n1)
    h2 = Host(n2)
    h3 = Host()
    h4 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,h4,env]
     
    i1 = Instruction(h1, h3)
    i2 = Instruction(h2, h4, 2)
    i3 = Instruction(h4, h2)
    i4 = Instruction(h4, env)    
    i5 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4,i5]
    
    instruction_connections = [(i1,i2,2),(i2,i2,2),(i2,i3,1),(i3,i4,1),
                               (i4,i3,2),(i4,i1,1),(i1,i5,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def Mod(n1, n2):  
    h1 = Host(n1)
    h2 = Host(n2)
    h3 = Host()
    h4 = Host()
    h5 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,env]
     
    i1 = Instruction(h2, h4)
    i2 = Instruction(h1, h3)
    i3 = Instruction(h4, h2)
    i4 = Instruction(h3, h5)
    i5 = Instruction(h3, env)
    i6 = Instruction(h4, h2)
    i7 = Instruction(None,None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7]
    
    instruction_connections = [(i1,i2,2),(i2,i1,2),(i1,i3,1),(i3,i1,1),
                               (i3,i4,2),(i4,i3,1),(i2,i5,1),(i5,i5,2),(i5,i6,1),(i6,i6,2),(i6,i7,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def Power(k, n):
    h1 = Host(k)
    h2 = Host(n)
    h3 = Host()
    h4 = Host()
    h5 = Host()
    h6 = Host(1)
    h7 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,env]
     
    i1 = Instruction(h2,h7)
    i2 = Instruction(h4,h7)
    i3 = Instruction(h6,h4)
    i4 = Instruction(h1,h3,2)
    i5 = Instruction(h3,h1)
    i6 = Instruction(h3,h5)
    i7 = Instruction(h5,h7)
    i8 = Instruction(h4,h3,2)
    i9 = Instruction(h3,h4)
    i10 = Instruction(h3,h6)
    i11 = Instruction(h6,env)
    i12 = Instruction(h4,h7)
    i13 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13]
    
    instruction_connections = [
        (i1,i2,2),(i1,i11,1),
        (i2,i2,2),(i2,i3,1),
        (i3,i3,2),(i3,i4,1),
        (i4,i4,2),(i4,i5,1),
        (i5,i6,2),(i5,i7,1),
        (i6,i5,1),
        (i7,i8,2),(i7,i1,1),
        (i8,i8,2),(i8,i9,1),
        (i9,i10,2),(i9,i7,1),
        (i10,i9,1),
        (i11,i11,2),(i11,i12,1),(i12,i12,2),(i12,i13,1)
        ]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def PowerMod(k, n, p):  
    h1 = Host(k)
    h2 = Host(n)
    h3 = Host()
    h4 = Host()
    h5 = Host()
    h6 = Host(1)
    h7 = Host()
    h8 = Host(p)
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,env]
     
    i1 = Instruction(h2,h7)
    i2 = Instruction(h4,h7)
    i3 = Instruction(h6,h4)
    i4 = Instruction(h1,h3,2)
    i5 = Instruction(h3,h1)
    i6 = Instruction(h3,h5)
    i7 = Instruction(h5,h7)
    i8 = Instruction(h4,h3,2)
    i9 = Instruction(h3,h4)
    i10 = Instruction(h3,h6)
    i11 = Instruction(h8,h5)
    i12 = Instruction(h6,h3)
    i13 = Instruction(h5,h8)
    i14 = Instruction(h3,h7)
    i15 = Instruction(h3,env)
    i16 = Instruction(h5,h8)
    i17 = Instruction(h4,h7)      
    i18 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18]
    
    instruction_connections = [
        (i1,i2,2),(i1,i11,1),
        (i2,i2,2),(i2,i3,1),
        (i3,i3,2),(i3,i4,1),
        (i4,i4,2),(i4,i5,1),
        (i5,i6,2),(i5,i7,1),
        (i6,i5,1),
        (i7,i8,2),(i7,i1,1),
        (i8,i8,2),(i8,i9,1),
        (i9,i10,2),(i9,i7,1),
        (i10,i9,1),
        
        (i11,i12,2),(i12,i11,2),
        (i11,i13,1),(i13,i11,1),
        (i13,i14,2),(i14,i13,1),
        (i12,i15,1),(i15,i15,2),
        (i15,i16,1),(i16,i16,2),(i16,i17,1), (i17,i17,2),(i17,i18,1)
        ]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def PowerModMod(k, n, p, q):  
    h1 = Host(k)
    h2 = Host(n)
    h3 = Host()
    h4 = Host()
    h5 = Host()
    h6 = Host(1)
    h7 = Host()
    h8 = Host(p)
    h9 = Host(q)
    h10 = Host()  
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,env]
     
    i1 = Instruction(h2,h10)
    i2 = Instruction(h4,h7)
    i3 = Instruction(h6,h4)
    i4 = Instruction(h1,h3,2)
    i5 = Instruction(h3,h1)
    i6 = Instruction(h3,h5)
    i7 = Instruction(h5,h7)
    i8 = Instruction(h4,h3,2)
    i9 = Instruction(h3,h4)
    
    i10 = Instruction(h3,h6)
    i11 = Instruction(h8,h5)
    i12 = Instruction(h6,h3)
    i13 = Instruction(h5,h8)
    i14 = Instruction(h3,h7)
    i15 = Instruction(h5,h8)
    
    i16 = Instruction(h3,h6)
    i17 = Instruction(h9,h5)
    i18 = Instruction(h6,h3)
    i19 = Instruction(h5,h9)
    i20 = Instruction(h3,h7)      
    i21 = Instruction(h3,env)
    i22 = Instruction(h5,h9)
    i23 = Instruction(h4,h7)
    
    i24 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24]
    
    instruction_connections = [
        (i1,i2,2),(i1,i11,1),
        (i2,i2,2),(i2,i3,1),
        (i3,i3,2),(i3,i4,1),
        (i4,i4,2),(i4,i5,1),
        (i5,i6,2),(i5,i7,1),
        (i6,i5,1),
        (i7,i8,2),(i7,i1,1),
        (i8,i8,2),(i8,i9,1),
        (i9,i10,2),(i9,i7,1),
        (i10,i9,1),
        
        (i11,i12,2),(i12,i11,2),
        (i11,i13,1),(i13,i11,1),
        (i13,i14,2),(i14,i13,1),
        (i12,i15,1),
        
        (i15,i15,2),(i15,i16,1),(i16,i16,2),(i16,i17,1),
        
        (i17,i18,2),(i18,i17,2),
        (i17,i19,1),(i19,i17,1),
        (i19,i20,2),(i20,i19,1),
        (i18,i21,1),(i21,i21,2),(i21,i22,1),(i22,i22,2),(i22,i23,1), (i23,i23,2),(i23,i24,1)
        ]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def MultMod(a, b, p):  
    h1 = Host(a)
    h2 = Host(b)
    h3 = Host()
    h4 = Host()
    h5 = Host()
    h6 = Host(p)
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,env]
     
    i1 = Instruction(h1, h3)
    i2 = Instruction(h2, h4, 2)
    i3 = Instruction(h4, h2)
    i4 = Instruction(h4, h5)   
    
    i5 = Instruction(h6,h1)
    i6 = Instruction(h5,h4)
    i7 = Instruction(h1,h6)
    i8 = Instruction(h4,h3)
    i9 = Instruction(h4,env) 
    i10 = Instruction(h1, h6)
    
    i11 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11]
    
    instruction_connections = [(i1,i2,2),(i2,i2,2),(i2,i3,1),(i3,i4,1),
                               (i4,i3,2),(i4,i1,1),(i1,i5,1),
                              
                              (i5,i6,2),(i6,i5,2),
                              (i5,i7,1),(i7,i5,1),
                              (i7,i8,2),(i8,i7,1),
                              (i6,i9,1),(i9,i9,2),(i9,i10,1),(i10,i10,2),(i10,i11,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def PowPowModMod(a, n1, b, n2, p, q):  
    h1 = Host(a)
    h2 = Host(n1)
    h3 = Host()
    h4 = Host()
    h5 = Host()
    h6 = Host(1)
    h7 = Host()
    h8 = Host(b)
    h9 = Host(n2)
    h10 = Host()
    h11 = Host(1)
    h12 = Host(p)
    h13 = Host(q)
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,env]
     
    i1 = Instruction(h2,h7)
    i2 = Instruction(h4,h7)
    i3 = Instruction(h6,h4)
    i4 = Instruction(h1,h3,2)
    i5 = Instruction(h3,h1)
    i6 = Instruction(h3,h5)
    i7 = Instruction(h5,h7)
    i8 = Instruction(h4,h3,2)
    i9 = Instruction(h3,h4)
    i10 = Instruction(h3,h6)
    i11 = Instruction(h6,h10)
    
    i12 = Instruction(h11,h6)
    i13 = Instruction(h10,h11)
    
    i14 = Instruction(h9,h7)
    i15 = Instruction(h4,h7)
    i16 = Instruction(h6,h4)
    i17 = Instruction(h8,h3,2)
    i18 = Instruction(h3,h8)
    i19 = Instruction(h3,h5)
    i20 = Instruction(h5,h7)
    i21 = Instruction(h4,h3,2)
    i22 = Instruction(h3,h4)
    i23 = Instruction(h3,h6)
    i24 = Instruction(h6,h10)
     
    i25 = Instruction(h11,h7)
    i26 = Instruction(h10,h3,2)
    i27 = Instruction(h3,h10)
    i28 = Instruction(h3,h6)
     
    i29 = Instruction(h12,h5)
    i30 = Instruction(h6,h3)
    i31 = Instruction(h5,h12)
    i32 = Instruction(h3,h7)
    i33 = Instruction(h5,h12)
     
    i34 = Instruction(h3,h6)
     
    i35 = Instruction(h13,h5)
    i36 = Instruction(h6,h3)
    i37 = Instruction(h5,h13)
    i38 = Instruction(h3,h7)    
    i39 = Instruction(h5,h13)
    
    i40 = Instruction(h3,env)
    i41 = Instruction(h4,h7)
    i42 = Instruction(h10,h7)  
    
    i43 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,
                    i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,
                    i21,i22,i23,i24,i25,i26,i27,i28,i29,i30,
                    i31,i32,i33,i34,i35,i36,i37,i38,i39,i40,
                   i41,i42,i43]
    
    instruction_connections = [
        (i1,i2,2),(i1,i11,1),(i2,i2,2),(i2,i3,1),(i3,i3,2),(i3,i4,1),(i4,i4,2),(i4,i5,1),
        (i5,i6,2),(i5,i7,1),(i6,i5,1),(i7,i8,2),(i7,i1,1),(i8,i8,2),(i8,i9,1),(i9,i10,2),
        (i9,i7,1),(i10,i9,1),(i11,i11,2),(i11,i12,1),
        (i12,i13,1),(i13,i13,2),(i13,i14,1),
        (i14,i15,2),(i14,i24,1),(i15,i15,2),(i15,i16,1),(i16,i16,2),(i16,i17,1),(i17,i17,2),(i17,i18,1),
        (i18,i19,2),(i18,i20,1),(i19,i18,1),(i20,i21,2),(i20,i14,1),(i21,i21,2),(i21,i22,1),(i22,i23,2),
        (i22,i20,1),(i23,i22,1),(i24,i24,2),(i24,i25,1),
        (i25,i26,2),(i26,i26,2),(i26,i27,1),(i27,i28,1),(i28,i27,2),(i28,i25,1),(i25,i29,1),
        
        (i29,i30,2),(i30,i29,2),(i29,i31,1),(i31,i29,1),(i31,i32,2),(i32,i31,1),(i30,i33,1),
        
        (i33,i33,2),(i33,i34,1),(i34,i34,2),(i34,i35,1),
        
        (i35,i36,2),(i36,i35,2),(i35,i37,1),(i37,i35,1),(i37,i38,2),(i38,i37,1),(i36,i39,1),(i39,i39,2),
        (i39,i40,1),(i40,i40,2),(i40,i41,1),(i41,i41,2),(i41,i42,1),(i42,i42,2),(i42,i43,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def Inverso(k,p):  
    h1 = Host(k)
    h2 = Host(1)
    h3 = Host(1)
    h4 = Host()
    h5 = Host()
    h6 = Host()
    h7 = Host()
    h8 = Host(p)
    h9 = Host()
    h10 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,env]
     
    i1 = Instruction(h1, h7,2)
    i2 = Instruction(h2, h10,2)
    i3 = Instruction(h7, h1)      
    i4 = Instruction(h7, h4)
    i5 = Instruction(h10, h2)
    i6 = Instruction(h10, h5)
     
    i7 = Instruction(h4, h6)
    i8 = Instruction(h5, h10,2)      
    i9 = Instruction(h10, h5)
    i10 = Instruction(h10, h7)
     
    i11 = Instruction(h8, h9)
    i12 = Instruction(h7, h4)
    i13 = Instruction(h9, h8)      
    i14 = Instruction(h4, h6)
    i15 = Instruction(h4, h10)
    i16 = Instruction(h9,h8)
     
    i17 = Instruction(h3, h4, 2)
    i18 = Instruction(h4, h3)
    i19 = Instruction(h4, h6)      
    i20 = Instruction(h10, h6)
    i21 = Instruction(h10, h6)
    i22 = Instruction(h2, env)
    
    i23 = Instruction(None, None)
     
    i24 = Instruction(h5, h6)
    i25 = Instruction(h10, h6)
    i26 = Instruction(h3, h4, 2)      
    i27 = Instruction(h4, h2)
    i28 = Instruction(h4, h3)
     
    i29 = Instruction(h3,h6)
    i30 = Instruction(h5,h6)
    
      
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17,i18,i19,i20,i21,i22,i23,i24,i25,i26,i27,i28,i29,i30]
    
    instruction_connections = [(i1,i1,2),(i1,i2,1),(i2,i2,2),(i2,i3,1),(i3,i4,2),(i4,i3,2),
                              (i3,i5,1),(i5,i6,2),(i6,i5,2),(i5,i7,1),
                              
                               (i7,i8,2),(i8,i8,2),(i8,i9,1),(i9,i10,1),(i10,i9,2),(i10,i7,1),(i7,i11,1),
                              
                               (i11,i12,2),(i12,i11,2),(i11,i13,1),(i13,i11,1),(i13,i14,2),(i14,i13,1),(i12,i15,1),
                              (i15,i15,2),(i15,i16,1),(i16,i16,2),(i16,i17,1),
                               
                               (i17,i18,1),(i18,i19,1),(i19,i20,2),(i20,i19,2),(i20,i24,1),(i19,i21,1),(i21,i22,1),
                              (i22,i22,2),(i21,i24,2),
                              
                              (i24,i24,2),(i24,i25,1),(i25,i25,2),(i25,i26,1),(i26,i27,1),(i27,i28,1),(i28,i1,1),
                              (i22,i29,1),(i29,i29,2),(i29,i30,1),(i30,i30,2),(i30,i23,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def ModInvmMult(x, r, hm, k, p):  
    
    vm = Inverso(k,p)
    sol=vm.compute(0)
    u=sol[1][-1]

    h1 = Host(x)
    h2 = Host(r)
    h3 = Host()
    h4 = Host()
    h5 = Host(hm)
    h6 = Host(u)
    h7 = Host(p)
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,env]
     
    i1 = Instruction(h1, h3)
    i2 = Instruction(h2, h4, 2)
    i3 = Instruction(h4, h2)
    i4 = Instruction(h4, h5) 
     
    i5 = Instruction(h6, h3)
    i6 = Instruction(h5, h4, 2)
    i7 = Instruction(h4, h5)
    i8 = Instruction(h4, h1)
     
    i9 = Instruction(h7, h6) 
    i10 = Instruction(h1, h4)
    i11 = Instruction(h6, h7)
    i12 = Instruction(h4, h3)
    i13 = Instruction(h4, env)
    i14 = Instruction(h6, h7)
    
    i15 = Instruction(h5, h3)
    i16 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16]
    
    instruction_connections = [(i1,i2,2),(i2,i2,2),(i2,i3,1),(i3,i4,1),
                               (i4,i3,2),(i4,i1,1),(i1,i5,1),
                              (i5,i6,2),(i6,i6,2),(i6,i7,1),(i7,i8,1),
                               (i8,i7,2),(i8,i5,1),(i5,i9,1),
                              (i9,i10,2),(i10,i9,2),(i9,i11,1),(i11,i9,1),(i11,i12,2),(i12,i11,1),(i10,i13,1),
                              (i13,i13,2),(i13,i14,1),(i14,i14,2),(i14,i15,1),(i15,i15,2),(i15,i16,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def GenNat():
    h1 = Host()
    h2 = Host(1)
    env = Host()
    
    hosts = [h1,h2,env]
     
    i1 = Instruction(h1, h2)
    i2 = Instruction(h2, h1, 2)
    i3 = Instruction(h1, env)    
    i4 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4]
    
    instruction_connections = [(i1,i2,1),(i1,i3,1),(i2,i1,1),(i3,i3,2),(i3,i4,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections,True)

    return vm

def Igual(n1,n2):
    h1 = Host(n1)
    h2 = Host(n2)
    h3 = Host(1)
    env = Host()
    
    hosts = [h1,h2,h3,env]
    
    i1 = Instruction(h1, h3)
    i2 = Instruction(h2, h3)
    i3 = Instruction(h2, h3)
    i4 = Instruction(None, None)    
    i5 = Instruction(h3, env)
    
    instructions = [i1,i2,i3,i4,i5]
    
    instruction_connections = [(i1,i2,2),(i2,i1,2),(i1,i3,1),(i3,i4,2),(i3,i5,1),(i2,i4,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def Menor(n1,n2):
    h1 = Host(n1)
    h2 = Host(n2)
    h3 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,env]
    
    i1 = Instruction(h1, h3)
    i2 = Instruction(h2, h3)
    i3 = Instruction(h2, h3)
    i4 = Instruction(None, None)    
    i5 = Instruction(h3, env)
    
    instructions = [i1,i2,i3,i4,i5]
    
    instruction_connections = [(i1,i2,2),(i2,i1,2),(i1,i3,1),(i3,i4,1),(i3,i5,2),(i2,i4,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def Mayor(n1,n2):
    h1 = Host(n1)
    h2 = Host(n2)
    h3 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,env]
    
    i1 = Instruction(h1, h3)
    i2 = Instruction(h2, h3)
    i3 = Instruction(h2, h3)
    i4 = Instruction(h3, env)    
    i5 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4,i5]
    
    instruction_connections = [(i1,i2,2),(i2,i1,2),(i2,i4,1),(i1,i3,1),(i3,i5,2),(i4,i5,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections)

    return vm

def Aleatorio(p):
    h1 = Host()
    h2 = Host(1)
    h3 = Host(1)
    h4 = Host(p)
    h5 = Host()
    h6 = Host()
    h7 = Host()
    h8 = Host()
    env = Host()
    
    hosts = [h1,h2,h3,h4,h5,h6,h7,h8,env]
     
    i1 = Instruction(h1, h2)
    i2 = Instruction(h2, h1,2)
    i3 = Instruction(h1, h5)
    i4 = Instruction(h3, h6)
    i5 = Instruction(h5, h8)
    i6 = Instruction(h6, h3)
    i7 = Instruction(h6, h3)
    i8 = Instruction(h1, h5)
    i9 = Instruction(h5, h7)
    i10 = Instruction(h4, h6)
    i11 = Instruction(h4, h6)
    i12 = Instruction(h5, h7)
    i13 = Instruction(h6, h4)
    i14 = Instruction(h7, h8)
    i15 = Instruction(h7, env)
    i16 = Instruction(h6, h4)
    i17 = Instruction(None, None)
    
    instructions = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15,i16,i17]
    
    instruction_connections = [(i1,i2,1),(i2,i1,1),(i1,i3,1),(i3,i5,1),(i3,i4,2),(i4,i3,2),(i5,i6,1),(i6,i1,1),
                              (i4,i7,1),(i7,i8,1),(i8,i8,2),(i8,i9,1),(i9,i10,2),(i10,i9,2),(i9,i11,1),(i10,i12,1),
                               (i11,i12,1),(i12,i12,2),(i12,i13,1),(i13,i13,2),(i13,i14,1),(i14,i14,2),(i14,i1,1),
                               (i11,i15,2),(i15,i15,2),(i15,i16,1),(i16,i16,2),(i16,i17,1)]
    
    vm = VirusMachine(hosts, instructions, instruction_connections, True)

    return vm