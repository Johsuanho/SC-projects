"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.
Revised: Johsuan
"""

from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts
graphics = BreakoutGraphics()
count = 0
switch = True


def main():
    """
    This program stimulates the brick breaking game by mouse
    click. User have certain amount of chances to break all the brick.
    """
    onmouseclicked(ball_move)


def ball_move(m):
    """
    This program defines how the ball will move. Ball changes
    its direction when hitting walls and ceiling as well as
    when removing the brick.
    """
    global count, switch
    if count <= NUM_LIVES-1 and switch:
        switch = False
        while True:
            graphics.ball.move(graphics.get_vx(), graphics.get_vy())

            # set four corner of the ball as detect point for objects
            object1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            if object1 is not None and object1 is not graphics.paddle:
                graphics.window.remove(object1)
                graphics.set_vy(-graphics.get_vy())
            object2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
            if object2 is not None and object2 is not graphics.paddle:
                graphics.window.remove(object2)
                graphics.set_vy(-graphics.get_vy())
            object3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
            if object3 is not None and object3 is not graphics.paddle:
                graphics.window.remove(object3)
                graphics.set_vy(-graphics.get_vy())
            if object3 is graphics.paddle:
                graphics.set_vy(-graphics.get_vy())
            object4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                    graphics.ball.y+graphics.ball.height)
            if object4 is not None and object4 is not graphics.paddle:
                graphics.window.remove(object4)
                graphics.set_vy(-graphics.get_vy())
            if object4 is graphics.paddle:
                graphics.set_vy(-graphics.get_vy())

            # add the fifth spot at the bottom of the ball to detect the paddle
            object5 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                    graphics.ball.y + graphics.ball.height)
            if object5 is graphics.paddle:
                graphics.set_vy(-graphics.get_vy())

            # set ball bouncing function
            if graphics.ball.x + graphics.ball.width >= graphics.window.width or graphics.ball.x <= 0:
                graphics.set_vx(-graphics.get_vx())
            if graphics.ball.y <= 0:
                graphics.set_vy(-graphics.get_vy())
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                count += 1
                switch = True
                break
            pause(FRAME_RATE)
        graphics.window.add(graphics.ball, x=graphics.window.width/2-graphics.ball.width,
                            y=graphics.window.height/2-graphics.ball.height)


if __name__ == '__main__':
    main()
