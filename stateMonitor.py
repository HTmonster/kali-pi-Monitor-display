#! /usr/bin/python
# -*- coding:utf-8 -*-
import psutil
import subprocess
import time

import ssd1306show,rgbStateshow

class stateMonitor():

    def __init__(self,interval=20):
        # other unit
        self.ssd1306=ssd1306show.ssd1306()
        self.rgbstate=rgbStateshow.rgbState()
        self.interval=interval if interval>1 else 2


    def begin_monitor(self):

        while True:
            cmd = "hostname -I | cut -d\' \' -f1"
            IP = subprocess.check_output(cmd, shell = True )

            cpu=psutil.cpu_percent(interval=1)

            mem=psutil.virtual_memory()
            mem_str="{}/{}M {}%".format(
                round(mem.used/(1024*1024),2),
                round(mem.total/(1024*1024),2),
                mem.percent)

            disk=psutil.disk_usage("/")

            disk_str="{}/{}G {}%".format(
                round(disk.used/(1024*1024*1024),2),
                round(disk.total/(1024*1024*1024),2),
                disk.percent)

            self.ssd1306.clear_image() # clear
            self.ssd1306.show_info(IP,cpu,mem_str,disk_str)

            if cpu >90:
                    self.rgbstate.color_display('red')
            elif cpu >50:
                self.rgbstate.color_display('yellow')
            elif cpu >10:
                self.rgbstate.color_display('blue')
            else:
                self.rgbstate.color_display('green')

            time.sleep(self.interval)
        

if __name__ == "__main__":
    stateMonitor=stateMonitor()
    stateMonitor.begin_monitor()