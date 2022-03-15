
# Importing Image from PIL package
from PIL import Image

# creating a image object
im = Image.open(r"aa.jpg")

# coordinate = x, y = 92, 296
# coordinate = x, y = 120, 120

# using getpixel method

def func_fill(a,b,color_new,color_boundary):
    coord=a,b
    
    c=im.getpixel(coord)
    print(c)
    if(c==color_boundary):
        return 1
    elif(c==color_new):
        return 1
    else:
        im.putpixel( (a, b), color_new )
        func_fill(a+1,b,color_new,color_boundary)
        func_fill(a-1,b,color_new,color_boundary)
        func_fill(a,b+1,color_new,color_boundary)
        func_fill(a,b-1,color_new,color_boundary)
func_fill(120,120,(125, 165, 156, 255),(0,0,0))

# (c!=color_new) and (c!=color_boundary)