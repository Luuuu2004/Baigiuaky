def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

arr = list(map(int, input("Nhập danh sách số, cách nhau bằng dấu cách: ").split()))
bubble_sort(arr)
print("Mảng sau khi sắp xếp:", arr)