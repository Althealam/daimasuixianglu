s=input()
res=list(s)
for i in range(len(res)):
    if res[i].isdigit():
        res[i]='number'
print(''.join(res))