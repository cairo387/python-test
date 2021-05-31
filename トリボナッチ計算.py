# PYTHON_TRIBONACCI-1

# トリボナッチ数列生成関数
def tribonacci_list(n, t0, t1, t2):
    tri = [t0, t1, t2]
    if n == 1:
        tri = [t0]
    elif n == 2:
        tri = [t0, t1]
    else:
        for k in range(3, n):
            tri.append(tri[k-1]+tri[k-2]+tri[k-3])
    return tri
# PYTHON_TRIBONACCI-2

# 1,1,2から始まる10項のトリボナッチ数列
tri = tribonacci_list(30, 1, 0, 5)

print(tri)