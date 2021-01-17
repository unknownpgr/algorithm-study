def permutation(n, f):
    queue = [([], list(range(n)))]
    results = []
    while len(queue) > 0:
        permutation_list, unused_number = queue.pop()
        len_u = len(unused_number)
        len_t = len(permutation_list)+1
        if len_u > 0:
            for i in range(len_u):
                temp = permutation_list[:]
                temp.append(unused_number[i])
                if not f(temp, len_t):
                    continue
                queue.append((temp, unused_number[:i]+unused_number[i+1:]))
        else:
            results.append(permutation_list)
    return results


def main1(n=8):
    def back_tracking_check(p, l):
        # Check if queens are on same diagonal.
        if l == 0:
            return True
        adds = {}
        subs = {}
        for i in range(l):
            add = i+p[i]
            sub = i-p[i]
            if add in adds:
                return False
            if sub in subs:
                return False
            adds[add] = True
            subs[sub] = True
        return True

    r = permutation(n, back_tracking_check)

    for case in r:
        for i in range(n):
            row = ['□']*n
            row[case[i]] = 'Q'
            print(' '.join(row))
        print()

    return r


print('START!')
print(len(main1(8)))
