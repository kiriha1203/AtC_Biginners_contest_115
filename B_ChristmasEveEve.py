n = int(input())
pay = []
for count in range(n):
    pay.append(int(input()))

pay.sort(reverse=True)
pay[0] //= 2
print(sum(pay))