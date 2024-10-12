import random
import time

def selection_sort(alist):
    size = len(alist)
    comparisons = 0
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if alist[j] < alist[min_index]:
                min_index = j
            comparisons += 1
        (alist[ind], alist[min_index]) = (alist[min_index], alist[ind])
    return comparisons

def insertion_sort(alist):
    size = len(alist)
    comparisons = 0
    for i in range(1, size):
        j = i
        while j > 0:
            comparisons += 1
            if alist[j] < alist[j - 1]:
                temp = alist[j]
                alist[j] = alist[j - 1]
                alist[j - 1] = temp
            else:
                break
            j -= 1
        i += 1
    return comparisons
def main():

    for num in [1000, 2000, 4000, 8000, 16000, 32000]:
        random.seed(1234)
        randoms = random.sample(range(1000000), num)  # Generate num random numbers from 0 to 999,999
        start_time = time.time()
        comps = insertion_sort(randoms)
        stop_time = time.time()
        print("n:", num, "- comps:", comps, "- time:", stop_time - start_time)

if __name__ == '__main__': 
    main()

