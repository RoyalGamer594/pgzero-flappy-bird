import random

TITLE = "FLAPPY BIRD"

WIDTH = 395
HEIGHT = 650

bird = Actor("bird1", center=(WIDTH/2-100, HEIGHT/2))
top = Actor("top", anchor=("left","bottom"))
bottom = Actor("bottom", anchor=("left","top"))



bird.above_ground = 0
bird.dead = False

FALL = .6

JUMP = -9

SPEED = 3

GAP = 130

score = -1


def draw():
    global score
    screen.clear()
    screen.blit("background", (0,0))
    bird.draw()
    top.draw()
    bottom.draw()
    screen.draw.text(str(score), center=(WIDTH/2, 100), fontsize=50)
    if bird.dead == True:
        screen.draw.text("G A M E  O V E R", center=(WIDTH/2, HEIGHT/2), fontsize = 50)


def reset_pipes():
    pipe_gap = random.randint(200, HEIGHT - 200)
    top.pos = (WIDTH, pipe_gap - GAP // 2)
    bottom.pos = (WIDTH, pipe_gap + GAP // 2)

def update():

    global speed, score

    if bird.dead == False:

        bird.above_ground += FALL
        bird.y += bird.above_ground

        top.left -= SPEED
        bottom.left -= SPEED

        if top.left < 0:
            reset_pipes()
            top.left = WIDTH
            bottom.left = WIDTH

            if not bird.dead:
                score += 1

        if bird.above_ground <= -3:
            bird.image="bird1"
        else:
            bird.image="bird2"

        if bird.colliderect(top) or bird.colliderect(bottom):
            bird.dead = True
            bird.image = "birddead"



def on_key_down():
    if bird.dead == False:
        if keyboard.SPACE:
            bird.above_ground = JUMP
            bird.image = "bird2"