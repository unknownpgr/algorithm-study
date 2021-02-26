def search_bin_unique(array, target):
    l = 0
    r = len(array)-1
    while l <= r:
        m = (r+l)//2
        if(array[m] == target):
            return m
        if array[m] > target:
            r = m-1
        else:
            l = m+1
    return -1


def search_bin_first(array, target):
    l = 0
    r = len(array)-1
    while l <= r:
        m = (l+r)//2
        if array[m] < target:
            l = m+1
        else:
            r = m-1
    if array[l] != target:
        return -1
    return l


def search_bin_last(array, target):
    l = 0
    r = len(array)-1
    while l <= r:
        m = (l+r)//2
        if array[m] <= target:
            l = m+1
        else:
            r = m-1
    if array[r] != target:
        return -1
    return r
