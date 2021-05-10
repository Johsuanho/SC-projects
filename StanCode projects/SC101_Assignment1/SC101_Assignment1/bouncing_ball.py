"""
File: bouncing_ball.py
Name: Johsuan
-------------------------
This program stimulates a ball-drop from designated
starting point. The ball falls and moves according to
the constants given.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


DELAY = 10
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
click = 0
count = 0
VX = 3
VY = 0
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.fill_color = 'navy'
ball.color = 'navy'
window = GWindow(800, 500, title='bouncing_ball.py')
# control whether the "click" stimulates ball move
swich = True


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global swich
    window.add(ball)
    # when ball was added in the window, turn on the swich.
    #swich = True
    onmouseclicked(bouncing)


def bouncing(m):
    global window, count, VX, VY, click, swich
    GRAVITY = 1
    # ball moves when there were less then two ball bounced and when swich is on.
    if count <= 2 and swich is True:
        while True:
            # while ball is moving, turn off the swich
            swich = False
            ball.move(VX, VY)
            if ball.y + SIZE > window.height and VY >= GRAVITY/REDUCE:
                VY = -VY * REDUCE
            VY += GRAVITY
            if ball.x + SIZE >= window.width:
                # to make sure the ball will go out of the window
                ball.move(VX * 2, 0)
                count += 1
                # when ball counce is completed, turn on the swich for the next ball
                swich = True
                break
            pause(DELAY)
        window.add(ball, START_X, START_Y)





if __name__ == "__main__":
    main()
