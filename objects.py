a = [1, 4, 5, 6, 9]
b = [2, 1, 5, 10, 12]
result = []
 
for i in b:
    if i in a:
        result.append(i)
print(len(result))
