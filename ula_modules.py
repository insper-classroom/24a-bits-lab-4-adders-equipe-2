from myhdl import *

@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a & b  
    return instances()

@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]

    haList[0] = halfAdder(a, b, s[0], s[1])
    haList[1] = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]
    return instances()

@block
def adder2bits(x, y, soma, vaiUm):
    
    c0 = Signal(bool(0)) 
    HA = halfAdder(x[0], y[0], soma[0], c0)
    FA = fullAdder(x[1], y[1], c0, soma[1], vaiUm)

    
    return instances()


@block
def adder(x, y, soma, carryOut):
    n = len(x)
    c = [Signal(bool(0)) for _ in range(n+1)] 
    faList = [None for _ in range(n)]


    for i in range(n):
        if i == 0:
            faList[i] = fullAdder(x[i], y[i], c[i], soma[i], c[i+1])
        else:
            faList[i] = fullAdder(x[i], y[i], c[i], soma[i], c[i+1])

    @always_comb
    def comb():
        carryOut.next = c[n]

    return instances()

