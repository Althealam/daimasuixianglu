# k为输入的右旋的位置，string为输入的字符串
k=int(input())
s=input()

print(s[-k:]+s[:-k])
