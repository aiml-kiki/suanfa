def find_max(arr):
    # 停止条件
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    # 递归
    sub_max = find_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(find_max([23, 123, 2, 12, 3123, 23, 1231, 21]))