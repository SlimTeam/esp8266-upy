"""
 Test the modled FrameBuffer implementation with a single MOD-LED8x8RGB Olimex board.

 MOD-LED8x8RGB is 8x8 RGB LED Matrix (7 colors) that can be daisy chained.

MOD-LED8x8RGB board : http://shop.mchobby.be
MOD-LED8x8RGB board : https://www.olimex.com/Products/Modules/LED/MOD-LED8x8RGB/open-source-hardware
Arduino code sample : https://github.com/OLIMEX/UEXT-MODULES/tree/master/MOD-LED8x8RGB/ARDUINO%20EXAMPLE

The MIT License (MIT)
Copyright (c) 2018 Dominique Meurisse, support@mchobby.be, shop.mchobby.be
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from machine import Pin, SPI
from modled import *

# Initialize the SPI Bus (on ESP8266-EVB)
# Software SPI
#    spi = SPI(-1, baudrate=4000000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(13), miso=Pin(12))
# Hardware SPI on Pyboard
spi = SPI(2) # MOSI=Y8, MISO=Y7, SCK=Y6, SS=Y5
spi.init( baudrate=2000000, phase=0, polarity=0 ) # low @ 2 MHz
# We must manage the SS signal ourself
ss = Pin( Pin.board.Y5, Pin.OUT )

modled = ModLedRGB( spi, ss ) # Just one LED brick LED-8x8RGB

modled.rect(0,0,8,8,RED) #x,y, width, Height
modled.rect(1,1,6,6,GREEN)
modled.rect(2,2,4,4,BLUE)
modled.rect(3,3,2,2,MAGENTA)
modled.show() # Update the matrix
