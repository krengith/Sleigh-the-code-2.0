import turtle
import random
import time

# ================= SCREEN =================
screen = turtle.Screen()
screen.setup(1100, 700)
screen.bgcolor("#0b1d3a")
screen.tracer(0)

# ================= PEN =================
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

GROUND_Y = -260
SCARF_OFFSET_X = 10   # <<< moves scarf to the right

# ================= MOON & STARS =================
def draw_moon_and_stars():
    pen.penup()
    pen.goto(420, 230)
    pen.color("#f5f3ce")
    pen.begin_fill()
    pen.pendown()
    pen.circle(45)
    pen.end_fill()

    pen.color("white")
    for _ in range(60):
        pen.penup()
        pen.goto(random.randint(-520, 520), random.randint(50, 330))
        pen.dot(random.randint(2, 3))

# ================= GROUND =================
def draw_ground(snow_height):
    pen.penup()
    pen.goto(-550, GROUND_Y + snow_height)
    pen.color("white")
    pen.begin_fill()
    pen.pendown()
    pen.goto(550, GROUND_Y + snow_height)
    pen.goto(550, -400)
    pen.goto(-550, -400)
    pen.goto(-550, GROUND_Y + snow_height)
    pen.end_fill()

# ================= TREE WITH TRUNK =================
def draw_tree(x, y, scale):
    # trunk
    pen.penup()
    pen.goto(x - 8 * scale, y - 30 * scale)
    pen.color("#6b3e26")
    pen.begin_fill()
    pen.pendown()
    pen.goto(x + 8 * scale, y - 30 * scale)
    pen.goto(x + 8 * scale, y)
    pen.goto(x - 8 * scale, y)
    pen.goto(x - 8 * scale, y - 30 * scale)
    pen.end_fill()

    # foliage
    pen.color("#0b6623")
    for i in range(3):
        pen.penup()
        pen.goto(x - 40 * scale + i * 6, y + i * 30)
        pen.begin_fill()
        pen.pendown()
        pen.goto(x + 40 * scale - i * 6, y + i * 30)
        pen.goto(x, y + 120 * scale + i * 12)
        pen.goto(x - 40 * scale + i * 6, y + i * 30)
        pen.end_fill()

# ================= SNOWMAN (FOREGROUND) =================
def draw_snowman():
    base_x = 220
    base_y = GROUND_Y + 10

    pen.color("white")

    # body
    for r, y in [(65, base_y), (50, base_y + 95), (35, base_y + 160)]:
        pen.penup()
        pen.goto(base_x, y)
        pen.begin_fill()
        pen.pendown()
        pen.circle(r)
        pen.end_fill()

    # eyes
    pen.color("black")
    pen.penup()
    pen.goto(base_x - 10, base_y + 200)
    pen.dot(5)
    pen.goto(base_x + 10, base_y + 200)
    pen.dot(5)

    # carrot nose
    pen.color("orange")
    pen.goto(base_x, base_y + 195)
    pen.setheading(0)
    pen.pendown()
    pen.forward(25)
    pen.penup()

    # buttons
    for y in [base_y + 120, base_y + 95, base_y + 70]:
        pen.goto(base_x, y)
        pen.dot(6)

    # ---- SCARF (SHIFTED RIGHT) ----
    pen.color("red")

    # neck wrap
    pen.penup()
    pen.goto(base_x - 55 + SCARF_OFFSET_X, base_y + 175)
    pen.begin_fill()
    pen.pendown()
    pen.goto(base_x + 55 + SCARF_OFFSET_X, base_y + 175)
    pen.goto(base_x + 55 + SCARF_OFFSET_X, base_y + 155)
    pen.goto(base_x - 55 + SCARF_OFFSET_X, base_y + 155)
    pen.goto(base_x - 55 + SCARF_OFFSET_X, base_y + 175)
    pen.end_fill()

    # hanging tail
    pen.penup()
    pen.goto(base_x + 30 + SCARF_OFFSET_X, base_y + 155)
    pen.begin_fill()
    pen.pendown()
    pen.goto(base_x + 55 + SCARF_OFFSET_X, base_y + 155)
    pen.goto(base_x + 45 + SCARF_OFFSET_X, base_y + 100)
    pen.goto(base_x + 25 + SCARF_OFFSET_X, base_y + 100)
    pen.goto(base_x + 30 + SCARF_OFFSET_X, base_y + 155)
    pen.end_fill()

    # twig arms
    pen.color("#6b3e26")
    pen.pensize(3)

    pen.penup()
    pen.goto(base_x - 50, base_y + 120)
    pen.setheading(160)
    pen.pendown()
    pen.forward(60)
    pen.left(30)
    pen.forward(20)
    pen.penup()

    pen.goto(base_x + 50, base_y + 120)
    pen.setheading(20)
    pen.pendown()
    pen.forward(60)
    pen.right(30)
    pen.forward(20)
    pen.penup()

    pen.pensize(1)

# ================= FALLING SNOW =================
snowflakes = []
for _ in range(80):
    flake = turtle.Turtle()
    flake.hideturtle()
    flake.penup()
    flake.color("white")
    flake.goto(random.randint(-550, 550), random.randint(-350, 350))
    flake.dot(random.randint(2, 3))
    flake.speed = random.uniform(0.15, 0.45)
    snowflakes.append(flake)

snow_level = 0

def animate_snow():
    global snow_level
    for flake in snowflakes:
        x, y = flake.position()
        y -= flake.speed
        if y < GROUND_Y + snow_level:
            y = random.randint(260, 350)
            x = random.randint(-550, 550)
            snow_level = min(snow_level + 0.01, 35)
        flake.goto(x, y)

# ================= MAIN LOOP =================
while True:
    pen.clear()

    draw_moon_and_stars()

    for x in range(-500, 500, 170):
        draw_tree(x, GROUND_Y + 50, 1.4)
    for x in range(-480, 480, 140):
        draw_tree(x, GROUND_Y + 30, 1.1)

    draw_ground(snow_level)

    draw_snowman()   # foreground

    animate_snow()

    screen.update()
    time.sleep(0.05)
