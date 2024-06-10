from Controllers.KeyboardController import KeyboardController
from Game_Components.GameComponent import GameComponent
import pygame

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
gameComponent = GameComponent('blue', 50, 50)
keyboardController = KeyboardController()

gameComponent.setXCoordinate(int(WIDTH / 2))
gameComponent.setYCoordinate(int(HEIGHT / 2))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    keyboardController.getKeyboardInput()

    gameComponent.setXCoordinate(gameComponent.getXCoordinate() + keyboardController.getMovementAdditiveHorizontal())
    gameComponent.setYCoordinate(gameComponent.getYCoordinate() + keyboardController.getMovementAdditiveVertical())

    screen.blit(gameComponent.image, (gameComponent.getXCoordinate(), gameComponent.getYCoordinate()), gameComponent.image.get_rect())

    pygame.display.flip()
    clock.tick(60)

pygame.quit()