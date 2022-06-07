def countdown(i):
    # 停止条件
    if i <= 0:
        return 0
    # 递归条件
    else:
        print(i)
        return countdown(i-1)

countdown(5)
