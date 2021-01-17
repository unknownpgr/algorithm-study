def permutation(n, f):
    queue = [([], list(range(n)))]
    results = []
    while len(queue) > 0:
        p, u = queue.pop()
        len_u = len(u)
        len_t = len(p)+1
        if len_u > 0:
            for i in range(len_u):
                temp = p[:]
                temp.append(u[i])
                if not f(temp, len_t):
                    continue
                queue.append((temp, u[:i]+u[i+1:]))
        else:
            results.append(p)
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
print(len(main1(10)))
