import matplotlib.pyplot as plt
r=100
x=0
y=r
m=50
n=50
a=[]
b=[]
d = 3-2*(r)
while(x<y):
    i=0
    if (d<0):
        
        d = d+(4*x)+6
        x=x+1
        
    else:
              
        d = d+(4*(x-y))+10
        x=x+1
        y=y-1
    a.insert(i,x+m)
    b.insert(i,y+n)
    i=i+1
    a.insert(i,y+m)
    b.insert(i,x+n)
    i=i+1
    a.insert(i,-y+m)
    b.insert(i,x+n)
    i=i+1
    a.insert(i,-x+m)
    b.insert(i,y+n)
    i=i+1
    a.insert(i,-x+m)
    b.insert(i,-y+n)
    i=i+1
    a.insert(i,-y+m)
    b.insert(i,-x+n)
    i=i+1
    a.insert(i,y+m)
    b.insert(i,-x+n)
    i=i+1
    a.insert(i,x+m)
    b.insert(i,-y+n)
    i=i+1
    print(x)
    print(y)
    
    
plt.plot(a,b)
# plt.plot(x+m,y+n)
# plt.plot(y+m,x+n)
# plt.plot(-y+m,x+n)
# plt.plot(-x+m,y+n)
# plt.plot(-x+m,-y+n)
# plt.plot(-y+m,-x+n)
# plt.plot(y+m,-x+n)
# plt.plot(x+m,-y+n)
    
    
