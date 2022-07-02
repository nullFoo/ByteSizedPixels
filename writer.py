from PIL import Image
import math

imgPath = input("image path: ")
writePath = input("write path: ")


im = Image.open(imgPath)   
out = Image.new('RGBA', im.size)
alpha = out.split()[-1]
out.putalpha(alpha)

alphaImg = out.getchannel("A")

width, height = im.size

if(width > 32 or height > 32):
    print("image too large: width and height must both be <32")
    exit()

arr = [int("00000000", 2)] # initialise with an empty byte, because for some reason the reader can't read the first byte idk

# add width and height headers
widthBin = "101" + (str(bin(width))[2:])
heightBin = "110" + (str(bin(height))[2:])

print(widthBin)
print(heightBin)

arr.append(int(widthBin, 2))
arr.append(int(heightBin, 2))

# loop through pixels
x = 0
y = 0

prevcolor = (-1,0,0,0)
compressionbuffer = 0

for i in range(width * height):
    r,g,b = im.getpixel((x,y))
    a = alphaImg.getpixel((x,y))
    
    r = math.floor(r / 64)
    g = math.floor(g / 64)
    b = math.floor(b / 64)
    a = math.ceil(a / 255)
    
    
    if(prevcolor == (r, g, b, a)):
        compressionbuffer += 1
        
        if(compressionbuffer > 30):
            byte = "111" + str(bin(compressionbuffer))[2:].zfill(5)
            arr.append(int(byte, 2))
            
            byte = "0" + str(bin(r))[2:].zfill(2) + str(bin(g))[2:].zfill(2) + str(bin(b))[2:].zfill(2) + str(bin(a))[2:]
            arr.append(int(byte, 2))
            
            compressionbuffer = 0
    else:
        if(compressionbuffer > 0):
            byte = "111" + str(bin(compressionbuffer))[2:].zfill(5)
            arr.append(int(byte, 2))
            compressionbuffer = 0
        
        byte = "0" + str(bin(r))[2:].zfill(2) + str(bin(g))[2:].zfill(2) + str(bin(b))[2:].zfill(2) + str(bin(a))[2:]
        arr.append(int(byte, 2))
        
        
    print(str(prevcolor) + " | " + str((r, g, b, a)))
    prevcolor = (r, g, b, a)
        
    x += 1
    if(x > width-1):
        x = 0
        y += 1

# write bytes to file
newFile = open(writePath, "wb")    
byteArray = bytes(arr)
newFile.write(byteArray)