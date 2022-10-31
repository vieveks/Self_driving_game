from sqlite3 import Time
import pyautogui as pt
import time 
print('hi')

screenWidth, screenHeight = pt.size()

#time.sleep(1)
#pt.moveTo(1100, 500)ṭ
human_max_speed = 700

def dist(x,y,a,b):
    return ((b-y)**2 + (a-x)**2)**(1/2)

def move(X,Y):
    x1,y1 = pt.position()
    time_cal = dist(x1,y1,X,Y) / human_max_speed
    print(time_cal)
    pt.moveTo(X,Y,time_cal)   

if __name__ == '__main__':
    
    time.sleep(1)
    print(pt.position)
    move(1000,700)
    

   
