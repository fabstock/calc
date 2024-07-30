import unittest
#from src.calc import addition,substraction,multiplication,division
from src.calc import addition,substraction,multiplication,division
#from src.calc import *


class test_calc(unittest.TestCase):

    def setUp(self):
        print("Avant le test")

    def tearDown(self):
        print("Après le test")


    def test_simple(self):
        self.assertTrue(True)

    #def add_two(n: int) -> int:
    def test_two(self):
        #expected_value = "3"
        self.assertEqual(addition(1, 2), 3)
        #addition(1,2)
        #self.assertEqual(string.strip(), expected_value)
        #return int(expected_value)
        #return int(expected_value)
    
    def test_sub(self):
        self.assertEqual(substraction(1, 2), -1)
    
    def test_mul(self):
        self.assertEqual(multiplication(1,2),2)

    def test_div(self):
        self.assertEqual(division(1,2),0.5)



def test_sum():
    assert addition([1, 2, 3]) == 6, "Should be 6"


if __name__ == '__main__':
  unittest.main()
  #testing=Testing()
  #print("add test:" , testing.add_two(1)
  #print("add test:" , testing.add_two(1))

