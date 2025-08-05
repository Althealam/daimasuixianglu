string = list(str(input()))

for i in range(len(string)):
    if string[i].isdigit():
        string[i] = 'number'

print(''.join(string))