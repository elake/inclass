import graph
import display
import time
import random
import sys

"""
Random walk in a graph demo

python3 walk.py [ --seed int ] [ --num_v int ] [ --num_e int ] 
    [ --start v ] [ --stop v ] [ --max_steps n ]

Try with:
    python3 walk.py --seed 23 --num_v 20 --num_e 30 --start 0 --stop 1
"""

seed = None
num_vertices = 10
num_edges = 25
start = None
stop = None
max_num_steps = 50

argv = sys.argv[1:]
while argv:
    token = argv.pop(0)
    if token == "--seed":
        seed = int(argv.pop(0))
    elif token == "--num_v":
        num_vertices = int(argv.pop(0))
    elif token == "--num_e":
        num_edges = int(argv.pop(0))
    elif token == "--start":
        start = int(argv.pop(0))
    elif token == "--stop":
        stop = int(argv.pop(0))
    elif token == "--max_steps":
        max_num_steps = int(argv.pop(0))
    else:
        print("Bad argument {}".format(token))
        sys.exit(1)

# use supplied seed if given
if seed is not None:
    random.seed(seed)

G = graph.generate_random_graph(num_vertices, num_edges)
dot_file_name = "walk-graph.dot"
# display.write_dot_desc(G, dot_file_name)

(V, E) = G

# start and stop vertices
if start is None:
    start = random.choice(list(V))

if stop is None:
    stop = random.choice(list(V))

# rendering attributes
attr = {"vertex_color":{}, "edge_color":{}}

# define a color for start and stop vertex
attr["vertex_color"][start]="green"
attr["vertex_color"][stop]="red"

print("Starting at {}, ending at {}".format(start, stop))
if len(graph.neighbours_of(G, start)) == 0:
    raise Exception("Bad luck, {} has no neighbours".format(start))

num_steps = 0

display.write_dot_desc(G, dot_file_name, attr)

cur = start
while cur != stop and num_steps < max_num_steps:
    display.pause(0)
    num_steps += 1

    print("Step {} at {}".format(num_steps, cur))
    # find a random neighbour of cur
    prev = cur
    neighbours = graph.neighbours_of(G, cur)
    cur = random.choice(list(neighbours))

    # do some coloring before next graph render
    attr["vertex_color"][prev]="white"
    attr["vertex_color"][start]="green"
    attr["vertex_color"][cur]="orange"
    attr["vertex_color"][stop]="red"
    attr["edge_color"][graph.mk_edge(prev, cur)]="orange"
    display.write_dot_desc(G, dot_file_name, attr)

print("Finished, after {} steps we are at {}".format(num_steps, cur))
if cur != stop:
    print("We failed to reach the stop vertex {}".format(stop))
