import pygame
from bird import Bird
from base import Base

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

# clock
clock = pygame.time.Clock()

# display msg


def msg(message, x, y, size):
    font = pygame.font.SysFont("Times new Roman", size)
    text = font.render(message, True, (100, 100, 100))
    scr.blit(text, (x, y))

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

        scr.fill((255, 255, 255))

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
                else:
                    bird.up()

        # score
        msg(f"Score:{Filter_score}", 30, 0, 30)

        # update sceen
        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    gameloop()
