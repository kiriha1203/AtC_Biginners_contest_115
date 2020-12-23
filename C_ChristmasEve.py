n, k = map(int, input().split())

ans = 999999999
trees = []
for count in range(n):
    trees.append(int(input()))

trees.sort()

for i in range(n - k + 1):
    ans = min(ans, trees[i + k - 1] - trees[i] )

print(ans)