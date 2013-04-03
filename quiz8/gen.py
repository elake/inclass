def mystery(s):
    """
    Creates a generator that iterates through the input s and yields 
    non-duplicate entries. Average runtime O(n) but worst case scenario (maximum
    collisions in es lookups) O(n^2). Realistically this is extremely unlikely,
    so O(n) would be the most appropriate runtime. n in this case would be the
    number of entries in s.

    >>> s = [i for i in mystery([1,4,8,8,1])]
    >>> s
    [1, 4, 8]
    >>> s = [i for i in mystery([4,7,8,9])]
    >>> s
    [4, 7, 8, 9]
    >>> s = [i for i in mystery([0])]
    >>> s
    [0]
    >>> s = [i for i in mystery([])]
    >>> s
    []
    >>> s = [i for i in mystery({1,4,8,8,1})]
    >>> s
    [8, 1, 4]
    >>> s = [i for i in mystery({4,7,8,9})]
    >>> s
    [8, 9, 4, 7]
    >>> s = [i for i in mystery({0})]
    >>> s
    [0]
    >>> s = [i for i in mystery({})]
    >>> s
    []
    >>> s = [i for i in mystery((1,4,8,8,1))]
    >>> s
    [1, 4, 8]
    >>> s = [i for i in mystery((4,7,8,9))]
    >>> s
    [4, 7, 8, 9]
    >>> s = [i for i in mystery((0, 0))]
    >>> s
    [0]
    >>> s = [i for i in mystery(())]
    >>> s
    []
    """
    
    es = set()
    for e in s:
        if e not in es:
            yield e
            es.add(e)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
