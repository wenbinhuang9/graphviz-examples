import graphviz as gv

class Graph():
    def __init__(self):
        self.node = set([])
        self.graph = self.__createSvg()

    def __createSvg(self):
        graph = gv.Digraph(format='svg')

        return graph

    def doubleEdge(self, a, b):
        self.edge(a, b)
        self.edge(b, a)
    def edge(self, a, b):
        if a not in self.node:
            self.node.add(a)
            self.graph.node(a)

            self.graph.node()
        if b not in self.node:
            self.node.add(b)
            self.graph.node(b)

        self.graph.edge(a, b)

    def render(self, file):
        self.graph.render(file)
