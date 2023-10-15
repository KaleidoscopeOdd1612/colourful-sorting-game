import pygame as py
import random

# Start pygame library#
py.init()

# Define title of screen#
py.display.set_caption("Colourful Sorting")
# RGB define colour
Black = (0, 0, 0)
Green = (0, 255, 0)
# Define size of the screen#
screen_w = 1300
screen_h = 700
screen = py.display.set_mode((screen_w, screen_h))
icon = py.image.load("rainbowegg.png")
py.display.set_icon(icon)
# Background
background = py.image.load("factory.jpg")
# Display background colour
screen.fill(Black)

# Load font#
font_path = "ABG.ttf"
custom_font = py.font.Font(font_path, 70)
score = 0
text = f"score: {score}"
scorefont = custom_font.render(text, True, (255, 255, 255))
time = 5400  # 1800
text_time = f"time: {time}:"
timefont = custom_font.render(text_time, True, (255, 255, 255))

# Load image
belt_move = []
belt_rect = []
sorting_move = []
sorting_rect = []
sortout_move = []
sortout_belt_rect = []
base_pipe_list = []

for i in range(4):
    belt_animation = py.image.load("belt_animation.png")
    belt_move.append(py.transform.scale(belt_animation, (403, 403)))
    belt_rect.append(belt_move[i].get_rect())
    belt_rect[i].centerx = screen_w // 2
    belt_rect[i].centery = 0 + 86 * i
    sorting_rightleft = py.image.load("sorting_rightleft.png")
    sorting_move.append(py.transform.scale(sorting_rightleft, (403, 403)))
    sorting_rect.append(sorting_move[i].get_rect())
    sorting_rect[i].x = 1000
    sorting_rect[i].y = 1000
    sortout_belt = py.image.load("sortout_belt.png")
    sortout_move.append(py.transform.scale(sortout_belt, (403, 403)))
    sortout_belt_rect.append(sortout_move[i].get_rect())
    sortout_belt_rect[i].centerx = screen_w // 2
    sortout_belt_rect[i].y = 189 + 68 * i

for i in range(2):
    base_pipe = py.image.load("base_pipe.png")
    base_pipe_list.append(py.transform.scale(base_pipe, (400, 400)))

Automatic_belt = py.image.load("Automatic_belt.png")
Automatic_sorting = py.image.load("Automatic_sorting.png")
rightarrow = py.image.load("rightarrow.png")
leftarrow = py.image.load("leftarrow.png")
sortout = py.image.load("sortout.png")
downarrow = py.image.load("downarrow.png")
left_pipe = py.image.load("left_pipe.png")
right_pipe = py.image.load("right_pipe.png")

# define size
Automatic_belt = py.transform.scale(Automatic_belt, (400, 400))
Automatic_sorting = py.transform.scale(Automatic_sorting, (400, 400))
rightarrow = py.transform.scale(rightarrow, (400, 400))
leftarrow = py.transform.scale(leftarrow, (400, 400))
sortout = py.transform.scale(sortout, (400, 400))
downarrow = py.transform.scale(downarrow, (400, 400))
left_pipe = py.transform.scale(left_pipe, (400, 400))
right_pipe = py.transform.scale(right_pipe, (400, 400))

# Egg Load
set_one = []
set_one_rect = []
set_two = []
set_two_rect = []
set_three = []
set_three_rect = []

