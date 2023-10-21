GAME_SIZE = (26*40, 600)
PLAYER_SIZE_W = 96
PLAYER_SIZE_H = 128
SPRITE_SIZE_W = 40
SPRITE_SIZE_H = 40
PLAYER_RES = (

    'projects/smallgame/playball/res/player/0.png',
    'projects/smallgame/playball/res/player/1.png',
    'projects/smallgame/playball/res/player/2.png',
    'projects/smallgame/playball/res/player/3.png',
    'projects/smallgame/playball/res/player/4.png',
    'projects/smallgame/playball/res/player/5.png',
    'projects/smallgame/playball/res/player/6.png',
)

BALL_RES = "projects/smallgame/playball/res/ball.png"
BLOCK_RES_FMT = "projects/smallgame/playball/res/block/%d.png"
GAME_OVER_RES = "projects/smallgame/playball/res/lose.png"


class BlockType:
    NULL = 0
    SPEED_UP = 1
    NORMAL = 2
    COPY = 3
    SPEED_DOWN = 6
    WALL = 9


class SoundRes:
    JNTM = 'projects/smallgame/playball/snd/jntm.WAV'
    NGM = 'projects/smallgame/playball/snd/niganma.WAV'
