
# Importing Image from PIL package
from PIL import Image

# creating a image object
im = Image.open(r"a.jpg")

# coordinate = x, y = 92, 296
# coordinate = x, y = 48, 148
coordinate = x, y = 322, 145
for i in range(109,149):
    im.putpixel((i,100),(0,0,0,255))
    im.putpixel((i,140),(0,0,0,255))
for i in range(100,141):
    im.putpixel((109,i),(0,0,0,255))
    im.putpixel((149,i),(0,0,0,255))
im.save('aa.jpg')
# coord=a,b=120,120
# c=im.getpixel(coord)

# for i in range(45):
#     a=120
#     b=120
#     print(im.getpixel((a,b)))
#     a=a+1
#     im.putpixel()


# for z in range(35):
    
#     print(c)
#     if(c!=(125, 165, 156, 255)) and (c!=(0,0,0)):
#         im.putpixel( (a, b), (125, 165, 156, 255))
#     a=a+1
#     c=im.getpixel(coord)



# def func_fill(a,b,color_new,color_boundary):
#     coord=a,b
    
#     c=im.getpixel(coord)
#     if(c!=color_new) and (c!=color_boundary):
#         im.putpixel( (a, b), color_new )
#         func_fill(a+1,b,color_new,color_boundary)
#         func_fill(a-1,b,color_new,color_boundary)
#         func_fill(a,b+1,color_new,color_boundary)
#         func_fill(a,b-1,color_new,color_boundary)
# func_fill(120,120,(125, 165, 156, 255),(0,0,0,255))

# im.show()

# print(im.getpixel(coordinate))
# print(type(im.getpixel(coordinate)))
# (31, 180, 187)