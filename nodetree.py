import graphics as gf, settings
class Node:
    arr = None
    def __init__(self, ival, val):
        self.l, self.r = None, None
        self.ival = ival
        self.val = val
    def add(self, ival, val):
        gf.showelem(Node.arr,ival, gf.indexcol)
        gf.tick_and_handleevents()
        if settings.doflush:
            return
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
        gf.showelem(Node.arr,ival, gf.normalcol)
        
    def heapaddnext(self, arr, index):
        gf.tick_and_handleevents()
        if settings.doflush:
            return 0
        i = index
        gf.showelem(arr, self.ival, gf.indexcol)
        if self.l != None:
            i = self.l.heapaddnext(arr, i)
            gf.showelem(arr, i, gf.sortedcol)
        gf.showelem(arr, i, gf.black)
        arr[i] = self.val
        gf.showelem(arr, i, gf.sortedcol)
        i += 1
        if self.r != None:
            gf.showelem(arr, i, gf.sortedcol)
            i = self.r.heapaddnext(arr, i)
        if index > self.ival:
            gf.showelem(arr, self.ival, gf.sortedcol)
        return i