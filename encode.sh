s = 'aaaabbbbccccceeeeaaa' # str(input())
count = 1
prev = ''
result = ''
for character in s:
    if character != prev:
        if prev:
            string = (str(prev) + str(count))
            result += string
            #print lst
        count = 1
        prev = character
    else:
        count += 1
else:
    string = (str(character) + str(count))
    result += string

print(result)
