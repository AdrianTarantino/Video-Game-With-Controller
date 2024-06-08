class GameController():
  def __init__(self):
    self.movementAdditiveVertical: int = 0
    self.movementAdditiveHorizontal: int = 0

  def getMovementAdditiveHorizontal(self) -> int:
    return self.movementAdditiveHorizontal
  
  def setMovementAdditiveHorizontal(self, newMovementAdditiveHorizontal: int) -> None:
    pass

  def getMovementAdditiveVertical(self) -> int:
    # Returns the amount something should move on vertical axis.
    self.movementAdditiveVertical

  def setMovementAdditiveVertical(self, newMovementAdditiveVertical: int) -> None:
    pass
