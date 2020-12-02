# better to do this using a matrix library

def project(a, c, e):
    d = [
      a[0] - c[0],
      a[1] - c[1],
      a[2] - c[2]
    ]
    b = [
      (e[2] / d[2] * d[0]) + e[0],
      (e[2] / d[2] * d[1]) + e[1]
    ]
    return [b[0], b[1]]


def rotatex(a, t):
    a = [
      a[0],
      a[1] * cos(t) - a[2] * sin(t),
      a[1] * sin(t) + a[2] * cos(t)
    ]
    return a


def rotatey(a, t):
    a = [
      a[2] * sin(t) + a[0] * cos(t),
      a[1],
      a[2] * cos(t) - a[0] * sin(t)
    ]
    return a


def rotatez(a, t):
    a = [
      a[0] * cos(t) - a[1] * sin(t),
      a[0] * sin(t) + a[1] * cos(t),
      a[2]
    ]
    return a
