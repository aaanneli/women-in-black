SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
CHARACTER_HEIGHT = 55
CHARACTER_WIDTH = 25
ALIEN_HEIGHT = 40
ALIEN_WIDTH = 20
NUMBER_OF_ALIENS = 15
BOSS_WIDTH = 60
BOSS_WIDTH_ALT = 40
BOSS_HEIGHT = 63
KEY_WIDTH = 30
KEY_HEIGHT = 30
NUM_GRID_ROWS = 6
NUM_GRID_COLS = 8
FPS = 30
NUMBER_OF_DIRECTION = 4
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
MOVING_INDEX = 5
ALIEN_MOVING_INDEX = 1
ALIEN_RANDOM_STEP = 20
ALIEN_SAFE_DISTANCE = 200
BOSS_MOVING_INDEX = MOVING_INDEX // 2
NUM_ROOMS = 7
WALL_WIDTH = 4
DOOR_WIDTH = 6
TILE_WIDTH = SCREEN_WIDTH * 1.0 / NUM_GRID_COLS
TILE_HEIGHT = SCREEN_HEIGHT * 1.0 / NUM_GRID_ROWS
DOOR_OFFSET = TILE_HEIGHT / 4.0

# Color
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (138, 140, 142)
BROWN = (119, 78, 8)
YELLOW = (243, 247, 17)


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

def checkPositionBetweenWall(wallRect, player):
    
    positionString = ""
    xDiff = abs(wallRect.center[0] - player.center[0])
    yDiff = abs(wallRect.center[1] - player.center[1])
    if yDiff < xDiff:
        if wallRect.bottom < player.center[1]:
            positionString += "top"
        elif wallRect.top > player.center[1]:
            positionString += "below"
            
    else:
        if wallRect.left > player.center[0]:
            positionString += "right"
        elif wallRect.right < player.center[0]:
            positionString += "left"

    if "2" in positionString:
        print(positionString)
    '''
    if wallRect.height > wallRect.width:
        pass
    else:
        pass
    '''
    return positionString
