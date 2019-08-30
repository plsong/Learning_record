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

if __name__ == '__main__':
    array = [1,83,42,5543,6,90,3,1,4,2,7,54]
    print(quick_sort(array))
