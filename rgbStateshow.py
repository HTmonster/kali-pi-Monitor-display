import RPi.GPIO as GPIO

class rgbState(Object):
    ''' 显示状态的rgb灯 '''

    #简单的颜色映射
    color_map={
        'red':  (True,False,False),
        'green':(False,True,False),
        'blue': (False,False,True),
        'white':(True,True,True),
        'yellow':(True,True,False),
    }

    def __init__(self,R=27,G=28,B=29):
        
        # set mode
        GPIO.setmode(GPIO.BCM)

        # set out
        GPIO.setup(R, GPIO.OUT)
        GPIO.setup(G, GPIO.OUT)
        GPIO.setup(B, GPIO.OUT)

        # save rgb
        self.RGB=(R,G,B)
    
    def color_display(self,color):
        ''' 根据颜色进行显示 '''

        rgb=color_map.get(color,(False,False,False))

        for i in range(3):
            GPIO.output(self.RGB[i],rgb[i])


if __name__=="__main__":
    test=rgbState()
    import time
    test.color_display('red')
    time.sleep(2)
    test.color_display('green')
    time.sleep(2)
    test.color_display('blue')
    time.sleep(2)
    test.color_display('yellow')
    time.sleep(2)
    test.color_display('white')