def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        mover = i - 1
        while (mover >= 0) and (arr[mover] > temp):
            arr[mover + 1] = arr[mover]
            mover -= 1
        arr[mover + 1] = temp

    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        small_number = i
        for select in range(i + 1, len(arr)):
            if arr[small_number] > arr[select]:
                small_number = select

        temp = arr[i]
        arr[i] = arr[small_number]
        arr[small_number] = temp

    return arr


arr = [12, 25, 64, 22, 11]
print(insertion_sort(arr))
print(selection_sort(arr))