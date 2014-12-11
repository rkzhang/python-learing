'''
@author: rkzhang
'''

class Complex(object):

    def __init__(self, real, imag=0) :
        self.real = float(real)
        self.imag = float(imag)
    
    def __repr__(self) :
        return "Complex(%s, %s)" % (self.real, self.imag)
    
    def __str__(self):
        return "(%g + %gj)" % (self.real, self.imag)
    
    def __add__(self, other) : 
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other) : 
        return Complex(self.real - other.real, self.imag - other.imag)
    
c = Complex(2, 3)
print c
print c + 3.0
print 3.0 + c
        
        