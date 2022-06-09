import random


def partition(arr, low, high):
    # 随机选择数组中的一个数作为基准，并将其放到数组最前
    pivot = random.randint(low, high)  
    arr[pivot], arr[low] = arr[low], arr[pivot]  
    pivot = arr[low]
    
    # 利用双指针将大于基准的数放到基准的左边，反之。。。
    left, right = low, high
    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
        
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    
    arr[left] = pivot
    
    return left

def quickSort(arr, low, hight):
    # 递归
    if low >= hight:
        return 
    
    mid = partition(arr, low, hight)
    quickSort(arr, low, mid - 1)
    quickSort(arr, mid + 1, hight)
    

if __name__ == '__main__':
    nums =[5, 6, 1, 8, 4, 0]
    quickSort(nums, 0, len(nums) - 1)
    print(nums)