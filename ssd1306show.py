#! /usr/bin/python
# -*- coding:utf-8 -*-

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class ssd1306():
    ''' ssd1306'''

    def __init__(self,padding=-2):
        RST = None     # pin isnt used

        # init disp
        self.disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
        self.disp.begin()  #init lib

        # clear display
        self.disp.clear()
        self.disp.display()

        # creat image with mode '1' for 1-bit color and draw object
        self.image=Image.new('1',(self.disp.width,self.disp.height))
        self.draw = ImageDraw.Draw(self.image)

        # top bottom
        self.top,self.bottom=padding,self.disp.height-padding

        # load font
        self.font=ImageFont.load_default()

    
    def clear_image(self):
        ''' fill black box to clear'''
        self.draw.rectangle((0,0,self.disp.width,self.disp.height), outline=0, fill=0)

    def show_info(self,IP,cpu,mem,disk):
        ''' draw info '''
        self.draw.text((0,self.top),"IP:"+str(IP),font=self.font,fill=255)
        self.draw.text((0,self.top+8),"CPU load:"+str(cpu),font=self.font,fill=255)
        self.draw.text((0,self.top+16),"Mem:"+str(mem),font=self.font,fill=255)
        self.draw.text((0,self.top+25),"Disk:"+str(disk),font=self.font,fill=255)

        self.disp.image(self.image)
        self.disp.display()

if __name__ == "__main__":
    test=ssd1306()
    test.show_info("x","x","x","x")
