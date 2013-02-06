import graph
import display
import time
import random
import sys

"""
Example of using breadth first search (BFS) to find a spanning tree
for graph G, starting at vertex root

Later we modify it to find a path in the spanning tree from start to any 
stop vertex.

Instead of generating a new graph that is the spanning tree, we just mark
the edges that are in the tree.  Edges are labelled in the order in which
they are first traversed during the search.

python3 bfs.py [ --seed int ] [ --num_v int ] [ --num_e int ] [ --root v ]

Try with:
    python3 bfs.py --seed 23 --num_v 20 --num_e 30 --root 0


"""

seed = None
num_vertices = 10
num_edges = 25
root = None

argv = sys.argv[1:]
while argv:
    token = argv.pop(0)
    if token == "--seed":
        seed = int(argv.pop(0))
    elif token == "--num_v":
        num_vertices = int(argv.pop(0))
    elif token == "--num_e":
        num_edges = int(argv.pop(0))
    elif token == "--root":
        root = int(argv.pop(0))
    else:
        print("Bad argument {}".format(token))
        sys.exit(1)

# use supplied seed if given
if seed is not None:
    random.seed(seed)

G = graph.generate_random_graph(num_vertices, num_edges)

(V, E) = G

# root vertex
if root is None:
    root = random.choice(list(V))

dot_file_name = "bfs-spanning-tree.dot"

# rendering attributes
attr = {
    "vertex_color":{}, 
    "edge_color":{},
    "vertex_label":{},
    "edge_label":{},
    }

# define a color for root
attr["vertex_color"][root]="green"
attr["vertex_label"][root]= str(root) + ":0"

print("Spanning tree rooted at {}".format(root) )
display.write_dot_desc(G, dot_file_name, attr)
display.pause(0)

# visited set, start with root being visited
visited = set([root])
visit_queue = [ root ]
edge_seq_num = 0
level = { root: 0}

while visit_queue:
    print("visited:" + str(visited))
    print("visit queue:" + str(visit_queue))

    # get the head of the queue, but don't remove
    v = visit_queue[-1]

    # find unvisited neighbour of v
    w = None
    for x in graph.neighbours_of(G, v):
        if x not in visited:
            w = x
            break

    if w is not None:
        # mark w as visited
        visited.add(w)

        print("visiting {} at step {}".format(w, edge_seq_num))
        level[w] = level[v] + 1

        # color and label the visited vertex
        attr["vertex_color"][w]="orange"
        attr["vertex_label"][w]= str(w) + ":" + str(level[w])

        # color the new edge v, w 
        attr["edge_label"][graph.mk_edge(v, w)]=edge_seq_num
        edge_seq_num += 1
        attr["edge_color"][graph.mk_edge(v, w)]="orange"

        # update the rendering
        display.write_dot_desc(G, dot_file_name, attr)
        display.pause(0)

        # add w to visit queue
        visit_queue.insert(0, w)
    else:
        # no unvisited neighbours, back track 
        visit_queue.pop()
