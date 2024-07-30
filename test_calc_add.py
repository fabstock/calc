import unittest
from calc import addition


class Testing(unittest.TestCase):

    def setUp(self):
        print("Avant le test")

    def tearDown(self):
        print("Après le test")


    def test_simple(self):

        self.assertTrue(True)

 


    def add_two(n: int) -> int:
        # def addition():
        string=n
        expected_value = "3"
        self.assertEqual(string.strip(), expected_value)
        #returnint(expected_value)
        #return int(n+2)




if __name__ == '__main__':
  unittest.main()
  testing=Testing()
  #print("add test:" , testing.addition(1,2)
  print("add test:" , testing.add_two(1))

