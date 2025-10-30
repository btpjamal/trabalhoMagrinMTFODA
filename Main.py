import random
import time

data = []
quantidade = 20000
inicio = 1
fim = 20000

for _ in range(quantidade):
    data.append(random.randint(inicio, fim))



def bubble_sort(arr):
    lst = arr.copy()
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def bubble_sort_no_optimizations(arr):
    lst = arr.copy()
    n = len(lst)
    for i in range(n):
        for j in range(n - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def selection_sort(arr):
    lst = arr.copy()
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

def insertion_sort(arr):
  lst = arr.copy()
  n = len(lst)
  for i in range(1,n):
    insert_index = i
    current_value = lst.pop(i)
    for j in range(i-1, -1, -1):
      if lst[j] > current_value:
        insert_index = j
    lst.insert(insert_index, current_value)
  return lst

def quick_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def tim_sort(dados):
    lista = list(dados)
    lista.sort()
    return lista


def medir_tempos(data, funcoes, repeticoes=5):
    resultados = {}
    for nome, func in funcoes:
        tempos = []
        for _ in range(repeticoes):
            arr = data.copy()
            t0 = time.perf_counter()
            func(arr)
            t1 = time.perf_counter()
            tempos.append(t1 - t0)
        resultados[nome] = sum(tempos) / len(tempos)
    return resultados

if __name__ == "__main__":
    funcoes = [
        ("BubbleSort", bubble_sort),
        ("BubbleSortNoOptimizations", bubble_sort_no_optimizations),
        ("SelectionSort", selection_sort),
        ("InsertionSort", insertion_sort),
        ("QuickSort", quick_sort),
        ("MergeSort", merge_sort),
        ("TimSort", tim_sort),
    ]

    repeticoes = 1
    tempos = medir_tempos(data, funcoes, repeticoes)

    
    ordem_desejada = [
        "BubbleSortNoOptimizations",
        "BubbleSort",
        "SelectionSort",
        "InsertionSort",
        "QuickSort",
        "MergeSort",
        "TimSort"
    ]
    
    for nome_algoritmo in ordem_desejada:
        if nome_algoritmo in tempos:
            t = tempos[nome_algoritmo]
            print(f"lista original: {data[0:10]}")
            print(f"{nome_algoritmo}: {t * 1000:.3f} ms (média de {repeticoes} runs)")

    
    mais_rapido = min(tempos.items(), key=lambda x: x[1])
    print(f"Mais rápido: {mais_rapido[0]} ({mais_rapido[1] * 1000:.3f} ms)")
