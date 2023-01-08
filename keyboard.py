import time
import RPi.GPIO as GPIO
from PCA9685 import PCA9685
import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    
    x,y = 90,90
    stdscr.addstr("Horizontal Motor: " + str(x) + "  ")
    stdscr.addstr("Vertical Motor:" + str(y))
    
    # starting motors
    # 0 = vertical
    # 1 = horizontal
    pwm = PCA9685()
    pwm.setPWMFreq(50)
    pwm.setRotationAngle(0,y)
    pwm.setRotationAngle(1,x)
    
    
    while True:
        key = stdscr.getkey()
        
        if key == "KEY_LEFT" and x > 0:
            x -= 1
            pwm.setRotationAngle(1,x)
        
        elif key == "KEY_RIGHT" and x < 180:
            x += 1
            pwm.setRotationAngle(1,x)
        
        elif key == "KEY_UP" and y < 180:
            y += 1
            pwm.setRotationAngle(1,y)
        
        elif key == "KEY_DOWN" and y > 0:
            y -= 1
            pwm.setRotationAngle(1,y)
        
       
        
        stdscr.clear()
        stdscr.addstr("Horizontal Motor: " + str(x) + "  ")
        stdscr.addstr("Vertical Motor:" + str(y))
        stdscr.addstr
        stdscr.refresh()
        
        

wrapper(main)
