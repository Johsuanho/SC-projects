"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['#FF8000', '#842B00', '#AD5A5A', '#FF7575']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    year_width = (width-GRAPH_MARGIN_SIZE*2)/len(YEARS)
    x = year_index * year_width+GRAPH_MARGIN_SIZE
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(0,GRAPH_MARGIN_SIZE,CANVAS_WIDTH,GRAPH_MARGIN_SIZE)
    canvas.create_line(0, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0,GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)
    canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       text=str(YEARS[0]), anchor=tkinter.NW)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i+1), 0, get_x_coordinate(CANVAS_WIDTH, i+1),
                           CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX,
                           CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    rank_width = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/MAX_RANK
    for i in range(len(lookup_names)):
        x_1 = 0
        y_1 = 0
        for k in YEARS:
            if k == YEARS[0]:
                x_2 = get_x_coordinate(CANVAS_WIDTH, YEARS.index(k))
                if str(k) in name_data[lookup_names[i]]:
                    rank = int(name_data[lookup_names[i]][str(k)])
                    y_1 = rank*rank_width+GRAPH_MARGIN_SIZE
                else:
                    rank = 0
                    y_1 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                x_1 = x_2
                if rank == 0:
                    canvas.create_text(x_2 + TEXT_DX, y_1 + TEXT_DX, text=lookup_names[i] + ' *',
                                       anchor=tkinter.NW, fill=COLORS[i % 4])
                else:
                    canvas.create_text(x_2 + TEXT_DX,
                                   y_1 + TEXT_DX, text=lookup_names[i]+ ' '+str(rank), anchor=tkinter.NW, fill=COLORS[i%4])
            else:
                x_2 = get_x_coordinate(CANVAS_WIDTH, YEARS.index(k))
                if str(k) in name_data[lookup_names[i]]:
                    rank = int(name_data[lookup_names[i]][str(k)])
                    y_2 = rank*rank_width+GRAPH_MARGIN_SIZE
                else:
                    rank = 0
                    y_2 = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                canvas.create_line(x_1, y_1, x_2, y_2, width=LINE_WIDTH, fill=COLORS[i%4])
                if rank == 0:
                    canvas.create_text(x_2 + TEXT_DX, y_2 + TEXT_DX, text=lookup_names[i] + ' *',
                                       anchor=tkinter.NW, fill=COLORS[i % 4])
                else:
                    canvas.create_text(x_2 + TEXT_DX, y_2+ TEXT_DX, text=lookup_names[i] + ' '+ str(rank), anchor=tkinter.NW,
                                   fill=COLORS[i % 4])
                x_1 = x_2
                y_1 = y_2




# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
