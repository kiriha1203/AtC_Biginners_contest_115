# f(0) = p
# f(1) = b f(0) p f(0) b

#f(n) = b f(n-1) p f(n-1) b 

# lv0 p  0, 1   
# lv1 bpppb 2,3           f(1) = 2           f(1) = 3         
# lv2 bbpppbpbpppbb 6,7   f(2)= 2f(2-1) + 2   f(2) = 2f(2-1) + 1  
# lv3 bbbpppbpbpppbbpbbpppbpbpppbbb  15, 14
# lv4 bbbbpppbpbpppbbpbbpppbpbpppbbbpbbbpppbpbpppbbpbbpppbpbpppbbbb 30, 31 
# lv5 bbbbbpppbpbpppbbpbbpppbpbpppbbbpbbbpppbpbpppbbpbbpppbpbpppbbbbpbbbbpppbpbpppbbpbbpppbpbpppbbbpbbbpppbpbpppbbpbbpppbpbpppbbbbb 63, 62
# lv6 127, 126


# 1 1 p 1 1
# 2 3 1 p 1 3 2
# 3 3 1 1 1 3 2 p 
# 4 3 1 1 1 3 2 1 2 3 1 1 1 3 3 p
# 5 3 1 1 1 3 2 1 2 2 3 1 1 1 3 3 1 3 3 1 1 1 3 2 1 2 3 1 1 1 3 4 p


# 1 5 13 29 61 

n, x = map(int, input().split())

def bagger(low_bagger):
    return 2 * low_bagger + 3

def pbagger(plow_bagger):
    return 2 * plow_bagger + 1
   
allcount = 1
targetcount = 0
p = 3

for i in range(1, n + 1):
    allcount = bagger(allcount)

for i in range(1, n - 1):
    p = pbagger(p)


print(allcount)
print(f'p {p}')

def strbagger(a):
    return f'b{a}p{a}b'

temp = 'p'
for i in range(1, n):
    temp = strbagger(temp)

if (x > allcount / 2 ):
    temp1 = temp.join('p')
    temp2 = x - (allcount - 1) / 2
    print(p)
    targetcount =  p + 1 - temp1[:temp2].count('p')
else:
    targetcount = p + 1 + p - temp[:x - 1].count('p')

print(targetcount)



# def bagger(low_bagger):
#    return f'b{low_bagger}p{low_bagger}b'

# ans = 0
# temp = 'p'

# for i in range(1,n + 1):
#     temp = bagger(temp)

# print(temp)
# p = temp.count('p')
# b = temp.count('b')
# print(p)
# print(b)

# print(temp[:x].count('p'))