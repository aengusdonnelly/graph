from SimpleMatrixGraph import *
import unittest

class TestExample(unittest.TestCase):

    def test_add_vertex(self):
        '''Prövar ifall metoden "add_vertex" lägger till hörn i grafen på
        rätt sätt.'''
        g = Graph()
        g.add_vertex("Hello world!")
        g.add_vertex(15)
        g.add_vertex(True)
        g.add_vertex(15)
        self.assertEqual(g.values, ["Hello world!", 15, True])
        self.assertEqual(g.size_, 3)

    def test_add_edge(self):
        '''Prövar ifall metoden "add_edge" lägger till kanter i grafen på
        rätt sätt."'''
        g = Graph()
        g.add_vertex("a")
        g.add_vertex("b")
        g.add_edge("a", "b")
        g.add_edge("a", "b")
        self.assertEqual(g.matrix[g.values.index("a")][g.values.index("b")], 1)
        self.assertEqual(g.matrix[g.values.index("b")][g.values.index("a")], 1)

    def test_remove_vertex(self):
        '''"prövar ifall metoden "remove_vertex" tar bort hörn i grafen på
        rätt sätt'''
        g = Graph()
        g.add_vertex("a")
        g.add_vertex("b")
        g.remove_vertex("a")
        g.remove_vertex("b")
        self.assertEqual(g.matrix, None)
        self.assertEqual(g.values, [])
        self.assertEqual(g.size_, 0)

    def test_remove_edge(self):
        '''Prövar ifall metoden "romove_edge" tar bort till kanter i
        grafen på rätt sätt."'''
        g = Graph()
        g.add_vertex("a")
        g.add_vertex("b")
        g.add_edge("a", "b")
        g.remove_edge("a", "b")
        self.assertEqual(g.matrix[g.values.index("a")][g.values.index("b")], 0)
        self.assertEqual(g.matrix[g.values.index("b")][g.values.index("a")], 0)
    
    def test_clear(self):
        '''Prövar ifall metoden "clear" rensar grafen.'''
        g = Graph()
        g.add_vertex("a")
        g.add_vertex("b")
        g.add_edge("a", "b")
        g.clear()
        self.assertEqual(g.matrix, None)
        self.assertEqual(g.values, [])
        self.assertEqual(g.size_, 0)
    
    def test_get_vertices(self):
        '''Prövar ifall metoden "get_vertices" retunerar rätt mängd
        hörn.'''
        g = Graph()
        g.add_vertex("a")
        g.add_vertex("b")
        g.add_vertex("c")
        self.assertEqual(g.get_vertices(), set(g.values))
    
    def test_get_edges(self):
        '''Prövar ifall metoden "get_edges" retunerar rätt mängd
        kanter.'''
        g = Graph()
        g.add_vertex("a")
        g.add_vertex("b")
        g.add_vertex("c")
        g.add_edge("a", "b")
        g.add_edge("b", "c")
        g.add_edge("c", "a")
        self.assertEqual(g.get_edges(), {("a", "b"), ("a", "c",), ("b", "c")})

    def test_get_neighbours(self):
        '''Prövar ifall metoden "get_neighbours" retunerar rätt mängd med
        grannar.'''
        g = Graph()
        g.add_vertex("a")
        g.add_vertex("b")
        g.add_vertex("c")
        g.add_edge("a", "b")
        g.add_edge("a", "c")
        self.assertEqual(g.get_neighbours("a"), {"b", "c"})

    def test_get_degree(self):
        '''Prövar ifall metoden "degree" retunerar rätt grad av ett
        hörn.'''
        g = Graph()
        g.add_vertex("a")
        g.add_vertex("b")
        g.add_vertex("c")
        g.add_edge("a", "b")
        g.add_edge("a", "c")
        self.assertEqual(g.get_degree("a"), 2)

    def test_get_distance(self):
        '''Prövar ifall metoden "get_distance" retunerar rätt minsta
        sträcka mellan två hörn.'''
        g = Graph()
        g.add_vertex("a")
        g.add_vertex("b")
        g.add_vertex("c")
        g.add_vertex("d")
        g.add_vertex("e")
        g.add_edge("a", "b")
        g.add_edge("a", "c")
        g.add_edge("c", "b")
        g.add_edge("a", "d")
        g.add_edge("d", "e")
        g.add_edge("e", "b")
        self.assertEqual(g.get_distance("a", "b"), 1)
        g.remove_edge("a", "b")
        self.assertEqual(g.get_distance("a", "b"), 2)
        g.remove_edge("a", "c")
        g.remove_edge("c", "b")
        self.assertEqual(g.get_distance("a", "b"), 3)
        g.remove_edge("a", "d")
        g.remove_edge("d", "e")
        g.remove_edge("e", "b")
        self.assertEqual(g.get_distance("a", "b"), None)
        self.assertEqual(g.get_distance("a", "a"), 0)

    def test_exist_vertex(self):
        '''Prövar ifall metoden "exist_vertex" korrekt undersöker om ett
        hörn finns i grafen.'''
        g = Graph()
        g.add_vertex("a")
        self.assertEqual(g.exist_vertex("a"), True)
        g.remove_vertex("a")
        self.assertEqual(g.exist_vertex("a"), False)
    
    def test_exist_edge(self):
        '''Prövar ifall metoden "exist_edge" korrekt undersöker om en
        kant finns i grafen.'''
        g = Graph()
        g.add_vertex("a")
        g.add_vertex("b")
        g.add_edge("a", "b")
        self.assertEqual(g.exist_edge("a", "b"), True)
        g.remove_edge("a", "b")
        self.assertEqual(g.exist_edge("a", "b"), False)

    def test_exist_path(self):
        '''Prövar ifall metoden "exist_path" retunerar ett korrekt
        resultat på ifall det finns en sammanlänkning mellan två hörn.'''
        g = Graph()
        g.add_vertex("a")
        g.add_vertex("b")
        g.add_vertex("c")
        g.add_vertex("d")
        g.add_edge("a", "b")
        g.add_edge("a", "c")
        g.add_edge("b", "c")
        g.add_edge("c", "d")
        self.assertEqual(g.exist_path("a", "d"), True)
        g.remove_edge("a", "c")
        self.assertEqual(g.exist_path("a", "d"), True)
        g.remove_edge("b", "c")
        self.assertEqual(g.exist_path("a", "d"), False)

    def test_size(self):
        '''Prövar ifall metoden "size" retunerar rätt storlek på
        grafen.'''
        g = Graph()
        g.add_vertex("a")
        g.add_vertex("b")
        self.assertEqual(g.size(), 2)
        g.remove_vertex("a")
        self.assertEqual(g.size(), 1)

if __name__ == "__main__":
    unittest.main()