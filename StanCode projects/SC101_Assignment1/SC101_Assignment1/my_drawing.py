"""
File: my_drawing.py
Name: Johsuan
----------------------
This program draws the organization chart for the
SC101 class. With modification on name of TA and number
of students, this chart can be used for future classes.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon, GLabel
from campy.graphics.gwindow import GWindow

W = 1000
S = 120
window = GWindow(W, W/2)


def main():
    """
    This program draws an organization chart for the class
    SC101 on Sunday night.
    """
    title = GLabel ('SC101 Sunday Night Class')
    title.font = 'Verdana-18-bold'
    window.add(title, S/4,S/2 )
    source = GLabel ('Source: SC101 Week 1 handout.')
    source.font = 'Verdana-8'
    window.add(source, S/4,S*4)
    # add Jerry squares
    squ_j = GRect(S, S / 2)
    squ_j.filled = True
    squ_j.fill_color = '#b32d00'
    squ_j.color = '#b32d00'
    window.add(squ_j, (W - S) / 2, S)
    midj_x = (W - S) / 2 + S / 2
    midj_y = S + S / 4
    jerry = GLabel('Jerry')
    jerry.color = 'white'
    jerry.font = 'Verdana-15-bold'
    window.add(jerry, midj_x-S/4, midj_y+S/10)
    label1 = GRect(S/10, S/10)
    label1.filled = True
    label1.fill_color = '#b32d00'
    label1.color = '#b32d00'
    window.add(label1, W/10*8, S*3.5)
    label1_1 = GLabel('Teacher')
    label1_1.font = 'Verdana-8'
    window.add(label1_1, W/10*8.2, S*3.6)

    # add TA squares
    squ_t1 = GRect(S, S / 2)
    squ_t2 = GRect(S, S / 2)
    squ_t3 = GRect(S, S / 2)
    squ_t4 = GRect(S, S / 2)
    squ_t1.filled = True
    squ_t1.fill_color = '#ff8000'
    squ_t1.color = '#ff8000'
    squ_t2.filled = True
    squ_t2.fill_color = '#ff8000'
    squ_t2.color = '#ff8000'
    squ_t3.filled = True
    squ_t3.fill_color = '#ff8000'
    squ_t3.color = '#ff8000'
    squ_t4.filled = True
    squ_t4.fill_color = '#ff8000'
    squ_t4.color = '#ff8000'
    window.add(squ_t1, W / 2 - S * 3.5, S*2)
    window.add(squ_t2, W / 2 - S * 1.5, S * 2)
    window.add(squ_t3, W / 2 + S * 0.5, S * 2)
    window.add(squ_t4, W / 2 + S * 2.5, S * 2)
    midt1_x = W / 2 - S * 3.5 + S / 2
    midt2_x = W / 2 - S * 1.5 + S / 2
    midt3_x = W / 2 + S * 0.5 + S / 2
    midt4_x = W / 2 + S * 2.5 + S / 2
    midt_y = S * 2 + S / 4
    ta1 = GLabel('Douglas')
    ta1.font = 'Verdana-12-bold'
    window.add(ta1, midt1_x-S/3.5, midt_y+S/12)
    ta2 = GLabel('Wesker')
    ta2.font = 'Verdana-12-bold'
    window.add(ta2, midt2_x-S/3.5, midt_y+S/12)
    ta3 = GLabel('Dennis')
    ta3.font = 'Verdana-12-bold'
    window.add(ta3, midt3_x-S/3.5, midt_y+S/12)
    ta4 = GLabel('Gibbs')
    ta4.font = 'Verdana-12-bold'
    window.add(ta4, midt4_x-S/4.5, midt_y+S/12)
    label2 = GRect(S/10, S/10)
    label2.filled = True
    label2.fill_color = '#ff8000'
    label2.color = '#ff8000'
    window.add(label2, W/10*8, S*3.65)
    label2_1 = GLabel('Teaching Assistant')
    label2_1.font = 'Verdana-8'
    window.add(label2_1, W/10*8.2, S*3.75)

    # add student squares
    squ_s1 = GRect(S, S / 2)
    squ_s1.filled = True
    squ_s1.fill_color = '#ffe6cc'
    squ_s1.color = '#ffe6cc'
    squ_s2 = GRect(S, S / 2)
    squ_s2.filled = True
    squ_s2.fill_color = '#ffe6cc'
    squ_s2.color = '#ffe6cc'
    squ_s3 = GRect(S, S / 2)
    squ_s3.filled = True
    squ_s3.fill_color = '#ffe6cc'
    squ_s3.color = '#ffe6cc'
    squ_s4 = GRect(S, S / 2)
    squ_s4.filled = True
    squ_s4.fill_color = '#ffe6cc'
    squ_s4.color = '#ffe6cc'
    window.add(squ_s1, W / 2 - S * 3.5, S * 2.75)
    window.add(squ_s2, W / 2 - S * 1.5, S * 2.75)
    window.add(squ_s3, W / 2 + S * 0.5, S * 2.75)
    window.add(squ_s4, W / 2 + S * 2.5, S * 2.75)
    mids_y = S * 3 + S / 4
    s1 = GLabel('x 9')
    s1.font = 'Verdana-20'
    window.add(s1, midt1_x, mids_y-S/8)
    s2 = GLabel('x 9')
    s2.font = 'Verdana-20'
    window.add(s2, midt2_x, mids_y-S/8)
    s3 = GLabel('x 9')
    s3.font = 'Verdana-20'
    window.add(s3, midt3_x, mids_y-S/8)
    s3 = GLabel('x 9')
    s3.font = 'Verdana-20'
    window.add(s3, midt3_x, mids_y-S/8)
    s4 = GLabel('x 9')
    s4.font = 'Verdana-20'
    window.add(s4, midt4_x, mids_y-S/8)


    # add structure line
    l0 = GLine(midj_x, S * 1.5, midj_x, S * 1.75)
    l1 = GLine(midt1_x, S * 1.75, midt1_x, S * 2)
    l2 = GLine(midt2_x, S * 1.75, midt2_x, S * 2)
    l3 = GLine(midt3_x, S * 1.75, midt3_x, S * 2)
    l4 = GLine(midt4_x, S * 1.75, midt4_x, S * 2)
    l5 = GLine(midt1_x, S * 2.5, midt1_x, S * 2.75)
    l6 = GLine(midt2_x, S * 2.5, midt2_x, S * 2.75)
    l7 = GLine(midt3_x, S * 2.5, midt3_x, S * 2.75)
    l8 = GLine(midt4_x, S * 2.5, midt4_x, S * 2.75)
    l9 = GLine(midt1_x, S * 1.75, midt4_x, S * 1.75)
    window.add(l0)
    window.add(l1)
    window.add(l2)
    window.add(l3)
    window.add(l4)
    window.add(l5)
    window.add(l6)
    window.add(l7)
    window.add(l8)
    window.add(l9)

    # add little person1
    head1 = GOval(S * 0.15, S * 0.15)
    head1.filled = True
    head1.fill_color = '#b32d00'
    head1.color = '#b32d00'
    body1 = GPolygon()
    body1.add_vertex((midt1_x-S*0.33, S*2.94))
    body1.add_vertex((midt1_x - S * 0.415, S * 3.15))
    body1.add_vertex((midt1_x - S * 0.233, S * 3.15))
    foot1 = GRect(S*0.09, S*0.07, x=midt1_x-S * 0.373, y=S * 3.15)
    foot1.filled = True
    foot1.fill_color = '#b32d00'
    foot1.color = '#b32d00'
    window.add(foot1)
    body1.filled = True
    body1.fill_color = '#b32d00'
    body1.color = '#b32d00'
    window.add(head1, midt1_x - S * 0.4, S * 2.8)
    window.add(body1)

    # add little person2
    head2 = GOval(S * 0.15, S * 0.15)
    head2.filled = True
    head2.fill_color = '#e69900'
    head2.color = '#e69900'
    window.add(head2, midt1_x - S * 0.2, S * 2.8)
    body2 = GPolygon()
    body2.add_vertex((midt1_x-S*0.33+S*0.2, S*2.94))
    body2.add_vertex((midt1_x - S * 0.415+S*0.2, S * 3.15))
    body2.add_vertex((midt1_x - S * 0.233+S*0.2, S * 3.15))
    body2.filled = True
    body2.fill_color = '#e69900'
    body2.color = '#e69900'
    window.add(body2)
    foot2 = GRect(S*0.09, S*0.07, x=midt1_x-S * 0.373+S*0.2, y=S * 3.15)
    foot2.filled = True
    foot2.fill_color = '#e69900'
    foot2.color = '#e69900'
    window.add(foot2)

   # add little person3
    head3 = GOval(S * 0.15, S * 0.15)
    head3.filled = True
    head3.fill_color = '#b32d00'
    head3.color = '#b32d00'
    body3 = GPolygon()
    body3.add_vertex((midt2_x-S*0.33, S*2.94))
    body3.add_vertex((midt2_x - S * 0.415, S * 3.15))
    body3.add_vertex((midt2_x - S * 0.233, S * 3.15))
    foot3 = GRect(S*0.09, S*0.07, x=midt2_x-S * 0.373, y=S * 3.15)
    foot3.filled = True
    foot3.fill_color = '#b32d00'
    foot3.color = '#b32d00'
    window.add(foot3)
    body3.filled = True
    body3.fill_color = '#b32d00'
    body3.color = '#b32d00'
    window.add(head3, midt2_x - S * 0.4, S * 2.8)
    window.add(body3)

    # add little person4
    head4 = GOval(S * 0.15, S * 0.15)
    head4.filled = True
    head4.fill_color = '#e69900'
    head4.color = '#e69900'
    window.add(head4, midt2_x - S * 0.2, S * 2.8)
    body4 = GPolygon()
    body4.add_vertex((midt2_x-S*0.33+S*0.2, S*2.94))
    body4.add_vertex((midt2_x - S * 0.415+S*0.2, S * 3.15))
    body4.add_vertex((midt2_x - S * 0.233+S*0.2, S * 3.15))
    body4.filled = True
    body4.fill_color = '#e69900'
    body4.color = '#e69900'
    window.add(body4)
    foot4 = GRect(S*0.09, S*0.07, x=midt2_x-S * 0.373+S*0.2, y=S * 3.15)
    foot4.filled = True
    foot4.fill_color = '#e69900'
    foot4.color = '#e69900'
    window.add(foot4)


   # add little person5
    head5 = GOval(S * 0.15, S * 0.15)
    head5.filled = True
    head5.fill_color = '#b32d00'
    head5.color = '#b32d00'
    body5 = GPolygon()
    body5.add_vertex((midt3_x-S*0.33, S*2.94))
    body5.add_vertex((midt3_x - S * 0.415, S * 3.15))
    body5.add_vertex((midt3_x - S * 0.233, S * 3.15))
    foot5 = GRect(S*0.09, S*0.07, x=midt3_x-S * 0.373, y=S * 3.15)
    foot5.filled = True
    foot5.fill_color = '#b32d00'
    foot5.color = '#b32d00'
    window.add(foot5)
    body5.filled = True
    body5.fill_color = '#b32d00'
    body5.color = '#b32d00'
    window.add(head5, midt3_x - S * 0.4, S * 2.8)
    window.add(body5)

    # add little person6
    head6 = GOval(S * 0.15, S * 0.15)
    head6.filled = True
    head6.fill_color = '#e69900'
    head6.color = '#e69900'
    window.add(head6, midt3_x - S * 0.2, S * 2.8)
    body6 = GPolygon()
    body6.add_vertex((midt3_x-S*0.33+S*0.2, S*2.94))
    body6.add_vertex((midt3_x - S * 0.415+S*0.2, S * 3.15))
    body6.add_vertex((midt3_x - S * 0.233+S*0.2, S * 3.15))
    body6.filled = True
    body6.fill_color = '#e69900'
    body6.color = '#e69900'
    window.add(body6)
    foot6 = GRect(S*0.09, S*0.07, x=midt3_x-S * 0.373+S*0.2, y=S * 3.15)
    foot6.filled = True
    foot6.fill_color = '#e69900'
    foot6.color = '#e69900'
    window.add(foot6)

   # add little person7
    head7 = GOval(S * 0.15, S * 0.15)
    head7.filled = True
    head7.fill_color = '#b32d00'
    head7.color = '#b32d00'
    body7 = GPolygon()
    body7.add_vertex((midt4_x-S*0.33, S*2.94))
    body7.add_vertex((midt4_x - S * 0.415, S * 3.15))
    body7.add_vertex((midt4_x - S * 0.233, S * 3.15))
    foot7 = GRect(S*0.09, S*0.07, x=midt4_x-S * 0.373, y=S * 3.15)
    foot7.filled = True
    foot7.fill_color = '#b32d00'
    foot7.color = '#b32d00'
    window.add(foot7)
    body7.filled = True
    body7.fill_color = '#b32d00'
    body7.color = '#b32d00'
    window.add(head7, midt4_x - S * 0.4, S * 2.8)
    window.add(body7)

    # add little person8
    head8 = GOval(S * 0.15, S * 0.15)
    head8.filled = True
    head8.fill_color = '#e69900'
    head8.color = '#e69900'
    window.add(head8, midt4_x - S * 0.2, S * 2.8)
    body8 = GPolygon()
    body8.add_vertex((midt4_x-S*0.33+S*0.2, S*2.94))
    body8.add_vertex((midt4_x - S * 0.415+S*0.2, S * 3.15))
    body8.add_vertex((midt4_x - S * 0.233+S*0.2, S * 3.15))
    body8.filled = True
    body8.fill_color = '#e69900'
    body8.color = '#e69900'
    window.add(body8)
    foot8 = GRect(S*0.09, S*0.07, x=midt4_x-S * 0.373+S*0.2, y=S * 3.15)
    foot8.filled = True
    foot8.fill_color = '#e69900'
    foot8.color = '#e69900'
    window.add(foot8)

if __name__ == "__main__":
    main()
