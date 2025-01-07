# 时间复杂度：O(n)
# 空间复杂度：O(n)
# （1）result会拼接字符，因此会占据空间

s=input()

def replace_digits(s):
    result=""
    for char in s:
        if char.isdigit():
            result+="number"
        else:
            result+=char
    return result

result=replace_digits(s)
print(result)