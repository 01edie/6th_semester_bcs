import time
import matplotlib.pyplot as plt
r=100
x=0
y=r
m=50
n=50
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
    ax.append(x+m)
    ay.append(y+n)
    
    bx.append(y+m)
    by.append(x+n)
    
    cx.append(-y+m)
    cy.append(x+n)
    
    dx.append(-x+m)
    dy.append(y+n)
    
    ex.append(-x+m)
    ey.append(-y+n)
    
    fx.append(-y+m)
    fy.append(-x+n)
    
    gx.append(y+m)
    gy.append(-x+n)
    
    hx.append(x+m)
    hy.append(-y+n)
    
plt.plot(ax,ay)
plt.plot(bx,by)
plt.plot(cx,cy)
plt.plot(dx,dy)
plt.plot(ex,ey)
plt.plot(fx,fy)
plt.plot(gx,gy)
plt.plot(hx,hy)

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
    
    