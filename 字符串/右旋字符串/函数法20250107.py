# k为输入的右旋的位置，string为输入的字符串
k=int(input())
s=input()

def spiral_str(s,k):
    """
    :param s:字符串
    :param k:旋转的位置
    """
    return s[len(s)-k:]+s[:len(s)-k]
print(spiral_str(s,k))

