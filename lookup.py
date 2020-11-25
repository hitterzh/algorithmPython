
def foreach_lookup(collection, val):
    index = 0
    for item in collection:
        if val == item:
            return index
        index += 1

    # not find: return max index + 1
    return index


def binary_lookup_rec(collection, val):
    def lookup(collection, s, e, val):
        mid = (s+e)//2
        if val == collection[mid]:
            return mid
        elif val < collection[mid]:
            lookup(collection, s, mid, val)
        else:
            lookup(collection, mid + 1, e, val)

        return mid

    return lookup(collection, 0, len(collection), val)

def binary_lookup(collection, val):
    s = 0
    e = len(collection)

    while s != e:
        mid = (s+e)//2
        if val == collection(mid):
            return mid
        elif val < collection(mid):
            e = mid
        else:
            s = mid + 1

    return mid

