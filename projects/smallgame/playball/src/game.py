import pygame
import const
import player
import ball
import level
import block


class Game(object):
    def __init__(self, surface):
        pygame.mixer.init()
        self.surface = surface
        self.Load(1)

    def Load(self, lv):
        self.level = level.Level(lv)
        self.isGameOver = False
        self.balls = []
        self.loadPlayer()
        self.loadOneBall(self.player.GetRect().x, self.player.GetRect().y - const.SPRITE_SIZE_H - 5, 1, -1)
        self.loadBlockImages()

    def loadPlayer(self):
        self.player = player.Player(
            const.PLAYER_RES, (const.GAME_SIZE[0] - const.PLAYER_SIZE_W) / 2,
            const.GAME_SIZE[1] - const.PLAYER_SIZE_H, const.SPRITE_SIZE_W,
            const.GAME_SIZE[0] - const.PLAYER_SIZE_W - const.SPRITE_SIZE_W
        )

    def loadOneBall(self, x, y, dirX, dirY):
        tempBall = ball.Ball(const.BALL_RES, x, y, dirX, dirY)
        self.balls.append(tempBall)

    def loadBlockImages(self):
        self.blocks = []
        for tmpBlock in self.level.GetBlocks():
            sp = block.Block(tmpBlock[2], tmpBlock[0], tmpBlock[1], (0, 0))
            self.blocks.append(sp)

    def update(self):
        if self.isGameOver:
            return
        self.player.update()
        [ball.update() for ball in self.balls]
        self.checkCollide()
        if self.isGameWin():
            self.Load(self.level.level + 1)

    def draw(self) -> None:
        if self.isGameOver:
            img = pygame.image.load(const.GAME_OVER_RES)
            self.surface.blit(img, img.get_rect())
        else:
            self.player.draw(self.surface)
            [block.draw(self.surface) for block in self.blocks]
            [ball.draw(self.surface) for ball in self.balls]

    def checkBallBlockCollide(self):
        for tempBall in self.balls:
            for tempBlock in self.blocks:
                if tempBall.GetRect().colliderect(tempBlock.GetRect()):
                    tempBall.changeDirection(tempBlock.GetRect())
                    self.processBlock(tempBall, tempBlock)
                    break

    def processBlock(self, ball, tmpBlock):
        if tmpBlock.GetBlockType() == const.BlockType.COPY:
            self.copyBalls()
        if tmpBlock.GetBlockType() == const.BlockType.SPEED_UP:
            ball.SetSpeed(1.5)
        if tmpBlock.GetBlockType() == const.BlockType.SPEED_DOWN:
            ball.SetSpeed(0.2)
        if tmpBlock.GetBlockType() == const.BlockType.WALL:
            return
        self.blocks.remove(tmpBlock)

    def checkBallPlayerCollide(self):
        for tmpBall in self.balls:
            if tmpBall.GetRect().colliderect(self.player.GetRect()):
                tmpBall.changeYDirection(self.player.GetRect())
                break

    def checkCollide(self):
        self.checkBallBlockCollide()
        self.checkBallPlayerCollide()

        flag = True
        while flag:
            flag = False
            for tmpBall in self.balls:
                if tmpBall.GetRect().y > const.GAME_SIZE[1]:
                    self.balls.remove(tmpBall)
                    flag = True
                    break
        if len(self.balls) == 0:
            self.isGameOver = True

    def copyBalls(self):
        balls = [ball for ball in self.balls]
        for b in balls:
            self.loadOneBall(b.GetRect().x, b.GetRect().y, 1, -1)

    def isGameWin(self):
        for tmpBlock in self.blocks:
            if tmpBlock.GetBlockType() != const.BlockType.WALL:
                return False
        return True
