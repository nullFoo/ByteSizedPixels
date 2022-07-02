from PIL import Image, ImageColor
import math

path = input("file path")

width = 0
height = 0

curX = 0
curY = 0

currentColour = (0,0,0,255)

img = 0

def movePixel():
    if(img == 0):
        print("File headers missing")
        exit()
        
    global curX
    global curY

    img.putpixel((curX, curY), colour)
    
    curX += 1
    if(curX > width-1):
        curX = 0
        curY += 1

with open(path, "rb") as f:
    byte = f.read(1)
    while byte:
        byte = f.read(1)
        if(byte != ""):
            try:
                bits = ord(byte)
            except:
                break
            bits = bin(bits)[2:].rjust(8, '0')
            
            #for bit in bits:
            #    print(bit, end="")
                
            if(bits[0] == "1"): # this byte is an instruction
                instruction = int(bits[1] + bits[2], 2)
                
                if(instruction == 1): # set width
                    param = ''.join(bits[3:])
                    width = int(param, 2)
                elif(instruction == 2): # set height
                    param = ''.join(bits[3:])
                    height = int(param, 2)
                elif(instruction == 3): # previous colour continues for [param] pixels
                    print(str(bits))
                    param = ''.join(bits[3:])
                    print(str(currentColour) + " * " + param)
                    for x in range(int(param, 2)):
                        movePixel()
            else: # this byte is a colour
                r = int(''.join(bits[1:3]), 2)
                g = int(''.join(bits[3:5]), 2)
                b = int(''.join(bits[5:7]), 2)
                a = int(bits[7])
                
                if(img == 0):
                    print("File headers missing")
                    exit()
                
                r = math.floor(r * 63.75)
                g = math.floor(g * 63.75)
                b = math.floor(b * 63.75)
                
                colour = (r, g, b, a * 255)
                currentColour = colour
                
                movePixel()
                
            if(img == 0 and width != 0 and height != 0):
                img = Image.new(mode="RGB", size=(width, height))
            
            if(img != 0 and curY > height-1):
                break
    img.show()
    print("done")