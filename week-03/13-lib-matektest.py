#unit test készítése
import unittest
import matek #ez a tesztelendő

class MatekTeszt(unittest.TestCase):
    #teszt esetek létrehozása
    def test_kerek_osszead_problema(self):
        eredmeny = matek.kerekitett_osszeadas(0.2, 0.1)
        self.assertEqual(0.3, eredmeny)
    
    def test_kerek_osszead_problema_nelkul(self):
        eredmeny = matek.kerekitett_osszeadas(0.3, 0.2)
        self.assertEqual(0.5, eredmeny)
        
    def test_kerek_osszead_egeszre_mukodik(self):
        eredmeny = matek.kerekitett_osszeadas(3, 2)
        self.assertEqual(5, eredmeny)
    
    def test_kerek_osszead_kerekitessel(self):
        eredmeny = matek.kerekitett_osszeadas(0.22222222, 0.11111111)
        self.assertEqual(0.33333333, eredmeny)

if __name__ == '__main__';unittest.main()