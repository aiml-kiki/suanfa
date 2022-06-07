def quicksort(array):
    if len(array) < 2:
        # 数组元素个数为1，0时不用排序
        return array
    else:
        # 迭代条件，选择基准
        pivot = array[0]
        # 原数组中小于基准的子数组
        less = [i for i in array[1:] if i <= pivot]
        # 原数组中大于基准的子数组
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3]))
