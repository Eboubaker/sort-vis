import math, numpy
import graphics as gf,settings, tools
from nodetree import Node

def swap(arr, a, b):#transfer b to a
    arr[a], arr[b] = arr[b], arr[a]

def bublesort(arr):
    for i in range(len(arr)-1):
        issorted = True
        for j in range(len(arr)-1-i):
            gf.showelem(arr, j+1, gf.black)
            gf.showelem(arr, j, gf.black)
            gf.showelem(arr, j+1,gf.indexcol)
            gf.showelem(arr, j,gf.normalcol)
            if arr[j] > arr[j+1]:
                gf.showelem(arr, j, gf.black)
                gf.showelem(arr, j+1, gf.black)
                swap(arr,j,j+1)
                gf.showelem(arr, j, gf.normalcol)
                gf.showelem(arr, j+1, gf.indexcol)
                issorted = False
            else:
                gf.showelem(arr, j, gf.black)
                gf.showelem(arr, j ,gf.secondarycol)
            gf.tick_and_handleevents()
            if settings.doflush:
                return
        if issorted:
            for i in range(i, len(arr)):
                gf.showelem(arr, i, gf.sortedcol)
            break
        gf.showelem(arr, len(arr)-i-1, gf.sortedcol)
    gf.showelem(arr, 0, gf.sortedcol)

def quicksort(arr):
    quicksortp(arr, 0, len(arr)-1)
    return arr

