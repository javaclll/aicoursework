import graphviz
from space_search import Node, Search
from game import Game, GameState

graph = graphviz.Digraph(comment="The Table")
graph.attr(layout="dot")
graph.attr(dpi="500")

searching = Search()
print(searching.start_single_search())

height = {}
nodeList = [searching.root]
childrenList = []
parent = []
while nodeList:
    node = nodeList.pop(0)

    color = "lightblue"

    if node.data.gameStatus == GameState.Failed:
        color = "pink"
    elif node.data.gameStatus == GameState.Won:
        color = "lightgreen"

    graph.node(str(node.data), style="filled", color=color, shape="egg")
    if len(node.parent) > 0:
        for parentNode in node.parent:
            print(f"Node: {node.data} Parent: {parentNode.data}")

            graph.edge(
                str(parentNode.data), str(node.data), label=str(node.data.movePerformed)
            )

    childrenList.extend(node.children)

    if len(nodeList) == 0:
        if len(childrenList) != 0:
            nodeList = childrenList
            childrenList = []


source = graph
source.render("Missionary Cannibal", format="jpg", view=True)
