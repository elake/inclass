"""
A graph G=(V, E)  
V is a set of vertices

E is a set of edges, elements of E are
unorderd pairs (v, w) where v, w in V

Note: do we want to adopt some convention
for orering of vertices in tuple?

"""
import random

def print_graph(G):
    print(G)

def mk_edge(x, y):
    """
    return the cannonical format of an edge
    >>> mk_edge(1, 2)
    (1, 2)
    >>> mk_edge(2, 1)
    (1, 2)
    """
    return (min(x, y), max(x, y))

def fix_edges(G):
    """
    Make sure that all edges in E are in cannonical format
    >>> G = ( {1, 2, 3}, { (1, 2), (3, 2), (2, 1) })
    >>> fix_edges(G)
    >>> G[1] == { (1, 2), (2, 3) }
    True
    """
    (V, E) = G
    E_new = set()
    for (x, y) in E: E_new.add(mk_edge(x, y))
    E.clear()
    E.update(E_new)

def neighbours_of(G, v):
    """
    return the set of neighbours of vertex v in G
    w is a neighbour of v if exists a edge {w, v} in E

    >>> G = ( {1, 2, 3}, { (1, 2), (1, 3) } )
    >>> neighbours_of(G, 1) == {2, 3}
    True
    """

    (V, E) = G
    neighbours = set()

    for (x, y) in E:
        if x == v: neighbours.add(y)
        if y == v: neighbours.add(x)

    return neighbours
        

def generate_random_graph(n, m):
    V = set(range(n))
    E = set()
    while len(E) < m:
        # add a random edge to E
        # old: E.add(tuple(random.sample(V, 2)))

        pair = random.sample(V, 2)
        E.add( mk_edge(pair[0], pair[1]) )

    return (V, E)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

