#import unittest class to do pyunittesting and import class for sum of elements
import unittest
from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int1(self):
        data1 = [54, 456, 78] # Sum of the values is 588
        result1 = sum(data1)
        #test if the sum of numbers is correct
        self.assertEqual(result1, 588)
    def test_list_int2(self):
        data2 = [23525,234234,123123] # Sum of the values is 380,882
        result2 = sum(data2)
        self.assertEqual(result2, 380882)

class testSetingMethods(unittest.TestCase):
     def test_upper(self):
         #Test if the string is fully written in uppercase
        self.assertEqual('Centennial'.upper(), 'CENTENNIAL')
     def test_is_upper(self):
         #Test true and false by each statement.
         self.assertTrue('CENTENNIAL'.isupper())
         self.assertFalse('Centennial'.isupper())
         #Test if the string is fully written in lowercase
     def test_lower(self):
          self.assertEqual('Centennial'.lower(),'centennial')
         #Test true and false by each statement.
     def test_is_lower(self):
          self.assertTrue('centennial'.islower())
          self.assertFalse('Centennial'.islower())
        #Test if the string is properly split
     def test_split(self):
          s = 'Centennial College'
          self.assertEqual(s.split(),['Centennial' , 'College'])
          # check that s.split fails when the separator is not a string
          with self.assertRaises(TypeError):
             s.split(2)

if __name__ == '__main__':
    unittest.main()

#def suite():
#    suite = unittest.TestSuite()
#    suite.addTest(TestSum('test_list_int1'))
#    suite.addTest(testSetingMethods('test_upper'))
#    return suite

#if __name__ == '__main__':
#    runner = unittest.TextTestRunner()
#    runner.run(suite())
