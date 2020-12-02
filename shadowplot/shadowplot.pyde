# https://en.wikipedia.org/wiki/3D_projection#Perspective_projection

from rotations import *

# pyramid coordinates
a1 = [0.0, 0.0, 50.0]  # the 3D position of a point A that is to be projected
a2 = [0.0, 100.0, 50.0]
a3 = [100.0, 100.0, 50.0]
a4 = [100.0, 0.0, 50.0]
a5 = [50.0, 50.0, 125.0]

c = [0.0, 0.0, 200.0]  # the 3D position of a point C representing the camera
e = [0.0, 0.0, 140.0]  # display surface position relative to camera pinhole C
t = 0.02               # z rotation


def setup():
    size(600, 600)
    noFill()
    strokeWeight(3)


def draw():
    global a1, a2, a3, a4, a5
    background('#FFFFFF')

    # pyrmaid using isometric projection
    stroke('#FF0000')
    pushMatrix()
    translate(100, 100)
    # pyramid cap
    line(a5[0], a5[1], a1[0], a1[1])
    line(a5[0], a5[1], a2[0], a2[1])
    line(a5[0], a5[1], a3[0], a3[1])
    line(a5[0], a5[1], a4[0], a4[1])
    # pyramid base
    line(a1[0], a1[1], a2[0], a2[1])
    line(a2[0], a2[1], a3[0], a3[1])
    line(a3[0], a3[1], a4[0], a4[1])
    line(a4[0], a4[1], a1[0], a1[1])
    popMatrix()

    # pyramid using perspective projection
    stroke('#0000FF')
    pushMatrix()
    translate(width-100, height-100)
    p1, p2, p3, p4, p5 = [
      project(a1, c, e),
      project(a2, c, e),
      project(a3, c, e),
      project(a4, c, e),
      project(a5, c, e)
    ]
    # cap
    line(p5[0], p5[1], p1[0], p1[1])
    line(p5[0], p5[1], p2[0], p2[1])
    line(p5[0], p5[1], p3[0], p3[1])
    line(p5[0], p5[1], p4[0], p4[1])
    # base
    line(p1[0], p1[1], p2[0], p2[1])
    line(p2[0], p2[1], p3[0], p3[1])
    line(p3[0], p3[1], p4[0], p4[1])
    line(p4[0], p4[1], p1[0], p1[1])
    popMatrix()

    # x-axis rotation
    a1, a2, a3, a4, a5 = [
      rotatex(a1, t),
      rotatex(a2, t),
      rotatex(a3, t),
      rotatex(a4, t),
      rotatex(a5, t)
    ]
    # y-axis rotation
    a1, a2, a3, a4, a5 = [
      rotatey(a1, t),
      rotatey(a2, t),
      rotatey(a3, t),
      rotatey(a4, t),
      rotatey(a5, t)
    ]
