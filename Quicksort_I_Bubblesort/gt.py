# Julia Nowak 407203
from timeit import timeit
import random
from typing import List, Tuple


# zadanie 1 - Quicksort
def quicksort(unsorted_list: List[int]) -> List[int]:
    def inner_quicksort(inner_ul: List[int], beginning: int, end: int) -> List[int]:
        b = beginning
        e = end
        pivot = inner_ul[(b + e) // 2]
        while b < e:
            while inner_ul[b] < pivot:
                b += 1
            while inner_ul[e] > pivot:
                e -= 1
            if b <= e:
                inner_ul[b], inner_ul[e] = inner_ul[e], inner_ul[b]
                b += 1
                e -= 1
        if beginning < e:
            inner_quicksort(inner_ul, beginning, e)
        if b < end:
            inner_quicksort(inner_ul, b, end)
        return inner_ul
    replica = unsorted_list[:]
    return inner_quicksort(replica, 0, len(replica)-1)


# zadanie 2 - Bubblesort
def bubblesort(unsorted_list: List[int]) -> Tuple[List[int], int]:
    ul = unsorted_list[:]
    counter = 0
    length = len(ul)-1
    is_sorted = False
    while is_sorted is False:
        is_sorted = True
        for x in range(0, length):
            if ul[x] > ul[x+1]:
                ul[x], ul[x+1] = ul[x+1], ul[x]
                counter += 1
                is_sorted = False
    answer = (ul, counter)
    return answer


lista = []

for i in range(12):
    los = random.randint(1, 1000)
    lista.append(los)

print(lista)
print(bubblesort(lista))
print(lista)

lista2 = []

for i in range(12):
    los = random.randint(1, 1000)
    lista2.append(los)

print('\n')
print(lista2)
print(quicksort(lista2))
print(lista2)

# zadanie 3 - dane wejściowe
sorted_list = list(range(1, 1001))
reversed_sorted_list = sorted_list[::-1]
same_values_list = [random.randint(1, 10)]*1000
random_values_list = random.sample(range(1, 1001), 1000)

# zadanie 4 - pomiar czasu
sum1bs, sum1qs, sum2bs, sum2qs, sum3bs, sum3qs, sum4bs, sum4qs = 0, 0, 0, 0, 0, 0, 0, 0
for i in range(1000):
    sorted_list = list(range(1, 101))
    t1_bubblesort = timeit("bubblesort(sorted_list)", number=1, globals=globals())
    sum1bs += t1_bubblesort
    t1_quicksort = timeit("quicksort(sorted_list)", number=1, globals=globals())
    sum1qs += t1_quicksort
print('Bubblesort - lista posortowana: {0}'.format(sum1bs/1000))
print('Quicksort - lista posortowana: {0}\n'.format(sum1qs/1000))
for i in range(1000):
    reversed_sorted_list = sorted_list[::-1]
    t2_bubblesort = timeit("bubblesort(reversed_sorted_list)", number=1, globals=globals())
    sum2bs += t2_bubblesort
    t2_quicksort = timeit("quicksort(reversed_sorted_list)", number=1, globals=globals())
    sum2qs += t2_quicksort
print('Bubblesort - lista posortowana odwrócona: {0}'.format(sum2bs/1000))
print('Quicksort - lista posortowana odwrócona: {0}\n'.format(sum2qs/1000))
for i in range(1000):
    same_values_list = [random.randint(1, 10)] * 100
    t3_bubblesort = timeit("bubblesort(same_values_list)", number=1, globals=globals())
    sum3bs += t3_bubblesort
    t3_quicksort = timeit("quicksort(same_values_list)", number=1, globals=globals())
    sum3qs += t3_quicksort
print('Bubblesort - lista o jednakowych wartościach: {0}'.format(sum3bs/1000))
print('Quicksort - lista o jednakowych wartościach: {0}\n'.format(sum3qs/1000))
for i in range(1000):
    random_values_list = random.sample(range(1, 101), 100)
    t4_bubblesort = timeit("bubblesort(random_values_list)", number=1, globals=globals())
    sum4bs += t4_bubblesort
    t4_quicksort = timeit("quicksort(random_values_list)", number=1, globals=globals())
    sum4qs += t4_quicksort
print('Bubblesort - lista o losowych wartościach: {0}'.format(sum4bs/1000))
print('Quicksort - lista o losowych wartościach: {0}'.format(sum4qs/1000))

# zadanie 5 - rezultaty
# Lista posortowana - szybciej posortuje ją Bubblesort
# Lista posortowana odwrócona - szybciej posortuje ją Quicksort
# Lista o jednakowych wartościach - szybciej posortuje ją Bubblesort
# Lista o losowych wartościach - szybciej posortuje ją Quicksort
# Otrzymane wyniki są zgodne z teorią
