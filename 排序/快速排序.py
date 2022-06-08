import random


def partition(arr, low, high):
    pivot = random.randint(low, high)
    arr[pivot], arr[low] = arr[low], arr[pivot]
    pivot = arr[low]
    
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
    if low >= hight:
        return 
    
    mid = partition(arr, low, hight)
    quickSort(arr, low, mid - 1)
    quickSort(arr, mid + 1, hight)
    

if __name__ == '__main__':
    nums =[5, 6, 1, 8, 4, 0]
    quickSort(nums, 0, len(nums) - 1)
    print(nums)