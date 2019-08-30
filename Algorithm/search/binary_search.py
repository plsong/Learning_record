'''
算法：二分查找
对于已经排好序的序列，查找某个值的下标，采用二分查找法
'''

def binary_rearch(list,target):
    low = 0
    high = len(list)-1

    while high>=low:
        mid = (low+high )//2
        guses = list[mid]

        if guses == target:
            return mid
        if guses > target:
            high = mid-1
        if guses < target:
            low = mid+1
    return None # 没有找到

if __name__ == '__main__':
    a=[1,2,3,4,5,6,7]
    print(binary_rearch(a,7))
    print(binary_rearch(a,8))

'''
二分查找的步骤：
    每次都将列表中的中间的值与查找目标进行比较，这样就可以排除一半

二分查找仅当列表是有序的时候才管用

时间复杂度：
    二分查找的时间复杂度O(logn)
    简单查找的时间复杂度O(n)

'''