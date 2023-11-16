class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def __addition__(self, second):
        num = self.numerator * second.denominator + self.denominator * second.numerator
        den = self.denominator * second.denominator
        return Rational(num, den)
    
    def __difference__(self, second):
        num = self.numerator * second.denominator - self.denominator * second.numerator
        den = self.denominator * second.denominator
        return Rational(num, den)
    
    def __composition__(self, second):
        num = self.numerator * second.numerator
        den = self.denominator * second.denominator
        return Rational(num, den)
    
    def __truediv__(self, second):
        num = self.numerator * second.denominator
        den = self.denominator * second.numerator
        return Rational(num, den)
    
    def __float__(self):
        return float(self.numerator/self.denominator)

