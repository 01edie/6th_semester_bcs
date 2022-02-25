import matplotlib.pyplot as plt
m=[]
n=[]
def bld(x1, y1,x2,y2):
    x=x1
    y=y1
    dx=x2-x1
    dy=y2-y1
    slope=(dy/dx)
    p=(2*dy)-dx
    length=(x2-x1) if (x2-x1)>(y2-y1) else (y2-y1)
    m.insert(0,x)
    n.insert(0,y)
    print('x0=%s, y0=%s' %(x,y))
    if(slope<1):
        
        for i in range(length):
            if(p<0):
                x=x+1
                y=y
                p=p+2*dy
                m.insert(i+1,x)
                n.insert(i+1,y)
                print('x%s=%s, y%s=%s' %((i+1),x,(i+1),y))
                
            else:
                x=x+1
                y=y+1
                p=p+(2*dy)-(2*dx)
                m.insert(i+1,x)
                n.insert(i+1,y)
                print('x%s=%s, y%s=%s' %((i+1),x,(i+1),y))
    else:
        for i in range(length):
            if(p<0):
                x=x
                y=y+1
                p=p+2*dx
                m.insert(i+1,x)
                n.insert(i+1,y)
                print('x%s=%s, y%s=%s' %((i+1),x,(i+1),y))
                
            else:
                x=x+1
                y=y+1
                p=p+(2*dx)-(2*dy)
                m.insert(i+1,x)
                n.insert(i+1,y)
                print('x%s=%s, y%s=%s' %((i+1),x,(i+1),y))
        
        
        
bld(1,1,20,12)
plt.plot(m,n)
plt.title("bresenham line drawing")
plt.show()
            
        