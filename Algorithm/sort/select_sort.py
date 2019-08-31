'''
算法：选择排序

'''


def select_sort(array):
    new_array = []
    length = len(array)
    for i in range(0, length):
        samil = array[0]
        for j in range(0, length - i):
            if array[j] < samil:
                samil = array[j]
        new_array.append(samil) #每一次都找出最小的，放到新的数组里面
        array.remove(samil)

    return new_array


if __name__ == '__main__':
    array = [2, 3, 4, 1, 9, 6, 5]
    print(select_sort(array))

'''
选择排序算法思想：
（1）从头至尾，遍历序列，找出最小的元素和第一个元素交换，
（2）接着从剩下的元素中继续这种选择和交换方式，最终得到一个有序的序列
'''
