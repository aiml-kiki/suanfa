def selectionSort(arr):
    for i in range(len(arr) - 1):
        minIndex = i  # 记录最小数的索引

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j

        if i != minIndex:  # i 不是最小数时，将 i 和最小数进行交换
            arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr


if __name__ == '__main__':
    print(selectionSort([5, 6, 1, 8, 4, 0]))