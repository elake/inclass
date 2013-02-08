def deepcopy(l, memo = None):
    """
    deep copy a list

    >>> l = []
    >>> r = deepcopy(l)
    >>> r is l
    False
    >>> l = [ 1]
    >>> r = deepcopy(l)
    >>> l == r
    True
    >>> r is l
    False
    >>> r[0] is l[0]
    True
    >>> l = [ [ 1, 2, 3], [4, 5], 6 ]
    >>> r = deepcopy(l)
    >>> (r is not l) and (r == l) and (r[0] is not l[0]) and (r[1] is not l[1])
    True
    >>> l = [ 1 ]
    >>> l.append(l)
    >>> r = deepcopy(l)
    >>> l is not r
    True
    >>> l = [1, 2, "fred"]
    >>> r = deepcopy(l)
    >>> (l is not r) and (l == r)
    True
    >>> l
    >>> r
    """
    if not memo:
        memo = {}

    if id(l) in memo:
        return memo[id(l)]

    try:
        if len(l) == 0: return []
    except TypeError:
        return l

    r = []
    memo[id(l)] = r
    for e in l:
        r.append(deepcopy(e, memo))
    return r

if __name__ == "__main__":
    import doctest
    doctest.testmod()
