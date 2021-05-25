import unittest
import KDEclassifier


class TestKDE(unittest.TestCase):

    def test_n_volume(self):
        result = KDEclassifier.n_volume(2, 3)
        self.assertEqual(result, 9 )
        
        
    def test_n_volume_float(self):
        result = KDEclassifier.n_volume(1.5, 3)
        self.assertAlmostEqual(result, 14.137, places=3)
        
    def test_n_volume_notzero(self):
        result = KDEclassifier.n_volume(-3, 2)
        self.assertIsNot(result, 0)
        

    def test_n_volume_notnegative(self):
        result = KDEclassifier.n_volume(2, 2)
        self.assertGreater(result, 0)
        
   # def test_n_volume(self) :
    #    if type(self) not in [int, float]:
     #       raise TypeError("Should be integer or float")
    
        
    def test_fit(self):
       result = KDEclassifier.fit(self, 1)
       self.assertRaises(ValueError)
        
   # def test_dimension_control(self):
    #    result = KDEclassifier.fit(self, 1)
     #   self.assertIsNot(self, 2, ValueError)
        
    #def test_eval(self):
     #   result = KDEclassifier.eval(self, 1)
      #  self.assertRaises(ValueError, 'X must be 2D')  

if __name__ == '__main__':
    unittest.main()
    
    
   


        

