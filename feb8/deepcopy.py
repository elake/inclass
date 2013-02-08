def deepcopy(a):
    """
    Deep copies lists.
    """
    try:
        b = []
        for i in a:
            b.append(deepcopy(i))
        return b
    except TypeError:
        return a

def deepcopy2(a, memo=None):
    """
    Deep copies lists.  Handles recursive lists.
    """
    if not memo:
        memo = set()
    
    if id(a) in memo:
        return a
    else:
        memo.add(id(a))

    try:
        b = []
        for i in a:
            b.append(deepcopy2(i, memo))
        return b
    except TypeError:
        return a

def deepcopy3(a, memo=None):
    """
    Deep copies non-dictionary containers (tuples, lists, strings, etc.).
    Handles recursive data structures too.
    """
    if not memo:
        memo = set()

    # Check if we've already copied this exact object (based on its id)
    if id(a) in memo:
        return a
    else:
        memo.add(id(a))

    # Check if the thing is immutable.  If so, we can just return it.
    try:
        hash(a)
        return a
    except:
        pass

    # Otherwise we'll copy it as a list.
    try:
        b = []
        for i in a:
            b.append(deepcopy3(i, memo))
        return a.__class__(b)
    except TypeError:
        return a