def quicksortp(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        if(settings.doflush):
            return
        quicksortp(arr, low, pi-1)
        if(settings.doflush):
            return
        quicksortp(arr, pi+1, high)
        if(settings.doflush):
            return
    else:
        gf.showelem(arr, high, gf.sortedcol)

def partition(arr, low, high):
    i = low
    oi = i
    gf.showelem(arr, high, gf.indexcol)
    gf.showelem(arr, i, gf.secondarycol)
    gf.showelem(arr, low, gf.indexcol)
    for j in range(low, high):
        gf.showelem(arr, j+1,gf.indexcol)
        gf.showelem(arr, j,gf.normalcol)
        if arr[j] < arr[high]:
            swap(arr, i, j)
            gf.showelem(arr, j, gf.normalcol)
            gf.showelem(arr, i, gf.normalcol)
            i += 1
            gf.showelem(arr, i, gf.secondarycol)
        gf.tick_and_handleevents()
        if(settings.doflush):
            return 0
        
    gf.showelem(arr, i, gf.normalcol)
    gf.showelem(arr, high-1, gf.normalcol)
    
    swap(arr, i, high)
    gf.showelem(arr, i, gf.sortedcol)
    gf.showelem(arr, high, gf.normalcol)
    return i

def mergesort(arr):
    _mergesort(arr, 0, len(arr))
    for i in range(0, len(arr)):
        gf.showelem(arr, i, gf.sortedcol)
    return arr

def _mergesort(arr, start, end):
    if end - start < 3:
        if arr[start] > arr[start+1]:
            swap(arr, start, start+1)
        return arr
    else:
        mid = int((start+end)/2)
        part1 = _mergesort(arr, start, mid)[start:mid]
        part2 = _mergesort(arr, mid, end)[mid:end]
        pi1, pi2 = 0,0
        p1len, p2len = len(part1), len(part2)
        i = start
        while i < end:
            if pi1 == p1len or pi2 == p2len:
                gf.showelem(arr, start+p1len-1, gf.normalcol)
                gf.showelem(arr, mid+p2len-1, gf.normalcol)
                break
            gf.showelem(arr, start+pi1, gf.indexcol)
            gf.showelem(arr, mid+pi2, gf.indexcol)
            gf.tick_and_handleevents()
            if settings.doflush:
                return
            if part1[pi1] < part2[pi2]:
                arr[i] = part1[pi1]
                gf.showelem(arr, i, gf.normalcol)
                gf.showelem(arr, start+pi1, gf.normalcol)
                pi1 += 1 
            else:
                arr[i] = part2[pi2]
                gf.showelem(arr, i, gf.normalcol)
                gf.showelem(arr, mid+pi2, gf.normalcol)
                pi2 += 1 
            i += 1
        if pi1 != p1len:
            while i < end:
                gf.showelem(arr, start+pi1, gf.indexcol)
                arr[i] = part1[pi1]
                gf.tick_and_handleevents()
                if settings.doflush:
                    return
                gf.showelem(arr, i, gf.normalcol)
                gf.showelem(arr, start+pi1, gf.normalcol)
                pi1 += 1
                i += 1
        elif pi2 != p2len:
            while i < end:
                gf.showelem(arr, mid+pi2, gf.indexcol)
                arr[i] = part2[pi2]
                gf.showelem(arr, i, gf.normalcol)
                gf.showelem(arr, mid+pi2, gf.normalcol)
                gf.tick_and_handleevents()
                if settings.doflush:
                    return
                pi2 += 1
                i += 1
        return arr


def insertion_sort(arr):
    if len(arr) < 2:
        return
    for i in range(0, len(arr)-1):
        gf.showelem(arr, i, gf.indexcol)
        j = i+1
        gf.showelem(arr, j, gf.secondarycol)
        while j > 0:
            gf.tick_and_handleevents()
            if settings.doflush:
                return
            if arr[j] < arr[i]:
                gf.showelem(arr, i, gf.black)
                gf.showelem(arr, j, gf.black)
                swap(arr, i, j)
                gf.showelem(arr, i, gf.normalcol)
                gf.showelem(arr, j, gf.normalcol)
                i -= 1
                j = i + 1
                gf.showelem(arr, i, gf.indexcol)
                gf.showelem(arr, j, gf.secondarycol)
            else:
                break
            if settings.doflush:
                return
        gf.showelem(arr, i, gf.sortedcol)
        gf.showelem(arr, i+1, gf.normalcol)
    for i in range(0, len(arr)):
        gf.showelem(arr, i, gf.sortedcol)
            
def treesort(arr):
    if len(arr) == 0:
        return
    Node.arr = arr
    base = Node(0,arr[0])
    gf.tick_and_handleevents()
    for i in range(1, len(arr)):
        base.add(i, arr[i])
    base.heapaddnext(arr, 0)

def radiaxsort(arr):
    #get how many digits we need (from get the largest value first)
    arrlen = len(arr)
    maxi = 0
    if arrlen > 2:
        for i in range(1, len(arr)):
            gf.showelem(arr, i, gf.indexcol)
            if arr[i] > arr[maxi]:
                gf.showelem(arr, maxi, gf.normalcol)
                maxi = i
                gf.showelem(arr, maxi, gf.secondarycol)
            gf.tick_and_handleevents()
            gf.showelem(arr, i-1, gf.normalcol)
            if settings.doflush:
                return
    gf.showelem(arr, maxi, gf.normalcol)
    gf.showelem(arr, len(arr)-1, gf.normalcol)
    digits = math.log10(arr[maxi])
    if int(digits) != digits:
        digits = int(digits + 1)
    idigits = 0
    while idigits < digits:
        buckets = [[],[],[],[],[],[],[],[],[],[]]
        for i in range(0, arrlen):
            gf.showelem(arr, i, gf.secondarycol)
            buckets[tools.getdigit(arr[i], idigits+1)].append(arr[i])
            gf.tick_and_handleevents()
            if settings.doflush:
                return
            gf.showelem(arr, i-1, gf.normalcol)
        index = 0
        for i in range(0, 10):
            for j in range(0, len(buckets[i])):
                gf.showelem(arr, index, gf.indexcol)
                arr[index] = buckets[i][j]
                if settings.doflush:
                    return
                gf.tick_and_handleevents()
                gf.showelem(arr, index, gf.black)
                gf.showelem(arr, index-1, gf.normalcol)
                index += 1
        idigits += 1


