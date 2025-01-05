def move_robots(robots, t, w, h):
    return [((pw + t * vw) % w, (ph + t * vh) % h) for pw, ph, vw, vh in robots]