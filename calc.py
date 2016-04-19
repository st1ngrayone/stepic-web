a = 2#int(input())
b = 4#int(input())
c = 4#int(input())
d = 9#int(input())

ran1 = range(a, b+1)
ran2 = range(c, d+1)

for i in ran2:
        print('\t', i, end='')
for j in ran1:
        print('\n', j, '\t', end='')
        for n in ran2:
                print((n * j), '\t', end='')
