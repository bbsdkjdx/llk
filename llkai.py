import config

def can_through(zs,row,col):
    if (row,col) in zs:
        return True
    if not config.current_info.border:
        cfg=config.current_info
        if row<0 or row>cfg.r-1 or col<0 or col>cfg.c-1:
            return True
    return False



def Linkable(zs,r1,c1,r2,c2):
    ret=_straight_link(zs,r1,c1,r2,c2)
    if ret!="":
        return ret
    ret=_one_corner(zs,r1,c1,r2,c2)
    if ret!="":
        return ret
    ret=_right_search(zs,r1,c1,r2,c2)
    if ret!="":
        return ret
    ret=_left_search(zs,r1,c1,r2,c2)
    if ret!="":
        return ret
    ret=_up_search(zs,r1,c1,r2,c2)
    if ret!="":
        return ret
    ret=_down_search(zs,r1,c1,r2,c2)
    if ret!="":
        return ret
    
    return ""


def _straight_link(zs,r1,c1,r2,c2):
    if r1==r2:
        ma,mi=c1,c2
        if ma<mi:
            ma,mi=mi,ma
        for i in range(mi+1,ma):
            if not can_through(zs,r1,i):
                return ""
        return "straight link"
    if c1==c2:
        ma,mi=r1,r2
        if ma<mi:
            ma,mi=mi,ma
        for i in range(mi+1,ma):
            if not can_through(zs,i,c1):
                return ""
        return "straight link"
    return ""
def _one_corner(zs,r1,c1,r2,c2):
    if _straight_link(zs,r1,c1,r1,c2)!="" and _straight_link(zs,r1,c2,r2,c2)!="" and can_through(zs,r1,c2):
        return "(%d,%d) " % (r1,c2)
    if _straight_link(zs,r1,c1,r2,c1)!="" and _straight_link(zs,r2,c1,r2,c2)!="" and can_through(zs,r2,c1):
        return "(%d,%d) " % (r2,c1)
    return ""

def _right_search(zs,r1,c1,r2,c2):
    ct=c1
    while True:
        ct+=1
        if not can_through(zs,r1,ct):
            return ""
        if ct>config.current_info.c:
            return ""
        if _straight_link(zs,r1,ct,r2,c2)!="":
            return "(%d,%d) " % (r1,ct)
        s1=_one_corner(zs,r1,ct,r2,c2)
        if s1!="":
            s2="(%d,%d) " % (r1,ct)
            return s1+s2
def _left_search(zs,r1,c1,r2,c2):
    ct=c1
    while True:
        ct-=1
        if not can_through(zs,r1,ct):
            return ""
        if ct<-1:
            return ""
        if _straight_link(zs,r1,ct,r2,c2)!="":
            return "(%d,%d) " % (r1,ct)
        s1=_one_corner(zs,r1,ct,r2,c2)
        if s1!="":
            s2="(%d,%d) " % (r1,ct)
            return s1+s2
def _down_search(zs,r1,c1,r2,c2):
    rt=r1
    while True:
        rt+=1
        if not can_through(zs,rt,c1):
            return ""
        if rt>config.current_info.r:
            return ""
        if _straight_link(zs,rt,c1,r2,c2)!="":
            return "(%d,%d) " % (rt,c1)
        s1=_one_corner(zs,rt,c1,r2,c2)
        if s1!="":
            s2="(%d,%d) " % (rt,c1)
            return s1+s2
def _up_search(zs,r1,c1,r2,c2):
    rt=r1
    while True:
        rt-=1
        if not can_through(zs,rt,c1):
            return ""
        if rt<-1:
            return ""
        if _straight_link(zs,rt,c1,r2,c2)!="":
            return "(%d,%d) " % (rt,c1)
        s1=_one_corner(zs,rt,c1,r2,c2)
        if s1!="":
            s2="(%d,%d) " % (rt,c1)
            return s1+s2
