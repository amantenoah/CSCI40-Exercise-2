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
        
        divisor = min(a, b)
        while divisor:
            if a % divisor == 0 and b % divisor == 0:
                break
            divisor -= 1
        return divisor
        
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def get_fraction(self):
        divisor = self.gcd(int(self.get_numerator()), self.get_denominator())

        if divisor == 0:  
            return "0" if self.get_numerator() == 0 else f"{self.get_numerator()}/{self.get_denominator()}"

        simplifiednumerator = int(self.get_numerator() / divisor)
        simplifieddenominator = int(self.get_denominator() / divisor)
        
        if self.get_denominator() == 1:
            return str(simplifiednumerator)
        
        return f"{simplifiednumerator}/{simplifieddenominator}"
