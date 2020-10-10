import pytest
from clacutator.calcy import Calculator

class Test001:
    num1=12
    num2=8

    def test_add_functionality(self):
        cal = Calculator()
        result=cal.add_two_numbers(self.num1,self.num2)
        assert result

    def test_sub_functionality(self):
        cal=Calculator()
        result=cal.sub_two_numbers(self.num1,self.num2)
        assert result

    def test_mul_functionality(self):
        cal=Calculator()
        result=cal.multiply(self.num1,self.num2)
        assert result







