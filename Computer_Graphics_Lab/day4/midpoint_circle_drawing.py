import matplotlib.pyplot as plt
r=100
x=0
y=r
m=50
n=50
a=[]
b=[]
d = 1-r
while(x<y):
    i=0
    if (d<0):
        d = d+(2*x)+3
        x=x+1
    else:
        d = d+(2*(x-y))+5
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
    
    
    
plt.plot(a,b,'c.')
# here just points has been plotted , not joined



# plt.plot(x+m,y+n)
# plt.plot(y+m,x+n)
# plt.plot(-y+m,x+n)
# plt.plot(-x+m,y+n)
# plt.plot(-x+m,-y+n)
# plt.plot(-y+m,-x+n)
# plt.plot(y+m,-x+n)
# plt.plot(x+m,-y+n)