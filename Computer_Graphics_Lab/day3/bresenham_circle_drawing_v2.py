import time
import matplotlib.pyplot as plt
r=100
x=0
y=r
xc=50
yc=50
ax=[]
bx=[]
cx=[]
dx=[]
ex=[]
fx=[]
gx=[]
hx=[]

ay=[]
by=[]
cy=[]
dy=[]
ey=[]
fy=[]
gy=[]
hy=[]

d = 3-2*(r)
while(x<y):
    
    if (d<0):
        
        d = d+(4*x)+6
        x=x+1
        
    else:
              
        d = d+(4*(x-y))+10
        x=x+1
        y=y-1
    ax.append(x+xc)
    ay.append(y+yc)
    
    bx.append(y+xc)
    by.append(x+yc)
    
    cx.append(-y+xc)
    cy.append(x+yc)
    
    dx.append(-x+xc)
    dy.append(y+yc)
    
    ex.append(-x+xc)
    ey.append(-y+yc)
    
    fx.append(-y+xc)
    fy.append(-x+yc)
    
    gx.append(y+xc)
    gy.append(-x+yc)
    
    hx.append(x+xc)
    hy.append(-y+yc)
    
plt.plot(ax,ay,linewidth=3)
plt.plot(bx,by,linewidth=3)
plt.plot(cx,cy,linewidth=3)
plt.plot(dx,dy,linewidth=3)
plt.plot(ex,ey,linewidth=3)
plt.plot(fx,fy,linewidth=3)
plt.plot(gx,gy,linewidth=3)
plt.plot(hx,hy,linewidth=3)
plt.title('Bresenham Circle Drawing')
# plt.plot(hx,hy,marker = 'o', markerfacecolor = 'r')
# here for 8 points, 8parts' points are stored in 8 arrays sorted one after another
# and then 8 parts points are joined separately
    
    
    

# plt.plot(x+m,y+n)
# plt.plot(y+m,x+n)
# plt.plot(-y+m,x+n)
# plt.plot(-x+m,y+n)
# plt.plot(-x+m,-y+n)
# plt.plot(-y+m,-x+n)
# plt.plot(y+m,-x+n)
# plt.plot(x+m,-y+n)
    
    
