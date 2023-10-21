GAME_SIZE = (800, 600)
PLAYER_SIZE_W = 96
PLAYER_SIZE_H = 128
SPRITE_SIZE_W = 40
SPRITE_SIZE_H = 40

PLAYER_RES = (

    'notes/smallgame/playball/res/player/0.png',
    'notes/smallgame/playball/res/player/1.png',
    'notes/smallgame/playball/res/player/2.png',
    'notes/smallgame/playball/res/player/3.png',
    'notes/smallgame/playball/res/player/4.png',
    'notes/smallgame/playball/res/player/5.png',
    'notes/smallgame/playball/res/player/6.png',
)

BALL_RES = "notes/smallgame/playball/res/ball.png"
BLOCK_RES_FMT = "notes/smallgame/playball/res/block/%d.png"

GAME_OVER_RES = "notes/smallgame/playball/res/lose.png"

class BlockType:
    NULL = 0
    SPEED_UP = 1
    NORMAL = 2
    COPY = 3
    SPEED_DOWN = 6
    WALL = 9

class SoundRes:
    JNTM = 'notes/smallgame/playball/snd/jntm.WAV'
    NGM = 'notes/smallgame/playball/snd/niganma.WAV'
