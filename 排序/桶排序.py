def bucket_sort(arr, bucketSize):
    if len(arr) < 2:
        return arr
    min_ = min(arr)
    max_ = max(arr)
    
    # 需要桶个数
    bucketNum = (max_ - min_) // bucketSize + 1
    buckets = [[] for _ in range(bucketNum)]
    
    for num in arr:
        # 放入相应的桶中
        buckets[(num - min_) // bucketSize].append(num)
    res = []

    for bucket in buckets:
        if not bucket: 
            continue
        if bucketSize == 1:
            res.extend(bucket)
        else:
            # 当都装在一个桶里,说明桶容量大了
            if bucketNum == 1:
                bucketSize -= 1
            res.extend(bucket_sort(bucket, bucketSize))
    return res
