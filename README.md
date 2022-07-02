# ByteSizedPixels
an image format

## Notes
- There are two bits per channel, meaning only 64 possible colours (images with more colours will be converted automatically, no need to make sure you're using 2-bit colour)
- Images must be under 32x32

This is an image format I made. It's not efficient or good but it was fun to make. I will add some compression to it later.

## For each byte in a file:
First bit: 0 means it is a colour, 1 means it is an instruction

Colours:
- Two bits for each colour channel (RGB). The last bit is alpha, which can be either 0(transparent) or 1(opaque)
    
Instructions:
- The first two bits tell you what instruction it is. This means a maximum of 4 instructions, though there only are 3 at the moment. The three instructions that currently exist are:
  - 01: set width of image
  - 10: set height of image
  - 11: continue previous colour for [param] pixels (this is used in compression)
- The other bits are the parameters. Unfortunately, this means the maximum for any parameter is 32, hence the image size limit.
- I think I will add a fourth instruction later which will allow you to add bits to the parameters of the previous instruction, increasing the limit.
        
## Usage
https://user-images.githubusercontent.com/38643612/177018187-91aa0f1f-1d8f-4547-b97c-f4c6d5cac6ab.mp4

