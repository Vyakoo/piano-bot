import cv2
import mss
import numpy as np

import mouse
import keyboard

import time

mss = mss.mss()

mon = { # Size window
"top": 450,
"left": 605,
"width": 375, 
"height": 525
}

def findColor(color, img): # Find color

    our_map = (color[2], color[1], color[0], 255)

    indexes = np.where(np.all(img == our_map, axis=-1))
    our_crd = np.transpose(indexes)
    return our_crd
    

# Color
color = [17, 17, 17]

while True: # main cycle
    
    img = np.asarray(mss.grab(mon)) # Grab screen
    
    cv2.imshow('img', img) # Show screen
    cv2.moveWindow('img', 0,0)
    cv2.waitKey(1)

    result = findColor(color, img)
    if result.__len__():
        x = result[0][1] + mon.get('left') # coordinates
        y = result[0][0] + mon.get('top')
        
        mouse.move(x+50, y+100) # click
        mouse.click('left')



if __name__ == "__main__":
    main()
