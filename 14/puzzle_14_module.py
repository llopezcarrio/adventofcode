def move_robot(pw,pt,vr,vd,w,h,s):

    for i in range(s):

        pw = pw + vr

        if pw < 0:
            pw = w + pw

        if pw >= w:
            pw = pw - w

        pt = pt + vd

        if pt < 0:
            pt = h + pt

        if pt>= h:
            pt = pt - h



    return pw, pt

def get_quadrant(pw, pt, w, h):

    if pw == w//2  or pt == h//2:
        return 0
    if pw < w/2 and pt < h/2:
        return 1
    elif pw >= w/2 and pt < h/2:
        return 2
    elif pw < w/2 and pt >= h/2:
        return 3
    elif pw >= w/2 and pt >= h/2:
        return 4
