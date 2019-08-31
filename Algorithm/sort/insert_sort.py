'''
算法：插入排序

'''

def insert_sort(array):
    length=len(array)

    for i in range(length):

        preIndex=i-1
        current=array[i]
        while preIndex>=0 and array[preIndex]>current:
            array[preIndex+1] = array[preIndex]
            preIndex-=1
        array[preIndex+1]=current
    return array

if __name__ == '__main__':
    array=[3,7,1,2]
    print(insert_sort(array))


'''
(1) 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列
(2) 从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置,
（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
'''
