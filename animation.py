from __future__ import absolute_import
from gvanim import Animation, render, gif
from space_search import Node, Search
from game import GameState
from random import sample

if __name__ == "__main__":
    datapoints = dict()

    searching = Search()
    searching.start_single_search()

    for node in searching.searchedNodes:
        if datapoints.get(str(node.data)):
            datapoints[str(node.data)].extend(node.children)
        else:
            datapoints[str(node.data)] = node.children

    # nodeList = [searching.root]
    # childrenList = []
    # parent = []
    # while nodeList:
    #     node = nodeList.pop(0)

    #     if datapoints.get(str(node.data)):
    #         datapoints[str(node.data)].extend(node.children)
    #     else:
    #         datapoints[str(node.data)] = node.children

    #     childrenList.extend(node.children)

    #     if len(nodeList) == 0:
    #         if len(childrenList) != 0:
    #             nodeList = childrenList
    #             childrenList = []

    graphAnimation = Animation()

    print(len(datapoints))
    graphAnimation.add_node(str(searching.root.data))
    graphAnimation.next_step()

    for vertex, adjacents in datapoints.items():
        for uertex in adjacents:
            color = "cyan"

            if uertex.data.gameStatus == GameState.Failed:
                color = "pink"
            elif uertex.data.gameStatus == GameState.Won:
                color = "lightgreen"

            graphAnimation.add_node(str(uertex.data), color=color)
            graphAnimation.add_edge(
                vertex, str(uertex.data), label=f" {str(uertex.data.movePerformed)}"
            )

            graphAnimation.next_step()

    graphs = graphAnimation.graphs()
    files = render(graphs, "./animationimages/M and C", "png", 1500)
    print(files)
    gif(files, "M and C", 30, 1500)
