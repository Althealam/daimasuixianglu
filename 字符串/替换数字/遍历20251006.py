s = str(input())
string_list = list(s)

for i in range(len(string_list)):
    if string_list[i].isdigit():
        string_list[i] = 'number'
print(''.join(string_list[:]))