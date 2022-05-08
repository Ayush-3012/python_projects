import turtle
from turtle import *


#Draw a square
fillcolor('blue')
begin_fill()
for i in range(4):

    turtle.forward(200)
    turtle.left(90)

end_fill()


#calling for the mainloop()
turtle.mainloop()