def insertionSort(arr):

    for i in range(len(arr)):
        preIndex = i - 1  # arr[:i-1] 为有序数组
        current = arr[i]  # 待排序值
        
        while preIndex >= 0 and arr[preIndex] > current:  # 找到比待排小的索引 或者数组头部
            arr[preIndex + 1] = arr[preIndex] # 排序数组中大于待排值的后移
            preIndex -= 1  # 前向遍历
        
        arr[preIndex + 1] = current  # 插入
    
    return arr

if __name__ == '__main__':
    print(insertionSort([5, 6, 1, 8, 4, 0]))