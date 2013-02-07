"""
Class for representing undirected graphs.

A graph G is, conceptually, a pair G=(V, E)  
where
    V is a set of vertices.  Vertices must be comparable and immutable

    E is a set of edges, elements of E are pairs (u, v) where v, w are in V
    and the pair is ordered such that v < w

Note: this means no self loops, i.e an edge (v, v) from v back to itself.
"""

import random
import copy

class Graph:
    """
    """
    
    def __init__(self):
        self._vertices = set()
        self._edges = set()

    def __repr__(self):
        return "Graph({},{})".format(self._vertices, self._edges)

    def add_vertex(self, v):
        self._vertices.add(v)

    def add_edge(self, e):
        """
        G.add_edge( (x, y) ) add the edge (x, y) to G, and if x or y is not a
        vertex, then adds x, y to the vertices of G .  If (x, y) are not in 
        cannoncial ordering then they are reorderd.

        It is ok if the edge already exists.

        >>> G = Graph()
        >>> G.add_edge( (2, 1) )
        >>> G._vertices == {1, 2}
        True
        >>> G._edges == { (1, 2) }
        True
        """
        x = min(e)
        y = max(e)
        if x not in self._vertices:
            self.add_vertex(x)
        if y not in self._vertices:
            self.add_vertex(y)
        self._edges.add( (x, y) )

    def num_edges(self):
        return len(self._edges)

    def num_vertices(self):
        return len(self._vertices)

    def get_vertices(self):
        """
        G.get_vertices() returns the set of vertices in G
        """
        return self._vertices
     
    def get_edges(self):
        """
        G.get_edges() returns the set of edges in G
        """
        return self._edges

    def adj_to(self, v):
        """
        return the set of neighbours of vertex v

        w is a neighbour of v if there exists an
        edge {w, v}

        >>> G = Graph()
        >>> G.add_vertex(1)
        >>> G.add_vertex(2)
        >>> G.add_vertex(3)
        >>> G.add_edge((1,2))
        >>> G.add_edge((1,3))
        >>> G.adj_to(1) == {2, 3}
        True
        """

        neighbours = set()

        for (x, y) in self._edges:
            if x == v: neighbours.add(y)
            if y == v: neighbours.add(x)

        return neighbours


# Utility functions that don't really belong in the class, but in a distinct
# utility module

def random_graph(n, m):
    """
    Generate a random graph with n vertices and m edges

    >>> G = random_graph(5, 10)
    >>> G.num_edges()
    10
    >>> G.num_vertices()
    5
    """
    G = Graph()
    for v in range(n):
        G.add_vertex(v)
        
    while G.num_edges() < m:
        G.add_edge(random.sample(range(n), 2))

    return G

# Convenience constructor for a graph given by a list or set of edges
def graph_from_edges(e):
    """
    
    >>> G = graph_from_edges([(1, 2), (3, 1)])
    >>> G.get_vertices() == {1, 2, 3}
    True
    >>> G.get_edges() == { (1, 2), (1, 3) }
    True
    
    """
    G = Graph()
    for (x, y) in e:
        G.add_vertex(x)
        G.add_vertex(y)
        G.add_edge( (x, y) )
    return G

