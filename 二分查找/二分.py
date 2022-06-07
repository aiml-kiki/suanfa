class BinarySearch():

    def search_iterative(self, list, item):
        # 左右指针可以理解为要查找值所在的区间
        low = 0
        high = len(list) - 1

        # 指针相遇时停止
        while low <= high:
            # 找到中间值索引
            mid = (low + high) // 2
            guess = list[mid]
            # 比较中间值与目标值
            if guess == item:
                return mid
            # 中间值 ＞ 目标值 =》 目标值在左边区间，右指针左移到中间值前一位
            if guess > item:
                high = mid - 1
            # 中间值 ＜ 目标值 =》 目标值在右边区间，左指针右移到中间值后一位
            else:
                low = mid + 1

        # 遍历完没用返回值 则目标值不在给定数组中
        return None

    def search_recursive(self, list, low, high, item):
        # 递归写法

        # 定义停止条件
        if high >= low:

            # 主要逻辑与正常二分查找类似
            mid = (high + low) // 2
            guess = list[mid]

            if guess == item:
                return mid

            # 中间值 ＞ 目标值 =》 目标值在左边区间，对左区间执行二分查找
            elif guess > item:
                return self.search_recursive(list, low, mid - 1, item)

            # 中间值 ＜ 目标值 =》 目标值在右边区间，对右区间执行二分查找
            else:
                return self.search_recursive(list, mid + 1, high, item)

        else:
            # 递归完没返回值 则目标值不在给定数组中
            return None


if __name__ == "__main__":
    # 初始化二分查找类
    bs = BinarySearch()
    my_list = [1, 3, 5, 7, 9]

    print(bs.search_iterative(my_list, 3))  # 正常版
    print(bs.search_iterative(my_list, 7))  # 递归版