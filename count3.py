a = int(input())
b = int(input())

ran1 = range(a, b+1)
u = 0
n = 0
for i in ran1:
        if i % 3 == 0:
                n = (n + i)
                u = (u + 1)
print(n / u)
