import unittest
from djCalculator import DjCalculator

class DjCalculatorTests(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(DjCalculator().calculate("+(1,2.5,3)"), 6.5)
        
    def test_product(self):
        self.assertEqual(DjCalculator().calculate("*(20,3,0.1)"), 6.0)
        
    def test_count(self):
        self.assertEqual(DjCalculator().calculate("~(20,3,0.1)"), 3)
    
    def test_combined1(self):
        self.assertEqual(DjCalculator().calculate("+(1,2,3.5,*(2,4),1,2,3)"), 20.5)
        
    def test_combined2(self):
        self.assertEqual(DjCalculator().calculate("+(*(2,4),1,2,3.5,1,2,3)"), 20.5)
        
    def test_combined3(self):
        self.assertEqual(DjCalculator().calculate("+(+(1,2),~(5,4))"), 5)
        
    def test_combined4(self):
        self.assertEqual(DjCalculator().calculate("+(+(1,2,3),1,2,3)"), 12)
        
    def test_combined5(self):
        self.assertEqual(DjCalculator().calculate("+(1,2,3,4.5,4.555,8,+(45,2.3))"), 70.35499999999999)
        
    def test_division(self):
        self.assertEqual(DjCalculator().calculate("*(6,/(2,3))"), 1.0)
        
    def test_nested(self):
        self.assertEqual(DjCalculator().calculate("*(~(/(+(1))))"), 1)
        
    def test_extravenous_bracket(self):
        with self.assertRaises(SyntaxError):
            DjCalculator().calculate("*(1,(2))")
            
    def test_missing_brackets(self):
        with self.assertRaises(SyntaxError):
            DjCalculator().calculate("+(+(+(1,2)")
            
    def test_missing_operation_brackets(self):
        with self.assertRaises(SyntaxError):
            DjCalculator().calculate("1,2,3")
            
    def test_missing_operation(self):
        with self.assertRaises(SyntaxError):
            DjCalculator().calculate("(1,2,3)")
            
    def test_missing_comma(self):
        with self.assertRaises(SyntaxError):
            DjCalculator().calculate("*(1,2~(3,4))")
            
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            DjCalculator().calculate("/(0)")
    
if __name__ == "__main__":
    unittest.main()
