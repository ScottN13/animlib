import sys
import time
import turtle
 # import tkinter <--- This is only a plan for the future, it might break turtle idk, never read its documentation, just copied from google.

# Important turtle data
pen = turtle.Turtle()
screen = turtle.screensize(800,600)
pen.ht()


print("animlib inited")


class premade:
        # Pre-built animations.
        class console:
                def loading1(x,y) -> None:
                    top = "|"
                    right = ">"
                    left = "<"

                    if x == "load":
                        state = "loading...  "
                    elif x == "exit":
                        state = "exiting... "

                    for i in range(y):
                        print(state,top, end="\r")
                        time.sleep(0.5)
                        print(state,left, end="\r")
                        time.sleep(0.5)
                        print(state,top, end="\r")
                        time.sleep(0.5)
                        print(state,right, end="\r")
                        time.sleep(0.5)
                    
            
        class windowed:
            def square(color,width,speed,height,args):
                pen.color = color
                pen.width = width
                    
                if speed == str("default"): # Default turtle speeds (very fast, just like a timelapse)
                   print("default speed")

                elif speed == str("slow"): # Somewhat slow to observe the pen drawing.
                    pen.speed = 1

                elif speed == str("medium"): # Medium speed.
                    pen.speed = 3

                elif speed == str("fast"): # FASSTTTT
                    pen.speed = 5

                for i in range(4):
                    pen.fd(height)
                    pen.rt(90)

                if args == "none" or "":
                    print("Automatically exiting")
                if args == "exitonclick" or "manual":
                    turtle.exitonclick()

            def circle(color,width,speed,height):
                pen.color = color
                pen.width = width
                    
                if speed == str("default"): # Default turtle speeds (very fast, just like a timelapse)
                    print("default speed")

                elif speed == str("slow"): # Somewhat slow to observe the pen drawing.
                    pen.speed = int(1)

                elif speed == str("medium"): # Medium speed.
                    pen.speed = int(3)

                elif speed == str("fast"): # FASSTTTT
                    pen.speed = int(5)

                pen.circle(float(height),90)

                turtle.exitonclick()