def quickSort(arr, left=None, right=None):
    
    # 确定子序列起止范围
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    
    # 递归执行分区排序
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
    
    return arr


def partition(arr, left, right):
    
    # 分区并排序 
    pivot = left  # 基准
    index = pivot + 1
    i = index
    
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index += 1
        
        i += 1
    
    swap(arr, pivot, index - 1)
    
    return index - 1


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    

if __name__ == '__main__':
    print(quickSort([5, 6, 1, 8, 4, 0]))