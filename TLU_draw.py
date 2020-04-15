import graphviz as gv



def tlu(weights, threshhold):

    g = gv.Digraph(format="svg")
    g.attr(rankdir="LR")

    y = str(threshhold)
    g.node(y, shape="circle")
    x = "x"
    for i, w in enumerate(weights):

        xi = x + str(i + 1)
        g.node(xi, shape="plaintext", width=".0")
        g.edge(xi, y, str(w), shape="circle")

    g.node("y", shape="plaintext",width=".0")
    g.edge(y, "y")
    g.render("./tlu")

tlu([-1,-1, 10], -0.5)
