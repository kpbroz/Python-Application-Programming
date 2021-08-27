#program to find the distance between two points

class point:
    """class created named point
    represents point in 2D coordinate space"""
    
p1=point()
p2=point()

p1.x=1
p1.y=1
p2.x=2
p2.y=2

from math import sqrt
def distance_bet_points(p1,p2):
    return sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)

print(distance_bet_points(p1,p2))
