from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
import sys

sys.path.append('/Users/yugeshluitel/Documents/State-Space-Visualizer/')
import EightPuzzle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/eightpuzzle/bfs")
def bfs():
    searching = EightPuzzle.Search(
            EightPuzzle.Node(
                EightPuzzle.Game(
                    EightPuzzle.State([1, 2, 3, 4, 8, " ", 7, 6, 5]),
                    EightPuzzle.State([1, 2, 3, 4, 5, 6, 7, 8, " "]),
                )
            )
        )
       
    temp = searching.start_single_search_bfs()

    return{"Searching Status": searching.finished, "Found": str(temp), "Data": searching.graphvizzes}

@app.get("/eightpuzzle/dfs")
def dfs():
    searching = EightPuzzle.Search(
            EightPuzzle.Node(
                EightPuzzle.Game(
                    EightPuzzle.State([1, 2, 3, 4, 8, " ", 7, 6, 5]),
                    EightPuzzle.State([1, 2, 3, 4, 5, 6, 7, 8, " "]),
                )
            )
        )
       
    # if(temp is None):
    #         print(f"Cannot find the end state within {depth} depth.")
    # else:
    #     while len(temp.parent) != 0:
    #         print(temp)
    #         temp = temp.parent[0]

    #     print(f"root: {searching.root}")
    #     print(searching.finished)

    temp = searching.start_single_search_dfs()

    return{"Searching Status": searching.finished, "Found": str(temp), "Data": searching.graphvizzes}

@app.get("/eightpuzzle/idfs/{depth}")
def idfs(depth: int = 3):
    searching = EightPuzzle.Search(
            EightPuzzle.Node(
                EightPuzzle.Game(
                    EightPuzzle.State([1, 2, 3, 4, 8, " ", 7, 6, 5]),
                    EightPuzzle.State([1, 2, 3, 4, 5, 6, 7, 8, " "]),
                )
            )
        )
       
    temp = searching.start_search_idfs(depth)

    if(temp is None):
            print(f"Cannot find the end state within {depth} depth.")
    else:
        while len(temp.parent) != 0:
            print(temp)
            temp = temp.parent[0]

        print(f"root: {searching.root}")
        print(searching.finished)

    # temp = searching.start_single_search_dfs()

    return{"Searching Status": searching.finished, "Found": str(temp), "Data": searching.graphvizzes}


@app.get("/eightpuzzle/heuristics/manhatten")
def manhatten():
    searching = EightPuzzle.Search(
            EightPuzzle.Node(
                EightPuzzle.Game(
                    EightPuzzle.State([1, 2, 3, 4, 8, " ", 7, 6, 5]),
                    EightPuzzle.State([1, 2, 3, 4, 5, 6, 7, 8, " "]),
                )
            )
        )
       
    temp = searching.start_search_manhatten()

    # if(temp is None):
    #         print(f"Cannot find the end state within {depth} depth.")
    # else:
    #     while len(temp.parent) != 0:
    #         print(temp)
    #         temp = temp.parent[0]

    #     print(f"root: {searching.root}")
    #     print(searching.finished)

    # temp = searching.start_single_search_dfs()

    return{"Searching Status": searching.finished, "Found": str(temp), "Data": searching.graphvizzes}

@app.get("/eightpuzzle/heuristics/misplaced")
def misplaced():
    searching = EightPuzzle.Search(
            EightPuzzle.Node(
                EightPuzzle.Game(
                    EightPuzzle.State([1, 2, 3, 4, 8, " ", 7, 6, 5]),
                    EightPuzzle.State([1, 2, 3, 4, 5, 6, 7, 8, " "]),
                )
            )
        )
       
    temp = searching.start_search_misplaced()

    # if(temp is None):
    #         print(f"Cannot find the end state within {depth} depth.")
    # else:
    #     while len(temp.parent) != 0:
    #         print(temp)
    #         temp = temp.parent[0]

    #     print(f"root: {searching.root}")
    #     print(searching.finished)

    # temp = searching.start_single_search_dfs()

    return{"Searching Status": searching.finished, "Found": str(temp), "Data": searching.graphvizzes}