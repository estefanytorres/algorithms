def bubblesort(a):
    swapped = True
    n = len(a)
    tmp = 0
    while (swapped == True):
        swapped = False
        for i in range(0,n-1):
            if a[i] > a[i+1]:
                tmp = a[i]
                a[i] = a[i+1]
                a[i+1] = tmp
                swapped = True

def insertionsort(a):
    n = len(a)
    tmp = 0
    p = 0
    for i in range(1,n):
        p = i
        tmp = a[p]
        while a[p-1] > tmp:
            a[p] = a[p-1]
            p = p-1
            if p == 0: 
                break
        a[p] = tmp
        
def shellsort(a):
    n = len(a)
    tmp = 0
    gap = int(n/2)
    while gap > 0:
        x = gap
        while x < n:
            tmp = a[x]
            while a[x-gap] > tmp:
                a[x] = a[x-gap]
                x = x-gap 
                if x < 0:
                    x = x + gap
                    break
            a[x] = tmp
            x = x+1
        gap = int(gap/2)
        
def mergesort(a):
    tmp = a.copy()
    mergesort_rec(a, tmp, 0, len(a)-1)
    
def mergesort_rec(a, tmp, left_start, right_end):
    if left_start == right_end:
        return
    left_end = left_start+int((right_end-left_start)/2)
    right_start = left_end+1
    mergesort_rec(a, tmp, left_start, left_end)
    mergesort_rec(a, tmp, right_start, right_end)
    mergesort_combine(a, tmp, left_start, left_end, right_start, right_end)
    
def mergesort_combine(a, tmp, left_start, left_end, right_start, right_end):
    i = left_start
    left = left_start
    right = right_start
    while left <= left_end and right <= right_end:
        if a[left] <= a[right]:
            tmp[i] = a[left]
            left = left+1
        else:
            tmp[i] = a[right]
            right = right+1
        i = i+1
    while left <= left_end:
        tmp[i] = a[left]
        left = left+1
        i = i+1
    while right <= right_end:
        tmp[i] = a[right]
        right = right+1
        i = i+1
    i = left_start
    while i <= right_end:
        a[i] = tmp[i]
        i = i+1
        
        
def quicksort(a):
    quicksort_rec(a, 0, len(a)-1)
    
def quicksort_rec(a, start, end):
    if start >= end:
        return
    pivot = start + int((end-start)/2)
    pivot_value = a[pivot]
    quicksort_swap(a, pivot, end)
    left = start
    right = end-1
    i = 1
    while left < right:
        i = i+1
        while left < right and a[left] < pivot_value:
            left = left+1
        while left < right and a[right] >= pivot_value:
            right = right-1
        if left < right: 
            quicksort_swap(a, left, right)
    if a[right] > a[end]:
        pivot = right
        quicksort_swap(a, pivot, end)
    else:
        pivot = end
    quicksort_rec(a,start, pivot-1)
    quicksort_rec(a,pivot+1, end)
    
def quicksort_swap(a, x, y):
    tmp = a[x]
    a[x] = a[y]
    a[y] = tmp
