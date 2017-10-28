SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 30
NUMBER_OF_DIRECTION = 4
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
MOVING_INDEX = 5
ALIEN_MOVING_INDEX = 1
ALIEN_RANDOM_STEP = 20
ALIEN_SAFE_DISTANCE = 150

# Color
WHITE = (255,255,255)
BLACK = (0,0,0)


def getDistance(rect1,rect2):
    return ((rect1.x-rect2.x)**2 + (rect1.y-rect2.y)**2) ** 0.5


def checkPostionBetweenRect(rect1,rect2):
    postionString = ""
    if rect1.center[1] < rect2.center[1]:
        postionString += "top"
    if rect1.center[1] > rect2.center[1]:
        postionString += "below"
    if rect1.center[0] > rect2.center[0]:
        postionString += "right"
    if rect1.center[0] < rect2.center[0]:
        postionString += "left"
    return postionString
