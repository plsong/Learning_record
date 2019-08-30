'''
算法：快速排序

快速排序介绍：
快速排序采用了分而治之（divide and conquer）的策略
    分而治之的策略是：将原有的问题分为若干个规模更小的但是结构和原问题相似的子问题，递归地解决
                     这些子问题，然后将子问题的答案组合为原问题的答案
    快速排序的思想：通过一次排序将未排序的序列分成 独立的两个部分，其中左边部分序列 比  划分值小的，
                右边部分的值 比 划分值 大，此时划分值的位置已经确定，然后对这两个序列按照同样的方法进行排序



'''



'''

#快速排序1
def quick_sort(array):
    if (len(array) < 2):
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot] #小于基准的
        greater = [i for i in array[1:] if i > pivot] #大于基准的

        return quick_sort(less) + [pivot] + quick_sort(greater)

'''

'''
#或者可以写成这样，快速排序2
def quick_sort(array):
    if len(array) < 2:
        return array

    else:
        less = []
        graeter = []
        pivot = array[0]
        for i in range(1, len(array)):
            if array[i] < pivot:
                less.append(array[i])
            else:
                graeter.append(array[i])

        return quick_sort(less) + [pivot] + quick_sort(graeter)
'''

def partition(array,left,right):
    pivot = array[right]

    i=left-1
    for j in range(1,right):
        if array[j]<pivot:
            i+=1
            array[i],array[j]=array[j],array[i]
    array[right],array[i+1] = array[i+1],array[right]

    return  i+1 #返回的是原数组中 pivot的下表








if __name__ == '__main__':
    array = [1,83,42,5543,6,90]
    print(quick_sort(array))
