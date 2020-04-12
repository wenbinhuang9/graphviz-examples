import unittest

from graph import  Graph
import graphviz as gv


class MyTestCase(unittest.TestCase):


    def test_peripheries(self):
        g = gv.Digraph(format='svg')

        g.node("a",peripheries="2")

        g.render("./test_peripheries")

    def test_graph(self):
        graph = Graph()

        graph.edge("ancestor1 male", "ancestor2 male")
        graph.edge("ancestor2 male", "xhe male")


        lming = "ll male"
        ybai = "yy female"
        wb = "wb male"
        graph.edge("qq female", "ll male")
        graph.edge("qq male", "ll male")

        graph.edge(lming, wb)
        graph.edge(ybai, wb)

        graph.edge(lming, "gb male")
        graph.edge(ybai, "gb male")

        graph.edge(lming, "yy female")
        graph.edge(ybai, "yy female")

        graph.edge(lming, "jj female")
        graph.edge(ybai, "jj female")

        graph.render("./famliy")

if __name__ == '__main__':
    unittest.main()
