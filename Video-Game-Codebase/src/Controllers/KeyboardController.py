from Controllers.GameController import GameController
import pygame

class KeyboardController(GameController):
  def __init__(self):
    super().__init__()

    self.movementAdditive = 5

  def getKeyboardInput(self) -> None:
    if pygame.key.get_pressed()[pygame.K_w]:
      self.setMovementAdditiveVertical(-self.movementAdditive)

    if pygame.key.get_pressed()[pygame.K_s]:
      self.setMovementAdditiveVertical(self.movementAdditive)

    if pygame.key.get_pressed()[pygame.K_a]:
      self.setMovementAdditiveHorizontal(-self.movementAdditive)

    if pygame.key.get_pressed()[pygame.K_d]:
      self.setMovementAdditiveHorizontal(self.movementAdditive)