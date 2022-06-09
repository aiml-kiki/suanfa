def mergeSort(arr, low, high):
    if low >= high:  # 递归结束条件
        return    

    # 将数组从中间分为两个子数组，并递归条用归并排序
    mid = low + (high - low) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    
    # 合并两个有序数组，双指针分别指向两个数组的头部，较小的值依次添加到临时列表中
    tmp = []
    left, right = low, mid + 1 
    while left <= mid and right <= high:
        if arr[left] > arr[right]:
            tmp.append(arr[right])
            right += 1

        else:
            tmp.append(arr[left])
            left += 1

    # 继续添加上一步剩下的数
    while left <= mid:
        tmp.append(arr[left])
        left += 1
        
    while right <= high:
        tmp.append(arr[right])
        right += 1
        
    arr[low: high + 1] = tmp


if __name__ == '__main__':
    nums =[5, 6, 1, 8, 4, 0]
    mergeSort(nums, 0, len(nums) - 1)
    print(nums)