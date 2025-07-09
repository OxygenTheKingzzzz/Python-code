from turtle import *
from PIL import Image
import numpy as np

# Load and convert image
img = Image.open("47892058-6d6f-483e-ae00-ddf8e5fb3106.png")
img = img.resize((80, 100))  # Resize for turtle speed
img = img.convert('RGB')
pixels = np.array(img)

screen = Screen()
screen.setup(width=800, height=1000)
screen.bgcolor('white')
pen = Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

# Draw image pixel by pixel
for y in range(img.height):
    for x in range(img.width):
        r, g, b = pixels[y][x]
        pen.goto(x * 5 - 200, -y * 5 + 300)  # Position turtle
        pen.dot(5, (r/255, g/255, b/255))  # Draw a colored dot

done()
