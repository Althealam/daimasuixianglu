# k为输入的右旋的位置，string为输入的字符串
k=int(input())
s=input()

print(s[-k:]+s[:-k])
# 1. s[-k:]：表示倒数第k个元素到最后一个元素
# 2. s[:-k]：表示第一个元素到倒数第k个元素