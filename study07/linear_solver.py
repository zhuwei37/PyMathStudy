from vectors import *
import numpy as np
def standard_from(u1,u2):
    x1,y1=u1
    x2,y2=u2
    a=y2-y1
    b=-(x2-x1)
    c=x1*y2-x2*y1
    return a,b,c

def intersection(u1,u2,v1,v2):
    a1,b1,c1=standard_from(u1,u2)
    a2,b2,c2=standard_from(v1,v2)
    m=np.array(((a1,b1),(a2,b2)))
    c=np.array((c1,c2))
    return np.linalg.solve(m,c)
def do_segments_intersect(s1,s2):
    u1,u2=s1
    v1,v2=s2
    l1,l2=distance(*s1),distance(*s2)
    try:
        x,y=intersection(u1,u2,v1,v2)
        return (
            distance(u1,(x,y))<=l1 and
            distance(u2,(x,y))<=l1 and
            distance(v1,(x,y)) <=l2 and
            distance(v2,(x,y))<=l2
        )
    except np.linalg._linalg.LinAlgError:
        return False