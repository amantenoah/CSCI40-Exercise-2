class Fraction(object):

    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __init__(self, fraction):
        numerator = int(fraction[0])
        denominator = int(fraction[2])
        self.fraction = numerator/denominator

    def __init__(self, number):
        numerator = int(number)
        denominator = 1
        self.fraction = numerator/denominator
                
    def __init__(self, fraction):
        pass

    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        
        

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass