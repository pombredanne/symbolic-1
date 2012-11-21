import unittest
import symath

class TestCoreClasses(unittest.TestCase):

  def setUp(self):
    self.w, self.v = symath.wilds('w v')
    self.x, self.y = symath.symbols('x y')
    self.head = symath.symbols('head')

  def test_match(self):
    m = {}
    self.assertTrue(self.head(self.x, 3).match(self.w(self.x, self.v), m))
    self.assertEqual(m['w'], self.head)
    self.assertEqual(m['v'], 3)

    self.assertFalse(self.head(self.x, self.y).match(self.head(self.v, self.v)))

    self.assertTrue(self.head(self.x, self.x).match(self.head(self.v, self.v), m))
    self.assertEqual(m['v'], self.x)

  def test_none_wild_match(self):
    m = {'should be removed': True}
    self.assertTrue(self.head(self.x).match(symath.wild()(self.x), m))

if __name__ == '__main__':
  unittest.main()
