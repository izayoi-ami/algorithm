##
class SingleBitHalfAdder:
    def __init__(self, A,B):
        self.A = A & 1
        self.B = B & 1

    def result(self):
        carry = self.A & self.B
        sum = self.A ^ self.B
        return carry, sum

class SinlgeBitFullAdder:
    def __init__(self,A,B,C):
        self.A = A&1
        self.B = B&1
        self.C = C&1

    def result(self):
        c, s = SingleBitHalfAdder(self.A, self.B).result()
        c, s =  c | (s ^ self.C) , s ^ self.C 
        return c, s

class Adder:
    @classmethod
    def add(self,a,b):
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        mask = 0xFFFFFFFF
        while b: a, b = (a^b) & mask, ((a&b)<<1) & mask
        return a if a <= MAX else ~(a ^ mask)


##
