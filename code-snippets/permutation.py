'''
Recursive function may not be recommanded because of stack overflow.
However, permutation can be implemented with recursive function without warring about overflow.
That is because n! grows so fast that it will reach at time limit before it overflows.
'''


def permutation(array):
    '''
    This function returns the array of all available permutations of given array.
    If the given array is sorted in ascending order, the result also will be sorted.
    '''
    l = len(array)
    if l == 1:
        return [array]
    result = []
    for i in range(l):
        sub_array = array[:i]+array[i+1:]
        for sub_result in permutation(sub_array):
            result.append([array[i]]+sub_result)
    return result
