import pygame
from bird import Bird
from base import Base
from enemy import Enemy
from time import sleep
import random

# initilaize
pygame.init()

# Gloabal value
WIDTH = 400
HEIGHT = 600
FPS = 30
SCORE = 0
GAME = True
Filter_score = 0

# screeen
scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whirlybird")
pygame.display.set_icon(pygame.image.load("img/android.png"))

# clock
clock = pygame.time.Clock()

# bg image
bgImg = pygame.image.load("img/bg.png")
bgImg = pygame.transform.scale(bgImg, (WIDTH, HEIGHT))

# display msg


def msg(message, x, y, size):
    font = pygame.font.SysFont("Times new Roman", size)
    text = font.render(message, True, (198, 234, 167))
    scr.blit(text, (x, y))


def gameOver():
    global GAME
    scr.fill((255, 255, 255))
    msg("GameOver", WIDTH/2-60, HEIGHT/2, 30)
    pygame.display.update()
    GAME = False
    sleep(2)

# HIGH score function


def HS(score):
    with open("HS.txt") as file:
        hs = int(file.read())  # 0
        if hs < score:
            with open("HS.txt", "w") as file:
                file.write(f"{score}")
            return score
        else:
            return hs

# gameloop


def gameloop():
    global WIDTH, HEIGHT, FPS, SCORE, GAME
    global Filter_score
    SCORE = 0
    GAME = True

    # bird
    bird = Bird(scr, WIDTH, HEIGHT, 25)
    bird.up()
    move_num = 0

    # enemy
    enemy = []
    for i in range(random.randrange(1, 4)):
        enemy.append(Enemy(scr, WIDTH, HEIGHT))

    # base
    base = []
    Total_base = 10
    for i in range(Total_base):
        base.append(Base(scr, WIDTH, HEIGHT))

    while GAME:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME = False

            # keystroke
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_num = -5
                if event.key == pygame.K_RIGHT:
                    move_num = 5
            if event.type == pygame.KEYUP:
                move_num = 0

        # scr.fill((255, 255, 255))
        scr.blit(bgImg, (0, 0))

        # bird
        bird.update()
        bird.move(move_num)
        bird.show()

        # base
        for i in base:
            i.show()

            # move base
            if bird.y <= 100:
                SCORE += 1
                Filter_score = SCORE//10
                i.move()

            # add base
            if i.y > HEIGHT:
                i.update_pos()

            # collision
            collision = i.collide(bird)
            if collision:
                if i.mode == "jump":
                    bird.up(20)
                elif i.mode == "danger":
                    print("Gameover")
                    gameOver()
                else:
                    bird.up()

        # enemy
        for i in enemy:
            i.show()
            i.move()

            if i.y > HEIGHT:
                i.update_pos()

            # collision
            if i.collide(bird):
                print("Gameover")
                gameOver()

            # move downward
            if bird.y <= 100:
                i.y += 5

        # if bird hit ground
        if bird.y >= HEIGHT-bird.r:
            print("Gameover")
            gameOver()

        # score
        msg(f"Score:{Filter_score}", 30, 0, 30)

        # For high score
        msg(f"HS:{HS(Filter_score)}", WIDTH-90, 0, 30)

        # update sceen
        clock.tick(FPS)
        pygame.display.update()


# =========================Main Condition=====================

if __name__ == "__main__":
    LOOP = True
    while LOOP:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LOOP = False
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_q]:
                LOOP = False
            elif pressed[pygame.K_SPACE]:
                gameloop()

        scr.fill((0, 0, 0))
        msg("Press space to play Q for quit", WIDTH/2-80, HEIGHT/2, 15)

        pygame.display.update()

# ===========================THE END==============================
