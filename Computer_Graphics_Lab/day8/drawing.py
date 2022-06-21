import matplotlib.pyplot as plt
plt.plot([0,200,200,0,0],[0,0,200,200,0])
plt.plot([0,100,200,0],[200,350,200,200])
plt.plot([80,80,120,120],[0,80,80,0])

#circle 1
r=25
x=0
y=r
m=40
n=150
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
    a.append(x+m)
    b.append(y+n)
    a.append(y+m)
    b.append(x+n)
    a.append(-y+m)
    b.append(x+n)
    a.append(-x+m)
    b.append(y+n)
    a.append(-x+m)
    b.append(-y+n)
    a.append(-y+m)
    b.append(-x+n)
    a.append(y+m)
    b.append(-x+n)
    a.append(x+m)
    b.append(-y+n)
    
    
    
plt.plot(a,b,'b')

#circle 2
r=25
x=0
y=r
m=160
n=150
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
    a.append(x+m)
    b.append(y+n)
    a.append(y+m)
    b.append(x+n)
    a.append(-y+m)
    b.append(x+n)
    a.append(-x+m)
    b.append(y+n)
    a.append(-x+m)
    b.append(-y+n)
    a.append(-y+m)
    b.append(-x+n)
    a.append(y+m)
    b.append(-x+n)
    a.append(x+m)
    b.append(-y+n)
    
    
    
plt.plot(a,b,'b')


 