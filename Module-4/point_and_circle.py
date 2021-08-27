#finding whether a point is present in circle or not

import copy
from math import sqrt

class circle:
    """circle with centre and radius"""
    
class point:
    """created class point"""
    
def point_in_circle(c,p):
    d=abs(sqrt((p.x-c.center.x)**2+(p.y-c.center.y)**2))
    
    if d>c.radius:
        return False
    return True
    
    
c=circle()
c.radius=75
c.center=point()
c.center.x=150
c.center.y=100

p=point()
x,y=input("Enter the coordinates of point to be searched: ").split()
p.x=float(x)
p.y=float(y)
result=point_in_circle(c,p)

print(result)
