class Fraction(object):

    def __init__(self, numerator=None, denominator=None):
        # Handle standard two value inputs
        if denominator is not None:
            if not (isinstance(numerator, int) and isinstance(denominator, int)):
                raise TypeError("Both numerator and denominator must be integers.")
            self.numerator = numerator
            self.denominator = denominator
            if self.denominator == 0:
                raise ValueError("Denominator cannot be 0")
            
        # Handle single value inputs, i.e. rational number or strings
        # Rationale number input    
        elif isinstance(numerator, int):
            self.numerator = numerator
            self.denominator = 1
            
        elif isinstance(numerator, str):
            fraction = numerator.strip() # Remove any unecessary white spaces
            # Find the / that divides numerator and denominator, assign values after
            divisionIndex = 0
            for digit in numerator:
                if digit == "/":
                    divisionIndex = digit.index()
                    
            self.numerator = numerator[:divisionIndex]
            self.denominator = numerator[divisionIndex:]
            if self.denominator == 0:
                raise ValueError("Denominator cannot be 0")
                
        # Handle remaining invalid inputs
        else:
            raise TypeError("Invalid input, refer to instructions for proper syntax")
        
        
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
        #TODO
        pass