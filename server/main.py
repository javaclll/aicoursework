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

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/eightpuzzle/bfs")
def bfs():
    searching = EightPuzzle.Search(
            EightPuzzle.Node(
                EightPuzzle.Game(
                    EightPuzzle.State([1, 2, 3, 4, 5, 6, 7, " ", 8]),
                    EightPuzzle.State([1, 2, 3, 4, 5, 6, 7, 8, " "]),
                )
            )
        )
       
    depth = 2
        # temp = searching.start_search_idfs(depth)
        # temp = searching.start_search_misplaced()
    temp = searching.start_single_search_bfs()

    return{"Searching Status": searching.finished, "Found": str(temp), "Data": searching.graphvizzes}