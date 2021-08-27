#return a modified rectangle
import copy
class point:
    """ created a class point"""
    
class rectangle:
    """created a class rectangle"""
    
def move_rectangle(rect,dx,dy):
    new=copy.deepcopy(rect)
    new.corner.x+=dx
    new.corner.y+=dy
    return new
    
box=rectangle()
box.width=100
box.height=200
box.corner=point()
box.corner.x=0
box.corner.y=0

box2=move_rectangle(box,50,75)
print(box.corner.x,box2.corner.x)
print(box.corner.y,box2.corner.y)
print(box.width,box2.width)
print(box.height,box2.height)
