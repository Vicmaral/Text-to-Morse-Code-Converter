from turtle import Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Text to Morse Code Converter")
screen.tracer(0)


is_on = True
while is_on:
    screen.update()


screen.exitonclick()