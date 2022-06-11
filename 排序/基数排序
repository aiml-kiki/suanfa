def radixSort(arr):
    if not arr: 
        return []
    max_ = max(arr)
    # 最大位数
    maxDigit = len(str(max_))
    bucketList = [[] for _ in range(10)]
    
    # 从低位开始排序
    div, mod = 1, 10
    for _ in range(maxDigit):
        for num in arr:
            bucketList[num % mod // div].append(num)
        div *= 10
        mod *= 10
        idx = 0
        for j in range(10):
            for item in bucketList[j]:
                arr[idx] = item
                idx += 1
            bucketList[j] = []
    return arr


if __name__ == '__main__':
    print(radixSort([5, 6, 1, 8, 4, 0]))