# Nome: Lucas Batista Pereira
# Matricula: 2020007290
# Trabalho 01 - COM 220.1 - 08/09/2021

import random
import time

# Partição de quicksort
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

# Call para QuickSort
def quick_sort(array, start, end):
    if start >= end:
        return
    
    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)

# BubbleSort
def bubbleSort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]


# Main
lista1 = [] # <- Lista 1 & 2, idênticas, usadas individualmente no Quick e bubble
lista2 = []
size_list = 10000 # <-Tamanho do vetor

for i in range(0,size_list):
    n = random.randint(1,100000)
    lista1.append(n)
    lista2.append(n)

inicio = time.time()
quick_sort(lista1, 0, size_list - 1)
fim = time.time()
delta = (fim - inicio) * 1000
print("Quicksort de vetor com",size_list,"elementos - Tempo de execução em milisegundos:", delta)

inicio = time.time()
bubbleSort(lista2)
fim = time.time()
delta = (fim - inicio) * 1000
print("BubbleSort de vetor com",size_list,"elementos - Tempo de execução em milisegundos:", delta)