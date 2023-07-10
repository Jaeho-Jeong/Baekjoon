N, M = map(int, input().split())
progress = [[0] * 3 for _ in range(2)]
ret = 0

def dfs(day, total, prevJ):
    if day == N:
        if total >= M:
            ret += 1
        return
    for i in range(2):
        for j in range(3):
            nextTotal = total
            if j == prevJ:
                nextTotal += progress[i][j] // 2
            else:
                nextTotal += progress[i][j]
            dfs(day + 1, nextTotal, j)

for i in range(2):
    progress[i] = list(map(int, input().split()))

dfs(0, 0, -1)
print(ret)
