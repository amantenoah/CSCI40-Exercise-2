class Fraction(object):

    def __init__(self, numerator=None, denominator=None):
        # Handle standard two value inputs
        if denominator is not None:
            if not (isinstance(numerator, int) and isinstance(denominator, int)):
                raise TypeError("Both numerator and denominator must be integers.")
            self.numerator = numerator
            self.denominator = denominator
            if self.denominator == 0:
                raise ZeroDivisionError("Denominator cannot be 0")
            
        # Handle single value inputs, i.e. rational number or strings
        # Rationale number input    
        elif isinstance(numerator, int):
            self.numerator = numerator
            self.denominator = 1
            
        elif isinstance(numerator, str):
            fraction = numerator.strip() # Remove any unecessary white spaces
            # Find the / that divides numerator and denominator, assign values after
            divisionIndex = 0
            for digit in fraction:
                if digit == "/":
                    divisionIndex = fraction.index(digit)
                    
            self.numerator = fraction[:divisionIndex]
            self.denominator = fraction[divisionIndex + 1:]
            try:
                self.numerator = int(self.numerator)
                self.denominator = int(self.denominator)
            except ValueError:
                self.numerator = 0
                self.denominator = 1
            if self.denominator == "0":
                raise ZeroDivisionError("Denominator cannot be 0")
                
        # Handle remaining invalid inputs
        else:
            self.numerator = 0
            self.denominator = 1
        
    @staticmethod
    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        
        while b:
            a, b = b, a % b  # Find the GCD by Euclidean Algorithm
        return a
        
    def get_numerator(self):
        divisor = Fraction.gcd(int(self.numerator), int(self.denominator))       
        return str(int(self.numerator/divisor))

    def get_denominator(self):
        divisor = Fraction.gcd(int(self.numerator), int(self.denominator))    
        return str(int(self.denominator/divisor))

    def get_fraction(self):
        if self.numerator == 0:
            return "0"
        return (self.get_numerator() + "/" + self.get_denominator())
