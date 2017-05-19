class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def points(self):
        return [self.a, self.b, self.c]

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def triangle_area(triangle):
    pts = [triangle.a, triangle.b, triangle.c, triangle.a]
    area = 0
    for i in range(3):
        area += pts[i].x * pts[i+1].y - pts[i+1].x * pts[i].y
    area = area / 2.0
    return abs(area)
