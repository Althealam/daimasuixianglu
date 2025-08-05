k = int(input())
string = str(input())

s = string[len(string)-k:]+string[:len(string)-k]
print(s)