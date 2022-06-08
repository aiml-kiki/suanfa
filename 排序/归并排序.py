def mergeSort(arr, low, high):
    if low >= high:
        return    # 递归结束

    mid = low + (high - low) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    
    tmp = []
    left, right = low, mid + 1 # 合并两个有序数组，双指针分别指向两个数组的头部
    while left <= mid and right <= high:
        if arr[left] > arr[right]:
            tmp.append(arr[right])
            right += 1

        else:
            tmp.append(arr[left])
            left += 1

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