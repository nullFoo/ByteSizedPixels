path = input("file path")
from PIL import Image, ImageColor

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
    if(curX > width):
        curX = 0
        curY += 1
        if(curY > height):
            exit()

with open(path, "rb") as f:
    byte = f.read(1)
    while byte:
        byte = f.read(1)
        if(byte != ""):
            print(" ")
            try:
                bits = ord(byte)
            except:
                break
            bits = bin(bits)[2:].rjust(8, '0')
            
            for bit in bits:
                print(bit, end="")
                
            if(bits[0] == "1"): # this byte is an instruction
                instruction = int(bits[1] + bits[2], 2)
                
                if(instruction == 1): # set width
                    param = ''.join(bits[2:])
                    width = int(param, 2)
                elif(instruction == 2): # set height
                    param = ''.join(bits[2:])
                    height = int(param, 2)
                elif(instruction == 3): # previous colour continues for [param] pixels
                    param = ''.join(bits[2:])
                    for x in range(param)
                        movePixel()
            else: # this byte is a colour
                r = int(''.join(bits[:2]), 2)
                g = int(''.join(bits[2:4]), 2)
                b = int(''.join(bits[4:6]), 2)
                a = int(bits[7])
                
                if(img == 0):
                    print("File headers missing")
                    exit()
                
                colour = (r * 64, g * 64, b * 64, a * 255)
                currentColour = colour
                print(colour)
                
                movePixel()
                
            if(img == 0 and width != 0 and height != 0):
                img = Image.new(mode="RGB", size=(width, height))
                print((width, height))
    img.show()