import ctypes
import config
dll=ctypes.CDLL(r'llkdll.dll')

def get_clr(x,y):
    "get pixel by specified (x,y) coordinate"
    return  dll.get_clr(x,y)

def find_wnd(title):
    return dll.find_wnd(title)

def get_wnd_offset(hwn):
    ofs=dll.get_wnd_offset(hwn)
    return ofs>>16,ofs&((1<<16)-1)

def get_id(r,c):
    "get the id of the specified grid."
    cfg=config.current_info
    ret=0
    for _r in range(6,cfg.h-6):
        accl=0
        for _c in range(6,cfg.w-6):
            x=cfg.x0+c*cfg.w+_c
            y=cfg.y0+r*cfg.h+_r
            accl+=get_clr(x,y)
        ret^=accl
    return ret

def sample(wnd):
    if wnd==0:
        return dict(),set()
    dll.snap(wnd)
    same=dict()
    zs=set()
    cfg=config.current_info
    for r in range(cfg.r):
        for c in range(cfg.c):
            k=get_id(r,c)
            if k==cfg.id_bk:
                zs.add((r,c))
                continue
            if k in same:
                same[k].append((r,c))
            else:
                same[k]=[(r,c)]
    return list(same.values()),zs

def test_sample():
    same=dict()
    zs=set()
    cfg=config.current_info
    for r in range(cfg.r):
        for c in range(cfg.c):
            k=get_id(r,c)
            if k==cfg.id_bk:
                zs.add((r,c))
                continue
            if k in same:
                same[k].append((r,c))
            else:
                same[k]=[(r,c)]
    return list(same.values()),zs

def click(x,y):
    ctypes.windll.user32.SetCursorPos(x,y)
    ctypes.windll.user32.mouse_event(2,0,0,0,0)
    ctypes.windll.user32.mouse_event(4,0,0,0,0)