# Spanning tree, also a potential class method
def spanning_edges(G, root):
    """
    E = spanning_edges(G, root)

    Given graph G, and a starting root vertex, generate a set of edges  E that
    forms a tree that contains root, and spans as much of the graph as possible.

    If G is connected, then the E is the edges of a spanning tree.

        spanning_edges(G, root) 
    returns a set of all the edges in a spanning tree of G

    >>> e = { (0, 1), (1, 2), (2, 3), (2, 4) }
    >>> G = graph_from_edges(e)
    >>> s = spanning_edges(G, 0)
    >>> s == e
    True
    >>> len(s)
    4

    Now try a disconnected graph

    >>> G.add_edge( (5, 6) )
    >>> s = spanning_edges(G, 0)
    >>> s == e
    True
    >>> len(s)
    4

    Now try a graph with two different spanning sets
    >>> G.add_edge( (2, 5) )
    >>> G.add_edge( (3, 5) )
    >>> G.add_edge( (4, 1) )

    >>> s = spanning_edges(G, 0)
    >>> ls = list(s)
    >>> ls.sort()
    >>> ls
    [(0, 1), (1, 4), (2, 4), (2, 5), (3, 5), (5, 6)]

    >>> t = spanning_edges(G, 5)
    >>> lt = list(t)
    >>> lt.sort()
    >>> lt
    [(0, 1), (1, 4), (2, 3), (2, 4), (3, 5), (5, 6)]

    """

    visited = set()
    todo = [ (root, None) ]
    E = set()
    while todo:
        (cur, e) = todo.pop()
        if cur in visited: continue

        if e: 
            # return cannonical form of the edge
            E.add( (min(e), max(e) ) )
        visited.add(cur)

        for n in G.adj_to(cur):
            if n not in visited:
                todo.append((n, (cur, n)))
    return E

## Quiz 4 starts here
def connected_components(G):
    """
    C = connected_components(G) 

    returns a list of sets, each set consisting of vertices.

    Each of the elements of C is a maximal size connected component of G.  
    A connected component of G is a set of vertices where any vertex in the
    component has a path to any other vertex in the component.  A maximal
    size component means that no other vertex can be connected to it.
    A vertex that is not connected to any other vertex is its own connected 
    component.

    NOTE: the list of sets C is ordered by the minimum vertex of each component
    For example, this list of connected components
        [{1, 3}, {0}, {5}, {4, 6}]
    would be sorted in C as:
        [{0}, {1, 3}, {4, 6}, {5}]

    Hint: Finding a spanning tree finds a maximal connected component.

    Hint: when a connected component has fewer vertices than there are in G
    there must be at least one other connected component.

    >>> G = graph_from_edges( [ (1, 2), (2, 3),  (4, 5) ] )
    >>> C = connected_components(G)
    >>> C[0] == {1, 2, 3}
    True
    >>> C[1] == {4, 5}
    True
    >>> G = graph_from_edges( [ (0, 1), (1, 2), (2, 7), (9, 5) ] )
    >>> C = connected_components(G)
    >>> C[0] == {0, 1, 2, 7}
    True
    >>> C[1] == {5, 9}
    True
    >>> G.add_vertex(12) # note no edges
    >>> C = connected_components(G)
    >>> C[0] == {0, 1, 2, 7}
    True
    >>> C[1] == {5, 9}
    True
    >>> C[2] == {12}
    True
    >>> G.add_edge( (5, 2) )
    >>> C = connected_components(G)
    >>> C[0] == {0, 1, 2, 5, 7, 9}
    True
    >>> C[1] == {12}
    True
    >>> G.add_edge((12, 16))
    >>> C = connected_components(G)
    >>> C[1] == {12, 16}
    True
    
    """
    # start with empty list of components
    C = []
    # the number of items within all the sets of C
    lenC = 0
    # vertices not yet in C
    unaccountedFor = copy.deepcopy(G._vertices)
    while lenC < len(G._vertices):
        # start with any random vertex not yet accounted for
        root = random.sample(unaccountedFor, 1)[0]
        # run through the spanning tree code, more or less
        visited = set()
        todo = [ (root, None) ]
        E = set()
        while todo:
            (cur, e) = todo.pop()
            if cur in visited: continue

            if e: 
                # return cannonical form of the edge
                E.add( (min(e), max(e) ) )
            visited.add(cur)
            # vertices in visited will soon be accounted for
            unaccountedFor.remove(cur)
            # and therefore lenC will grow by 1 vertice
            lenC += 1

            for n in G.adj_to(cur):
                if n not in visited:
                    todo.append((n, (cur, n)))
        # each spanning tree is a set for C
        C.append(visited)
            
    # sort the components list by the min on each element
    C.sort(key=min)
    return C


if __name__ == "__main__":
    import doctest
    doctest.testmod()

