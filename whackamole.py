import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        moleX = 3
        moleY = 3
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (moleX <= x + 16) and (moleX >= x - 16) and (moleY <= y + 16) and (moleX >= x - 16):
                        moleX = random.randrange(0, 20)*32 + 3
                        moleY = random.randrange(0, 16)*32 + 3

            screen.fill("light blue")

            for i in range(20):
                pygame.draw.line(screen, "black", (i*32, 0), (i*32, 512))
            for i in range(16):
                pygame.draw.line(screen, "black", (0, i*32), (640, i*32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(moleX, moleY)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