for i in range(2):
    red = py.image.load("redegg.png")
    set_one.append(py.transform.scale(red, (150, 150)))
    set_one_rect.append(set_one[i * 7].get_rect())
    set_one_rect[i * 7].centerx = screen_w // 2
    set_one_rect[i * 7].y = -10000
    set_one_rect[i * 7].width = 150
    set_one_rect[i * 7].height = 25
    orange = py.image.load("orangeegg.png")
    set_one.append(py.transform.scale(orange, (150, 150)))
    set_one_rect.append(set_one[i * 7 + 1].get_rect())
    set_one_rect[i * 7 + 1].centerx = screen_w // 2
    set_one_rect[i * 7 + 1].y = -10000
    set_one_rect[i * 7 + 1].width = 150
    set_one_rect[i * 7 + 1].height = 25
    yellow = py.image.load("yellowegg.png")
    set_one.append(py.transform.scale(yellow, (150, 150)))
    set_one_rect.append(set_one[i * 7 + 2].get_rect())
    set_one_rect[i * 7 + 2].centerx = screen_w // 2
    set_one_rect[i * 7 + 2].y = -10000
    set_one_rect[i * 7 + 2].width = 150
    set_one_rect[i * 7 + 2].height = 25
    green = py.image.load("greenegg.png")
    set_one.append(py.transform.scale(green, (150, 150)))
    set_one_rect.append(set_one[i * 7 + 3].get_rect())
    set_one_rect[i * 7 + 3].centerx = screen_w // 2
    set_one_rect[i * 7 + 3].y = -10000
    set_one_rect[i * 7 + 3].width = 150
    set_one_rect[i * 7 + 3].height = 25
    sky = py.image.load("skyegg.png")
    set_one.append(py.transform.scale(sky, (150, 150)))
    set_one_rect.append(set_one[i * 7 + 4].get_rect())
    set_one_rect[i * 7 + 4].centerx = screen_w // 2
    set_one_rect[i * 7 + 4].y = -10000
    set_one_rect[i * 7 + 4].width = 150
    set_one_rect[i * 7 + 4].height = 25
    blue = py.image.load("blueegg.png")
    set_one.append(py.transform.scale(blue, (150, 150)))
    set_one_rect.append(set_one[i * 7 + 5].get_rect())
    set_one_rect[i * 7 + 5].centerx = screen_w // 2
    set_one_rect[i * 7 + 5].y = -10000
    set_one_rect[i * 7 + 5].width = 150
    set_one_rect[i * 7 + 5].height = 25
    purple = py.image.load("purpleegg.png")
    set_one.append(py.transform.scale(purple, (150, 150)))
    set_one_rect.append(set_one[i * 7 + 6].get_rect())
    set_one_rect[i * 7 + 6].centerx = screen_w // 2
    set_one_rect[i * 7 + 6].y = -10000
    set_one_rect[i * 7 + 6].width = 150
    set_one_rect[i * 7 + 6].height = 25

for i in range(1):
    red = py.image.load("redegg.png")
    set_two.append(py.transform.scale(red, (150, 150)))
    set_two_rect.append(set_two[i * 7].get_rect())
    set_two_rect[i * 7].centerx = -4000
    set_two_rect[i * 7].y = -108
    orange = py.image.load("orangeegg.png")
    set_two.append(py.transform.scale(orange, (150, 150)))
    set_two_rect.append(set_two[i * 7 + 1].get_rect())
    set_two_rect[i * 7 + 1].centerx = -4000
    set_two_rect[i * 7 + 1].y = -108
    yellow = py.image.load("yellowegg.png")
    set_two.append(py.transform.scale(yellow, (150, 150)))
    set_two_rect.append(set_two[i * 7 + 2].get_rect())
    set_two_rect[i * 7 + 2].centerx = -4000
    set_two_rect[i * 7 + 2].y = -108
    green = py.image.load("greenegg.png")
    set_two.append(py.transform.scale(green, (150, 150)))
    set_two_rect.append(set_two[i * 7 + 3].get_rect())
    set_two_rect[i * 7 + 3].centerx = -4000
    set_two_rect[i * 7 + 3].y = -108
    sky = py.image.load("skyegg.png")
    set_two.append(py.transform.scale(sky, (150, 150)))
    set_two_rect.append(set_two[i * 7 + 4].get_rect())
    set_two_rect[i * 7 + 4].centerx = -4000
    set_two_rect[i * 7 + 4].y = -108
    blue = py.image.load("blueegg.png")
    set_two.append(py.transform.scale(blue, (150, 150)))
    set_two_rect.append(set_two[i * 7 + 5].get_rect())
    set_two_rect[i * 7 + 5].centerx = -4000
    set_two_rect[i * 7 + 5].y = -108
    purple = py.image.load("purpleegg.png")
    set_two.append(py.transform.scale(purple, (150, 150)))
    set_two_rect.append(set_two[i * 7 + 6].get_rect())
    set_two_rect[i * 7 + 6].centerx = -4000
    set_two_rect[i * 7 + 6].y = -108

