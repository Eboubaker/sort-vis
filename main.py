import random, math, pygame as pg
from sys import stdout
import graphics as gf, settings, sort as sorter
#cdll.LoadLibrary(r"C:\Users\MCS\AppData\Local\Programs\Python\Python38\Lib\site-packages\pyglet_ffmpeg2\Win64\avcodec-58.dll")
#cdll.LoadLibrary(r"C:\Users\MCS\AppData\Local\Programs\Python\Python38\Lib\site-packages\pyglet_ffmpeg2\Win64\avformat-58.dll")
#cdll.LoadLibrary(r"C:\Users\MCS\AppData\Local\Programs\Python\Python38\Lib\site-packages\pyglet_ffmpeg2\Win64\swscale-5.dll")
shufflingcount = 10
def main():
    flush()
    settings.sorttype = 'buble'
    while True:
        gf.tick_and_handleevents(60)
        if settings.start:
            startsort()
            settings.start = False
        elif settings.doflush:
            flush()
            settings.doflush = False
        elif settings.doreverse:
            reverse()
            settings.doreverse = False
def flush():
    if settings.lis == []:
        if settings.israndomized:
            for i in range(0, settings.arrsize):
                settings.lis.append(random.randint(settings.minval, settings.maxval))
                gf.showelem(settings.lis, i, gf.normalcol)
        else:
            for i in range(0, settings.arrsize):
                settings.lis.append(i)
                gf.showelem(settings.lis, i, gf.normalcol)
    for i in range(0, settings.arrsize):
        a,b = random.randint(0,settings.arrsize-1), random.randint(0,settings.arrsize-1)
        gf.showelem(settings.lis, a, gf.black)
        gf.showelem(settings.lis, b, gf.black)
        sorter.swap(settings.lis, a, b)
        gf.showelem(settings.lis, a, gf.normalcol)
        gf.showelem(settings.lis, b, gf.normalcol)
    settings.readystate = True
def reverse():
    if settings.lis == []:
        flush()
    nlis = settings.lis.copy()
    sleep = 500 if settings.arrsize < 500 else 0
    for i in range(settings.arrsize-1, -1, -1):
        gf.showelem(settings.lis, i, gf.black)
        settings.lis[i] = nlis[settings.arrsize-1-i]
        gf.showelem(settings.lis, i, gf.normalcol)
        gf.tick_and_handleevents(sleep)
    settings.doreverse = False
def startsort():
    gf.reinitT()
    if settings.sorttype == 'quick':
        sorter.quicksort(settings.lis)
    elif settings.sorttype == 'buble':
        sorter.bublesort(settings.lis)
    elif settings.sorttype == 'insertion':
        sorter.insertion_sort(settings.lis)
    elif settings.sorttype == 'merge':
        sorter.mergesort(settings.lis)
    elif settings.sorttype == 'heaptree':
        sorter.treesort(settings.lis)
    elif settings.sorttype == 'radiax':
        sorter.radiaxsort(settings.lis)
    gf.reinitT()

gf.mainreset = flush
gf.init()
main()





