def bubble_sort(array):
    length = len(array)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


arr = []
while True:
    try:
        n = int(input("Напишите несколько цифр: "))
        if n > 0:
            break
    except NameError and ValueError:
        print("Пожалуйста введите число")

for i in range(0, n):
    element = int(input("arr[" + str(i + 1) + "] = "))
    arr.append(element)
bubble_sort(arr)
print("Отсортированный массив: ")
average = sum(arr) / len(arr)
print(arr)
print(min(arr))
print(max(arr))
print(average)