for i in range(1):
    red = py.image.load("redegg.png")
    set_three.append(py.transform.scale(red, (150, 150)))
    set_three_rect.append(set_three[i * 7].get_rect())
    set_three_rect[i * 7].centerx = -4000
    set_three_rect[i * 7].y = -108
    orange = py.image.load("orangeegg.png")
    set_three.append(py.transform.scale(orange, (150, 150)))
    set_three_rect.append(set_three[i * 7 + 1].get_rect())
    set_three_rect[i * 7 + 1].centerx = -4000
    set_three_rect[i * 7 + 1].y = -108
    yellow = py.image.load("yellowegg.png")
    set_three.append(py.transform.scale(yellow, (150, 150)))
    set_three_rect.append(set_three[i * 7 + 2].get_rect())
    set_three_rect[i * 7 + 2].centerx = -4000
    set_three_rect[i * 7 + 2].y = -108
    green = py.image.load("greenegg.png")
    set_three.append(py.transform.scale(green, (150, 150)))
    set_three_rect.append(set_three[i * 7 + 3].get_rect())
    set_three_rect[i * 7 + 3].centerx = -4000
    set_three_rect[i * 7 + 3].y = -108
    sky = py.image.load("skyegg.png")
    set_three.append(py.transform.scale(sky, (150, 150)))
    set_three_rect.append(set_three[i * 7 + 4].get_rect())
    set_three_rect[i * 7 + 4].centerx = -4000
    set_three_rect[i * 7 + 4].y = -108
    blue = py.image.load("blueegg.png")
    set_three.append(py.transform.scale(blue, (150, 150)))
    set_three_rect.append(set_three[i * 7 + 5].get_rect())
    set_three_rect[i * 7 + 5].centerx = -4000
    set_three_rect[i * 7 + 5].y = -108
    purple = py.image.load("purpleegg.png")
    set_three.append(py.transform.scale(purple, (150, 150)))
    set_three_rect.append(set_three[i * 7 + 6].get_rect())
    set_three_rect[i * 7 + 6].centerx = -4000
    set_three_rect[i * 7 + 6].y = -108

# get_rect() can get for - width, height, size, centerx, centery, center
background_rect = background.get_rect()
Automatic_belt_rect = Automatic_belt.get_rect()
Automatic_sorting_rect = Automatic_sorting.get_rect()
rightarrow_rect = rightarrow.get_rect()
leftarrow_rect = leftarrow.get_rect()
sortout_rect = sortout.get_rect()
downarrow_rect = downarrow.get_rect()
left_pipe_rect = left_pipe.get_rect()
right_pipe_rect = right_pipe.get_rect()

