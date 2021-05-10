"""
File: draw_line.py
Name: Johsuan
-------------------------
This program creates lines designated by the user through
user mouse clicks.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# This constant controls the size of the GOval
SIZE = 10
window = GWindow()

# This save the x and y for the first click
s_x = 0
s_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(m):
    global s_x, s_y
    circle = GOval(SIZE, SIZE)
    window.add(circle, x=m.x-SIZE/2, y=m.y-SIZE/2)
    s_x = m.x
    s_y = m.y
    onmouseclicked(line)


def line(k):
    global s_x, s_y, SIZE
    line = GLine(k.x, k.y, s_x, s_y)
    window.add(line)
    # remove spot1
    circle = window.get_object_at(s_x-SIZE/3, s_y-SIZE/3)
    if circle is not None:
        window.remove(circle)
    onmouseclicked(draw)



if __name__ == "__main__":
    main()
