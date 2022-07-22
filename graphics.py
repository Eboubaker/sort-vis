import pygame as pg
import easygui as inputfield
import time,math, os, sys
import settings
import tools

white = None
black = None
sortedcol = None
indexcol = None
normalcol = None
secondarycol = None
font = None
ticks = None

def init():
    global sortedcol,indexcol,normalcol,secondarycol,black,white,font,ticks
    ticks = 0
    white = (settings.gf.dim*255,settings.gf.dim*255,settings.gf.dim*255)
    black = (0,0,0)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,25)
    pg.init()
    font = pg.font.SysFont('Arial', 10)
    settings.gf.cnv = pg.display.set_mode((settings.gf.width,settings.gf.height), pg.RESIZABLE)
    settings.gf.clock = pg.time.Clock()
    sortedcol = (0,255*settings.gf.dim,0)
    indexcol = (255*settings.gf.dim,0,0)
    normalcol = white
    secondarycol = (120,0,255)
    white = (255*settings.gf.dim,255*settings.gf.dim,255*settings.gf.dim)
    black = (0,0,0)
    reinit()
    settings.gf.cnv = pg.display.set_mode((settings.gf.width,settings.gf.height), pg.RESIZABLE)
    pg.display.update()

def reinit(refresh=False):
    if refresh:
        v = inputfield.integerbox("array size?", "give me input", settings.arrsize, 1, 999999)
        if v is not None:
            settings.arrsize = v
            settings.lis = []
            settings.gf.cnv.fill(black)
            pg.display.update()
    if settings.arrsize < -1:
        reinit()
        return
    #settings.maxval = settings.arrsize
    if settings.viewtype != 3:
        settings.gf.recwidth = int(settings.gf.width / settings.arrsize)
        settings.gf.strokewidth = tools.mapv(settings.arrsize, 200, 500, 0.5, 0.1)
def tick_and_handleevents(fbs=None):
    global ticks
    ticks += 1
    handle_events()
    if fbs == None:
        fbs = settings.framerate
    settings.gf.clock.tick(fbs)
def Tshow():
    sys.stdout.write('\rTime: '+str(ticks))
    sys.stdout.flush()
def reinitT():
    global ticks
    sys.stdout.write('\rTime: '+str(ticks)+'\n')
    sys.stdout.flush()
    ticks = 0
def handle_events():
    #keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit() 
        if event.type == pg.VIDEORESIZE and settings.readystate:
            settings.gf.cnv = pg.display.set_mode((event.w, event.h),pg.RESIZABLE)
            w,h = event.dict['size']
            settings.gf.width = w
            print(w,h)
            reinit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_KP_MINUS:
                if settings.framerate > 10:
                    settings.framerate -= 10
                elif settings.framerate > 1:
                    settings.framerate -= 1
            elif event.key == pg.K_KP_PLUS:
                settings.framerate += 10
            elif event.key == pg.K_KP_MULTIPLY:
                settings.framerate = 8192
            elif event.key == pg.K_KP_DIVIDE:
                settings.framerate = 1
            elif event.key == pg.K_KP_PERIOD:
                settings.framerate = 60
            elif event.key == pg.K_s:
                settings.start = True
            elif event.key == pg.K_r:
                settings.doreverse = True
            elif event.key == pg.K_f:
                settings.doflush = True
            elif event.key == pg.K_1:
                settings.viewtype = 1
                settings.gf.cnv.fill(black)
                pg.display.update()
                settings.doflush = True
            elif event.key == pg.K_2:
                settings.viewtype = 2
                settings.gf.cnv.fill(black)
                settings.doflush = True
                pg.display.update()
            elif event.key == pg.K_3:
                settings.viewtype = 3
                settings.gf.cnv.fill(black)
                settings.doflush = True
                pg.display.update()
            elif event.key == pg.K_4:
                settings.viewtype = 4
                settings.gf.cnv.fill(black)
                settings.doflush = True
                pg.display.update()
            elif event.key == pg.K_ESCAPE:
                exit()
            elif settings.readystate:
                if event.key == pg.K_q:
                    settings.sorttype = 'quick'
                elif event.key == pg.K_b:
                    settings.sorttype = 'buble'
                elif event.key == pg.K_m:
                    settings.sorttype = 'merge'
                elif event.key == pg.K_i:
                    settings.sorttype = 'insertion'
                elif event.key == pg.K_h:
                    settings.sorttype = 'heaptree'
                elif event.key == pg.K_a:
                    settings.sorttype = 'radiax'
                elif event.key == pg.K_RETURN:
                    reinit(True)
                elif event.key == pg.K_KP_ENTER:
                    tools.changeMaxVal()

def showelem(arr, index, col):
    """ show element """
    if len(arr) <= index:
        print('shoelem said no')
        return
    Tshow()
    if settings.viewtype == 1:
        as_rectline(arr, index, col)
    elif settings.viewtype == 2:
        as_spectrum(arr, index, col)
    elif settings.viewtype == 3:
        as_line(arr, index, col)
    elif settings.viewtype == 4:
        as_point(arr, index, col)

def as_point(arr, index, col):
    y = int(settings.gf.height - settings.gf.height * arr[index] / settings.maxval)
    pg.draw.rect(settings.gf.cnv,black,(index,0,1,settings.gf.height))# clear the whole line, the old point might be in any place on that line
    pg.display.update(pg.Rect(index,0,1,settings.gf.height))
    pg.draw.rect(settings.gf.cnv,col,(index,y,1,1))#put the new position of the point
    pg.display.update(pg.Rect(index,y,1,1))
    
def as_line(arr, index, col):
    len = settings.gf.height - 1.0*settings.gf.height*arr[index] / settings.maxval
    pg.draw.line(settings.gf.cnv,black,(index,0),(index,settings.gf.height))
    pg.draw.line(settings.gf.cnv,col,(index,len),(index,settings.gf.height))
    pg.display.update(pg.Rect(index, 0, 1, settings.gf.height))

def as_spectrum(arr, index, col):
    perc = float(arr[index]) / float(settings.maxval)
    if col == normalcol or col == sortedcol:
        col = tools.torgb(perc)
    elif col == indexcol:
        col = black
    elif col == secondarycol:
        col = tools.torgb(perc)
    rectbig = pg.Rect(int(index*settings.gf.recwidth), 0, settings.gf.recwidth, settings.gf.height)
    draw_rect(col, None, rectbig, 0)
    pg.display.update(rectbig)

def as_rectline(arr, index, col):
    len = settings.gf.height - 1.0*settings.gf.height*arr[index] / settings.maxval
    rect = pg.Rect(int(index*settings.gf.recwidth), len, settings.gf.recwidth, settings.gf.height-len)
    rectbig = pg.Rect(int(index*settings.gf.recwidth), 0, settings.gf.recwidth, settings.gf.height)
    draw_rect(black, None, rectbig)
    draw_rect(col, None, rect)
    pg.display.update(rectbig)

def draw_rect(fill_color, outline_color, rect, border=None):
    if border == None:
        border = settings.gf.strokewidth
    if outline_color == None:
        outline_color = black
    settings.gf.cnv.fill(outline_color, rect)
    settings.gf.cnv.fill(fill_color, rect.inflate(-border*2, -border*2))


def maptocolor(perc):
    """ map array value to color value """
    r = 255 * perc / .333 # these .3 and .6 so that white and black colors dont show up
    g = 255 * perc / .666
    b = 255 * perc
    return (r,g,b)
