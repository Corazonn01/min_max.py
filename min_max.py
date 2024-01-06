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
for i in range(n):
    while True:
        try:
            element = int(input(f"arr[{i + 1}] = "))
            break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    arr.append(element)

print("Отсортированный массив: ")
average = sum(arr) / len(arr)
print(arr)
print(min(arr))
print(max(arr))
print(average)

