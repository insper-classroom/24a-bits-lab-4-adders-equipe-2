from myhdl import *

@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a & b  
    return instances()

@block
def fullAdder(a, b, c, soma, carry_out):
    s = [Signal(bool(0)) for _ in range(3)]
    carry = [Signal(bool(0)) for _ in range(2)]

    ha1 = halfAdder(a, b, s[0], carry[0])
    ha2 = halfAdder(s[0], c, s[1], carry[1])
    
    @always_comb
    def comb():
        s[2].next = s[1]
        carry_out.next = carry[0] | carry[1]
        soma.next = s[2]
    return instances()

@block
def adder2bits(x, y, soma, vaiUm):
    
    c0 = Signal(bool(0)) 
    HA = halfAdder(x[0], y[0], soma[0], c0)
    FA = fullAdder(x[1], y[1], c0, soma[1], vaiUm)

    
    return instances()



@block
def adder(x, y, soma, carry):
    @always_comb
    def comb():
        pass

    return instances()
