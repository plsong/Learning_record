'''
算法：冒泡排序

'''

def bubble_sort(array):
    length = len(array)
    for i in range(length-1):
        for j in range(length - i -1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

if __name__ == '__main__':
    array=[1333,23,3,55,4,90,893274,444,4,2345,65]
    print(bubble_sort(array))


'''
冒泡排序的步骤：
（1）比较相邻的元素，如果第一个比第二个大，就交换他们两个
（2）对每一对相邻的元素重复以上步骤，除了最后一个

冒泡排序的时间复杂度：O(n^2)
'''