from __future__ import absolute_import

import graphviz

from gvanim import Animation, render, gif
from searching import Node, Search
from game import Game, GameState
from random import sample


if __name__=="__main__":
    
    datapoints = dict()
    graph = graphviz.Digraph(comment="Missionary and Cannibal")
    graph.attr(layout = 'dot')
    graph.attr(dpi = '500')

    searching = Search()
    print(searching.start_single_search())

    nodeList = [searching.root]
    childrenList = []
    parent = []
    while nodeList:
        node = nodeList.pop(0)
       
        if len(node.parent) > 0:
            for parentNode in node.parent:
                print(f"Node: {node.data} Parent: {parentNode.data}")

        #         graph.edge(str(parentNode.data), str(node.data), label=str(node.data.movePerformed))
        if datapoints.get(str(node.data)):
            datapoints[str(node.data)].extend(node.children) 
        else:
            datapoints[str(node.data)] = node.children

        print(f"Mathi Parent: {node.data}, children: {[str(child.data) for child in node.children]}")

        
        childrenList.extend(node.children)

        if len(nodeList) == 0:
            if len(childrenList) != 0:
                nodeList = childrenList
                childrenList = []
                
    # source = graph
    # source.render('Missionary Cannibal', format='jpg',view=True)
    for key, value in datapoints.items():
        print(f"Parent: {key}, children: {[str(child.data) for child in value]}")

    graphAnimation = Animation()

    print(len(datapoints))
    graphAnimation.add_node(str(searching.root.data))
    graphAnimation.highlight_node(str(searching.root.data), color="lightblue")
    graphAnimation.next_step()

    for vertex, adjacents in datapoints.items():
        for uertex in adjacents:
            color = "lightblue"

            if uertex.data.gameStatus == GameState.Failed:
                color = "pink"
            elif uertex.data.gameStatus == GameState.Won:
                color = "lightgreen"

            graphAnimation.add_node(str(uertex.data), color=color)
            graphAnimation.next_step()
            graphAnimation.add_edge(vertex, str(uertex.data))
            graphAnimation.next_step()   

    # seen = [ False for _ in  enumerate(datapoints)]
    # print(seen)
    # print(len(seen))
    # index = { k : i for i , k in enumerate(datapoints.keys())}
    # def dfv(v):
    #     graphAnimation.highlight_node( v )
    #     graphAnimation.next_step()
    #     seen[ index [v] ] = True
    #     for u in datapoints[ v ]:
    #         if not seen[ index[str(u.data)] ]:
    #             graphAnimation.highlight_node( v )
    #             graphAnimation.highlight_edge( v, str(u.data) )
    #             graphAnimation.next_step()
    #             dfv( str(u.data) )

    # dfv(str(searching.root.data))

    graphs = graphAnimation.graphs()
    files = render( graphs, 'dfv', 'png', 1500)
    print(files)
    gif( files, 'dfv', 30, 1500)



