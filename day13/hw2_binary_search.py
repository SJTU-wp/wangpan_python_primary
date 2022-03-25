# author: wp
# 2022年02月28日 21:44

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        elif target == arr[mid]:
            return mid
    return '目标值不在该数组中'


if __name__ == '__main__':
    arr_search = [2, 10, 23, 37, 65, 77, 85, 86, 86, 99]
    print("目标值在该数组中的位置索引为：", binary_search(arr_search, 37))
    print("目标值在该数组中的位置索引为：", binary_search(arr_search, 30))
