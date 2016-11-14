from CalculsSimples import *
import unittest

class TestCalculsSimples(unittest.TestCase):

  a = 6
  b = 2
  
  def testAddition(self):
    self.assertEqual(CalculsSimples.addition(a,b), 8)
        
  def testSoustraction(self):
    self.assertEqual(CalculsSimples.soustraction(a,b), 4)
  
  def testMultiplication(self):
    self.assertEqual(CalculsSimples.multiplication(a,b),12)
  
  def testDivision(self):
    self.assertEqual(CalculsSimples.division(a,b),3)
