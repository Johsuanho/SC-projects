"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
Note: This program sets the environment for basic brick
 breaking game
Revised: Johsuan
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width) / 2,
                            y=window_height - paddle_height - paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = '#003300'
        self.paddle.color = '#003300'
        self.window.add(self.paddle)
        self.paddle_offset = paddle_offset

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=window_width / 2 - ball_radius,
                          y=window_height / 2 - ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        x = random.randint(1, MAX_X_SPEED)
        self.__dx = x
        if (random.random() > 0.5):
            self.__dx = -self.__dx

        # Draw bricks
        for i in range(0, brick_rows):
            for k in range(0, brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if k <= 1:
                    self.brick.fill_color = '#26734d'
                    self.brick.color = '#26734d'
                if 1 < k <= 4:
                    self.brick.fill_color = '#339966'
                    self.brick.color = '#339966'
                if 4 < k <= 7:
                    self.brick.fill_color = '#53c68c'
                    self.brick.color = '#53c68c'
                if 7 < k <= 10:
                    self.brick.fill_color = '#8cd9b3'
                    self.brick.color = '#8cd9b3'
                if 10 < k:
                    self.brick.fill_color = '#c6ecd9'
                    self.brick.color = '#c6ecd9'
                self.window.add(self.brick, x=i * (brick_width + brick_spacing),
                                y=brick_offset + k * (+brick_height + brick_spacing))

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)

    def paddle_move(self, m):
        """
        This program defines the movement of paddle. Paddle moves
        according to the mouse movement on a constant y level.
        """
        if m.x < 0:
            self.paddle.x = 0
            self.paddle.y = self.window.height - self.paddle.height - self.paddle_offset
        if 0 <= m.x < self.window.width:
            self.paddle.x = m.x - self.paddle.width / 2
            self.paddle.y = self.window.height - self.paddle.height - self.paddle_offset
        if m.x + self.paddle.width >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
            self.paddle.y = self.window.height - self.paddle.height - self.paddle_offset

    # Set getter for vx and vy
    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    # Set setter for vx and vy
    def set_vx(self, vx):
        self.__dx = vx

    def set_vy(self, vy):
        self.__dy = vy
