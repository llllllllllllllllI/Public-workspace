import random
def quick_sort(lst):
    if len(lst) > 1:
        elem = lst[random.randint(0, len(lst) - 1)]
        left = [i for i in lst if i < elem]
        center = [i for i in lst if i == elem]
        right = [i for i in lst if i > elem]
        lst = quick_sort(left) + center + quick_sort(right)
    return lst
def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
a = input ('Введите последовательность чисел:')
while True:
    try:
        a_lst = list(map(int, a.split()))
        break
    except ValueError:
        print('На ввод принимаются только целые числа!')
        a = input('Введите последовательность чисел повторно: ')
element = input('Введите одно число:')
while True:
    try:
        element = int(element)
        break
    except ValueError:
        print('На ввод принимаются только целые числа!')
        element = input('Введите число повторно: ')
if element in a_lst:
    print(a_lst)
else:
    a_lst.append(element)
print(a_lst)
sort_a = quick_sort(a_lst)
print(*sort_a)
if element >= max(sort_a):
    print('Введенное число является максимальным среди чисел последовательности')
    print('Индекс числа:', binary_search(sort_a, element, 0, len(sort_a)))
elif element <= min(sort_a):
    print('Введенное число является минимальным среди чисел последовательности')
    print('Индекс числа:', binary_search(sort_a, element, 0, len(sort_a)))
elif element in sort_a:
    print('Индекс соседнего элемента:', binary_search(sort_a, element, 0, len(sort_a)) - 1)
    print('Индекс введеного элемента:', binary_search(sort_a, element, 0, len(sort_a)))