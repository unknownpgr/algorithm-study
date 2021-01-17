'''
이 스크립트의 목표는 0~n-1까지의 n개 숫자를 나열하는 순열을 최대한 효율적으로 생성하는 것이다.
특히 back-tracking에 사용할 수 있도록 순열을 트리 형태로 생성하고자 한다.
'''


def pr1(n):
    '''
    (생성된 순열,아직 사용하지 않은 숫자 배열)
    의 튜플을 사용하여, 사용하지 않은 숫자 배열에서 하나씩 수를 꺼내어 사용한다.
    따라서 배열의 길이가 처음에는 0이다가 점점 길어진다.
    '''
    q = [([], list(range(n)))]
    r = []
    while len(q) > 0:
        p, u = q.pop()
        if len(u) > 0:
            for i in range(len(u)):
                t = p[:]
                t.append(u[i])
                q.append((t, u[:i]+u[i+1:]))
        else:
            r.append(p)
    return r


def pr2(n):
    '''
    (숫자의 배열, 치환할 인덱스)
    의 튜플을 사용하여, 처음에는 오름차순으로 정렬된 배열을 사용하여, 치환할 인덱스와 치환할 인덱스 이상의 수를 치환하여
    새로운 배열을 생성한다.
    따라서 배열의 길이는 항상 일정하다.
    '''
    q = [(list(range(n)), 0)]
    r = []
    while len(q) > 0:
        a, i = q.pop()
        m = i+1
        if m == n:
            r.append(a)
        else:
            q.append((a, m))
            for j in range(m, n):
                b = a[:]
                b[i], b[j] = b[j], b[i]
                q.append((b, m))
    return r
