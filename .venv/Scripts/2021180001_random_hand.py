from pico2d import *
from random import *

width=800
height=600

open_canvas(width, height)
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')
ground=load_image('TUK_GROUND_FULL.png')

hand_flag=True
hand_x=0
hand_y=0
char_x=0
char_y=0
dx=0
dy=0

def random_hand():
    global hand_x,hand_y,hand_flag
    if hand_flag:
        hand_x=randint(0, 800)
        hand_y=randint(0, 600)
        hand_flag=False
def trace_hand():
    global hand_x,hand_y,hand_flag,char_x,char_y
    if not hand_flag:
        pass
def check():
    pass
def draw_scene():
    clear_canvas()
    hand.draw(hand_x, hand_y)
    update_canvas()


while True:

    random_hand()
    trace_hand()
    check()
    draw_scene()
