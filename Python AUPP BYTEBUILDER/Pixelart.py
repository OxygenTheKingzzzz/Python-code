import turtle

# Define pixel size and color map
pixel_size = 20
colors = {
    "X": "black",
    " ": "white"
}

# 16x16 grid representing a GitHub logo (Octocat head style)
github_logo = [
    "      XX      ",
    "    XXXXXX    ",
    "   XXXXXXXX   ",
    "  XXX XX XXX  ",
    " XXX  XX  XXX ",
    " XXX      XXX ",
    " XXX XXXX XXX ",
    "  XXX XX XXX  ",
    "  XXXXXXXXXX  ",
    "   XX XX XX   ",
    "   X  XX  X   ",
    "   X  XX  X   ",
    "   X      X   ",
    "    XXXXXX    ",
    "              ",
    "              "
]

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.penup()

# Draw each pixel
for y in range(len(github_logo)):
    for x in range(len(github_logo[y])):
        char = github_logo[y][x]
        color = colors.get(char, "white")
        t.goto(x * pixel_size - 160, -y * pixel_size + 160)
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(4):
            t.pendown()
            t.forward(pixel_size)
            t.right(90)
        t.end_fill()
        t.penup()

t.hideturtle()
screen.mainloop()
