class Fraction(object):

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __init__(self, fraction):
        numerator = fraction[0]
        denominator = fraction[2]
        self.fraction = numerator/denominator

    def __init__(self, number):
        numerator = number
        denominator = 1
        self.fraction = numerator/denominator
                
    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def get_fraction(self):
        #TODO
        pass