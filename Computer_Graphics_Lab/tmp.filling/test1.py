
# Importing Image from PIL package
from PIL import Image

# creating a image object
im1 = Image.open(r"aa.jpg")


coord = x, y = 120, 120
c=im1.getpixel(coord)
for z in range(45):
    if(c==(0,0,0)):
            break
    print(c)
    if(c!=(125, 165, 156, 255)) and (c!=(0,0,0)):
        
        im1.putpixel( (x, y), (125, 165, 156, 255))
    x=x+1
    c=im1.getpixel((x,y))
print(c)
im1.show()


# print(im.getpixel(coordinate))
# print(type(im.getpixel(coordinate)))
# (31, 180, 187)