# define the position of image
background_rect.center = (screen_w // 2, screen_h // 2)
Automatic_belt_rect.centerx = screen_w // 2
Automatic_belt_rect.y = 0
Automatic_sorting_rect.centerx = 1000
Automatic_sorting_rect.y = 1000
rightarrow_rect.centerx = 1000
rightarrow_rect.y = 1000
rightarrow_rect.width = 400
rightarrow_rect.height = 150
leftarrow_rect.centerx = 1000
leftarrow_rect.y = 1000
leftarrow_rect.width = 400
leftarrow_rect.height = 150
sortout_rect.centerx = screen_w // 2
sortout_rect.y = 375
downarrow_rect.centerx = screen_w // 2
downarrow_rect.y = 400
left_pipe_rect.x = 126
left_pipe_rect.y = 274
right_pipe_rect.x = 774
right_pipe_rect.y = 299

# random function#
distance = 180
speed = 12
order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
attach = []
random_number = random.choice(order)


def Shuffle(ordeal):
    global random_number
    random_number = random.choice(ordeal)
    return random_number


set_one_rect[random_number].y = -108
order.remove(random_number)


def reset(Y):
    global random_number, distance, order, attach
    if Y == distance:
        Shuffle(order)
        set_one_rect[random_number].centerx = screen_w // 2
        set_one_rect[random_number].y = -108
        attach.append(random_number)
        if len(order) > 0:
            order.remove(random_number)
    if Y == 624:
        if len(attach) > 0:
            order.append(attach[0])
            attach.pop(0)


def show_animation():
    global speed, order
    for i in range(len(set_one)):
        reset(set_one_rect[i].y)
    for i in range(len(set_one)):
        Isright(i)
        Isleft(i)
        set_one_rect[i].y += speed
        screen.blit(set_one[i], set_one_rect[i])


# sorting system#
R = 0
L = 0


def pipe_sign_right():
    global R
    R = random.randint(0, len(set_two) - 1)
    set_two_rect[R].x = 899
    set_two_rect[R].y = 433
    return R


def pipe_sign_left():
    global L
    L = random.randint(0, len(set_three) - 1)
    set_three_rect[L].x = 255
    set_three_rect[L].y = 433
    return L


pipe_sign_right()
pipe_sign_left()


def Isright(r):
    for i in range(len(set_one)):
        if set_one_rect[i].colliderect(rightarrow_rect):
            set_one_rect[r].y -= speed
            set_one_rect[i].x += 48
            screen.blit(set_one[i], set_one_rect[i])


def Isleft(l):
    for i in range(len(set_one)):
        if set_one_rect[i].colliderect(leftarrow_rect):
            set_one_rect[l].y -= speed
            set_one_rect[i].x -= 48
            screen.blit(set_one[i], set_one_rect[i])


def Iscollisionrightorleft():
    global order, attach, score
    for i in range(len(set_two)):
        if set_one_rect[i].colliderect(set_two_rect[i]):
            set_one_rect[i].y = -10000
            set_two_rect[i].y = -4000
            if len(attach) > 0:
                order.append(attach[0])
                attach.pop(0)
            score += 1
            pipe_sign_right()
        if set_one_rect[i].colliderect(set_three_rect[i]):
            set_one_rect[i].y = -10000
            set_three_rect[i].y = -4000
            if len(attach) > 0:
                order.append(attach[0])
                attach.pop(0)
            score += 1
            pipe_sign_left()
        if set_one_rect[i + 7].colliderect(set_two_rect[i]):
            set_one_rect[i].y = -10000
            set_two_rect[i].y = -4000
            if len(attach) > 0:
                order.append(attach[0])
                attach.pop(0)
            score += 1
            pipe_sign_right()
        if set_one_rect[i + 7].colliderect(set_three_rect[i]):
            set_one_rect[i].y = -10000
            set_three_rect[i].y = -4000
            if len(attach) > 0:
                order.append(attach[0])
                attach.pop(0)
            score += 1
            pipe_sign_left()

    for i in range(len(set_one)):
        for j in range(len(set_two)):
            if (i != j or i != j + 7) and set_one_rect[i].colliderect(set_two_rect[j]):
                set_one_rect[i].y = -10000
                if len(attach) > 0:
                    order.append(attach[0])
                    attach.pop(0)
            if (i != j or i != j + 7) and set_one_rect[i].colliderect(set_three_rect[j]):
                set_one_rect[i].y = -10000
                if len(attach) > 0:
                    order.append(attach[0])
                    attach.pop(0)


# variable use for animation
FPS = 30  # variable use for frame rate
clock = py.time.Clock()  # Use the Clock function
belt_bound = 144
sorting_bound_right = 610
sorting_bound_left = 300
sortout_belt_bound = 461
# Event detector#
right = False
left = False
down = True
running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    time -= 1
    text_time = f"time: {time}"
    timefont = custom_font.render(text_time, True, (255, 255, 255))
    text = f"score: {score}"
    scorefont = custom_font.render(text, True, (255, 255, 255))
    if time == 0:
        running = False
    # fill the screen again every time of while running
    screen.fill(Black)

    keys = py.key.get_pressed()  # get all value of pressed of keyboard

    if keys[py.K_UP]:  # if press up arrow
        pass

    if keys[py.K_DOWN]:  # if press down arrow
        for i in range(4):
            sorting_rect[i].x = 1000
            sorting_rect[i].y = 1000

        Automatic_sorting_rect.centerx = 1000
        Automatic_sorting_rect.y = 1000
        rightarrow_rect.centerx = 1000
        rightarrow_rect.y = 1000
        leftarrow_rect.centerx = 1000
        leftarrow_rect.y = 1000
        sortout_rect.centerx = screen_w // 2
        sortout_rect.y = 375

        for i in range(4):
            sortout_belt_rect[i].centerx = screen_w // 2
            sortout_belt_rect[i].y = 189 + 68 * i

        downarrow_rect.centerx = screen_w // 2
        downarrow_rect.y = 400
        down = True

    if keys[py.K_RIGHT]:  # if press right arrow
        for i in range(4):
            sortout_belt_rect[i].centerx = 1000
            sortout_belt_rect[i].y = 1000

        sortout_rect.centerx = 1000
        sortout_rect.y = 1000
        downarrow_rect.centerx = 1000
        downarrow_rect.y = 1000
        down = False
        leftarrow_rect.centerx = 1000
        leftarrow_rect.y = 1000
        Automatic_sorting_rect.centerx = screen_w // 2
        Automatic_sorting_rect.y = 277
        rightarrow_rect.centerx = screen_w // 2
        rightarrow_rect.y = 400

        for i in range(4):
            sorting_rect[i].x = 300 + 78 * i
            sorting_rect[i].y = 390

        right = True
        left = False

    if keys[py.K_LEFT]:  # if press left arrow
        sortout_rect.centerx = 1000
        sortout_rect.y = 1000

        for i in range(4):
            sortout_belt_rect[i].centerx = 1000
            sortout_belt_rect[i].y = 1000

        downarrow_rect.centerx = 1000
        downarrow_rect.y = 1000
        down = False
        rightarrow_rect.centerx = 1000
        rightarrow_rect.y = 1000
        Automatic_sorting_rect.centerx = screen_w // 2
        Automatic_sorting_rect.y = 277
        leftarrow_rect.centerx = screen_w // 2
        leftarrow_rect.y = 400

        for i in range(4):
            sorting_rect[i].x = 610 - 78 * i
            sorting_rect[i].y = 390

        right = False
        left = True

    for i in range(4):
        if belt_rect[i].y < belt_bound:
            belt_rect[i].y += speed
        elif belt_rect[i].y >= belt_bound:
            belt_rect[i].centery = 0
        if sorting_rect[i].x < sorting_bound_right and right == True:
            sorting_rect[i].x += speed
        elif sorting_rect[i].x >= sorting_bound_right and right == True:
            sorting_rect[i].x = 300
        if sorting_rect[i].x > sorting_bound_left and left == True:
            sorting_rect[i].x -= speed
        elif sorting_rect[i].x <= sorting_bound_left and left == True:
            sorting_rect[i].x = 610
        if sortout_belt_rect[i].y < sortout_belt_bound and down == True:
            sortout_belt_rect[i].y += speed
        elif sortout_belt_rect[i].y >= sortout_belt_bound and down == True:
            sortout_belt_rect[i].y = 189

    # screen.blit(variable,dest)
    # dest = top left position of text, image
    # img_rect = using the current data that record in img_rect
    # screen.blit is use for something that had base data in file like font, image because those need a
    # reference from the outside unlike shape draw that draw from program not outside files
    screen.blit(background, background_rect)
    screen.blit(Automatic_belt, Automatic_belt_rect)
    screen.blit(Automatic_sorting, Automatic_sorting_rect)
    screen.blit(sortout, sortout_rect)

    for i in range(4):
        screen.blit(belt_move[i], belt_rect[i])
        screen.blit(sorting_move[i], sorting_rect[i])
        screen.blit(sortout_move[i], sortout_belt_rect[i])

    screen.blit(rightarrow, rightarrow_rect)
    screen.blit(leftarrow, leftarrow_rect)
    screen.blit(downarrow, downarrow_rect)

    screen.blit(base_pipe_list[0], (126, 274))
    screen.blit(base_pipe_list[1], (761, 274))

    show_animation()
    Iscollisionrightorleft()

    screen.blit(left_pipe, left_pipe_rect)
    screen.blit(right_pipe, right_pipe_rect)

    screen.blit(set_two[R], set_two_rect[R])
    screen.blit(set_three[L], set_three_rect[L])

    screen.blit(scorefont, (10, 0))
    screen.blit(timefont, (10, 70))

    # Update to screen
    py.display.flip()
    # Update display for 30 time per second
    clock.tick(FPS)
py.quit()