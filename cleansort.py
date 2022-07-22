import math, random, tools, time

class Time:
    def __init__(self, t = None, string="Time:       "):
        self.startT = time.time_ns() if not t else t
        self.endT,self.delta, self.deltasec = None,None,None
        if len(string) < 12:
            string = (" " * (12 - len(string)))+string
        self.string = string
    def end(self, endT):
        self.endT = endT
        self.delta = self.endT - self.startT
        self.deltasec = self.delta / 1.0e9
    def endShow(self, endT=None):
        if not endT:
            endT = time.time_ns()
        self.end(endT)
        self.string = self.string + ": " + str(self.deltasec)
        print(self.string)
        return self.deltasec
    def show(self):
        if not self.endT:
            return self.endShow()
        else:
            print(self.string)
            return self.deltasec
class Node:
    arr = None
    def __init__(self, ival, val):
        self.l, self.r = None, None
        self.ival = ival
        self.val = val
    def add(self, ival, val):
        if val < self.val:
            if self.l != None:
                self.l.add(ival,val)
            else:
                self.l = Node(ival, val)
        else:
            if self.r != None:
                self.r.add(ival,val)
            else:
                self.r = Node(ival, val)
        
    def heapaddnext(self, arr, index):
        i = index
        if self.l != None:
            i = self.l.heapaddnext(arr, i)
        arr[i] = self.val
        i += 1
        if self.r != None:
            i = self.r.heapaddnext(arr, i)
        return i

def swap(arr, a, b):#transfer b to a
    arr[a], arr[b] = arr[b], arr[a]

def bublesort(arr):
    for i in range(len(arr)-1):
        issorted = True
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                swap(arr,j,j+1)
                issorted = False
        if issorted:
            break

def quicksort(arr):
    quicksortp(arr, 0, len(arr)-1)
    return arr

def quicksortp(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksortp(arr, low, pi-1)
        quicksortp(arr, pi+1, high)

def partition(arr, low, high):
    i = low
    for j in range(low, high):
        if arr[j] < arr[high]:
            swap(arr, i, j)
            i += 1
    swap(arr, i, high)
    return i

def mergesort(arr):
    _mergesort(arr, 0, len(arr))
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
                break
            if part1[pi1] < part2[pi2]:
                arr[i] = part1[pi1]
                pi1 += 1 
            else:
                arr[i] = part2[pi2]
                pi2 += 1 
            i += 1
        if pi1 != p1len:
            while i < end:
                arr[i] = part1[pi1]
                pi1 += 1
                i += 1
        elif pi2 != p2len:
            while i < end:
                arr[i] = part2[pi2]
                pi2 += 1
                i += 1
        return arr


def insertion_sort(arr):
    if len(arr) < 2:
        return
    for i in range(0, len(arr)-1):
        j = i+1
        while j > 0:
            if arr[j] < arr[i]:
                swap(arr, i, j)
                i -= 1
                j = i + 1
            else:
                break
            
def treesort(arr):
    if len(arr) == 0:
        return
    Node.arr = arr
    base = Node(0,arr[0])
    for i in range(1, len(arr)):
        base.add(i, arr[i])
    base.heapaddnext(arr, 0)

def radiaxsort(arr):
    #get how many digits we need (from get the largest value first)
    arrlen = len(arr)
    maxi = 0
    if arrlen > 2:
        for i in range(1, len(arr)):
            if arr[i] > arr[maxi]:
                maxi = i
    digits = math.log10(arr[maxi])
    if int(digits) != digits:
        digits = int(digits + 1)
    idigits = 0
    while idigits < digits:
        buckets = [[],[],[],[],[],[],[],[],[],[]]
        for i in range(0, arrlen):
            buckets[tools.getdigit(arr[i], idigits+1)].append(arr[i])
        index = 0
        for i in range(0, 10):
            for j in range(0, len(buckets[i])):
                arr[index] = buckets[i][j]
                index += 1
        idigits += 1

def shuff(arr):
    alen = len(arr)
    for _ in range(0, alen * 4):
        a, b = random.randint(0, alen-1), random.randint(0, alen-1)
        swap(arr, a, b)
    
def shuffle(arr):
    shuffle(arr)
    #reverse(arr)

def reverse(arr):
    nlis = arr.copy()
    for i in range(len(arr)-1, -1, -1):
        arr[i] = nlis[len(arr)-1-i]

def createarr(size, min, max, randomized = True):
    lis = [0] * size
    if randomized:
        for i in range(0,size):
            lis[i] = random.randint(min, max)
    else:
        for i in range(0,size):
            lis[i] = i
    return lis

arrsize = 90000
minval = 0
maxval = 99999999
lis = createarr(arrsize, minval, maxval)
times = []
names = []

tm = Time(None,"radiax")
names.append(tm.string)
radiaxsort(lis)
times.append(tm.show())
shuffle(lis)
treesort(lis)



for i in range(0, len(times)-1):
    for j in range(i, len(times)-1):
        if times[j] > times[j+1]:
            swap(times,j,j+1)
            swap(names,j,j+1)
print("lis view")
for i in range(0, len(times)):
    print(names[i]+":"+str(times[i]))
