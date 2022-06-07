# 找到数组中最小的元素
def findSmallest(arr):
    # 保存最小元素
    smallest = arr[0]
    # 最小元素对应的索引
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index


# 数组排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # 找到数组最小的数，并加入到新数组的尾部
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))
