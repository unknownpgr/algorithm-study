'''
가방의 크기가 s이고, 물건들의 집합이 X라 하자.
이때, knapsack문제의 답을 구해주는 함수를 f(s,X)라 하자.
그렇다면, X의 한 원소 x에 대하여, X를 다음과 같이 나누자.
x in X, Y = Z - {x}
이때 x의 무게를 w, x의 가치를 v라 하자.
그렇다면, 어쨌든 optimal solution은 x를 포함하거나 포함하지 않을 것이다.
x를 포함하는 경우, 자명히 x를 제한 경우에서도 optimal하다. 왜냐하면 x를 제하고서 더욱 optimal한 경우가 있다면, 그것이 optimal이기 때문이다.
따라서 optimal은 f(s-w,Z)+w이다.
x를 포함하지 않는 경우, 자명하다.
f(s,Z)가 optimal이다.
그러므로 optimal은 max(f(s,Z),f(s-w,Z)+w)이다.
이 방법은 가방의 크기를 정수로 제한하지 않는다. 그러므로 더욱 범용적인 솔루션이다.
이때 이 방법이 stack overflow에 빠질 가능성이 있는가?
있기는 하다. 집합 Z가 너무 크면 그렇게 된다.

그리고 어쨌든 완전탐색이면 경우의 수는 2^n가지. 너무 크다. w가 충분히 크다면 사실 그럴 일이 없지만, w가 작다면 충분히 그럴 수 있다.

풀어 보자.

그러고 보면 위의 maximum_fill 문제는 knapsack문제에서 w = s인 특수 케이스였다.
'''

s = 5
n = 5
ws = [1, 2, 3, 4, 5]
vs = [5, 4, 3, 2, 1]

dp = [[-1] * n for _ in range(s+1)]
for i in range(n):
    dp[0][i] = 0


def knapsack(s, i):
    if i < 0:
        return 0
    if s <= 0:
        return 0
    if dp[s][i] >= 0:
        return dp[s][i]
    solution = max(knapsack(s-ws[i], i-1)+vs[i], knapsack(s, i-1))
    dp[s][i] = solution
    return solution


print(knapsack(s, n-1))
