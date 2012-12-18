import symath
from symath.graph.algorithms import *
import symath.graph.generation as graphgen

import unittest

class TestDirectedGraph(unittest.TestCase):

  def setUp(self):
    self.x, self.y, self.z, self.w, self.e1, self.e2 = symath.symbols('x y z w e1 e2')
    self.g = symath.graph.directed.DirectedGraph()
    self.g.connect(self.x, self.y, self.e1)
    self.g.connect(self.y, self.z, self.e2)
    self.g.connect(self.z, self.w)
    self.g.connect(self.x, self.w)

  def test_edges(self):
    self.assertEqual(len(self.g.nodes[self.x].outgoing), 2)

  def test_pathq(self):
    self.assertTrue(pathQ(self.g, self.x, self.z))

  def test_adj_matrix(self):
    mp,m = self.g.adjacency_matrix()
    self.assertEqual(len(m), 4)
    self.assertEqual(m[mp[self.x],mp[self.y]], 1)
    self.assertEqual(m[mp[self.x],mp[self.x]], 0)

  def test_random_generation(self):
    randg = graphgen.random_graph(100, 0.05)
