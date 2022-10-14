from matek import *
import unittest

class MatekTest(unittest.TestCase):
    def test_kerek_kivon_kerekit(self):
        eredmeny = kerek_kivon(0.5, 0.2)
        self.assertEqual(0.3, eredmeny)
    
    def test_kerek_kivon_egeszre(self):
        eredmeny = kerek_kivon(5, 2)
        self.assertEqual(3, eredmeny)
    
    def test_kerek_szoroz_egeszre(self):
        eredmeny = kerek_szoroz(5, 2)
        self.assertEqual(10, eredmeny) 
    
    def test_kerek_szoroz_kerekit(self):
        eredmeny = kerek_szoroz(0.5, 0.2)
        self.assertEqual(0.1, eredmeny) 


if __name__ == '__main__':
    unittest.main()