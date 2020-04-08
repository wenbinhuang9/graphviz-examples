
import graphviz as gv

graph = gv.Digraph(format='svg')

source = "a"
target = "b"

sourceNode = graph.node(source)
targetNode = graph.node(target)

graph.edge(source, target)

graph.edge(target, source)
graph.render("./text.svg")