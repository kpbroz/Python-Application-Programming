#program to print centroid of a rectangle

class point:
    """represents points"""
    
class rectangle:
    """represents rectangle"""
    
    
def  centre(b):
    p=point()
    p.x=(b.width+b.corner.x)/2
    p.y=(b.height+b.corner.y)/2
    return p

def print_point(p):
    print('(%g,%g)'%(p.x,p.y))
    
box=rectangle()
box.width=100
box.height=200
box.corner=point()
box.corner.x=0
box.corner.y=0

cnter=centre(box)
print_point(cnter)
