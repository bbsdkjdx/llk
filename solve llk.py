from llkdll import sample,click,get_wnd_offset,find_wnd
from llkai import Linkable
from arbin import hotkey
from ctypes import windll
import config

li_linkable=list()
wnd=lambda :find_wnd(config.current_info.wnd_title)
last_tick=0

def get_lkb_from_li(li_same,zs):
    L=len(li_same)
    for i in range(L-1):
        for j in range(i+1,L):
            r1,c1=li_same[i]
            r2,c2=li_same[j]
            s=Linkable(zs,r1,c1,r2,c2)
            if s!="":
                return ((r1,c1),(r2,c2),s)
    return None

def search_one_loop(same,zs):
    ret=[]
    for _li in same:
        lkp=get_lkb_from_li(_li,zs)
        if lkp==None:
            continue
        _li.remove(lkp[0])
        _li.remove(lkp[1])
        zs.add(lkp[0])
        zs.add(lkp[1])
        ret.append(((lkp[0][0],lkp[0][1],lkp[1][0],lkp[1][1]),lkp[2]))
    return ret

def get_linkable_set(wnd):
    ret=list()
    same,zs=sample(wnd)
    _lkbs=search_one_loop(same,zs)
    while len(_lkbs)!=0:
        ret+=_lkbs
        _lkbs=search_one_loop(same,zs)
    return ret

def click_grid(wnd,r,c):
    cfg=config.current_info
    wx,wy=get_wnd_offset(wnd)
    x=wx+c*cfg.w+cfg.x0+cfg.w//2
    y=wy+r*cfg.h+cfg.y0+cfg.h//2
   # print("click",r,c,"   ",x,y)
    click(x,y)


def work_once():
    cfg=config.current_info
    _wnd=wnd()
    global li_linkable,last_tick
    if len(li_linkable)==0 or _wnd==0:
        tic=windll.kernel32.GetTickCount()
        if tic-last_tick<3000:
            return
        last_tick=tic
        li_linkable=get_linkable_set(_wnd)
        print("%d pairs found!"% len(li_linkable))
    
    if len(li_linkable)!=0:
        (r1,c1,r2,c2),s=li_linkable.pop(0)
        click_grid(_wnd,r1,c1)
        click_grid(_wnd,r2,c2)
       # print(r1,c1,r2,c2,"            ",s)

config.current_info=config.llk_48
hotkey.reg(0,hotkey.VK_F10,work_once)

#hk.reg(hk.MOD_CONTROL,50,reset)
