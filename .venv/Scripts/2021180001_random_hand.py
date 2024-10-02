from pico2d import *
from random import *

width=1000
height=800

open_canvas(width, height)
hand = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')
ground=load_image('TUK_GROUND_FULL.png')

hand_flag=True
hand_x=0
hand_y=0
dx=width//2
dy=height//2
direct=0
frame = 0
def random_hand():
    global hand_x,hand_y,hand_flag
    if hand_flag:
        hand_x=randint(0, width-1)
        hand_y=randint(0, height-1)
        hand_flag=False

def draw_scene():
    global hand_x,hand_y, dx, dy, frame, direct
    clear_canvas()
    ground.draw(width//2, height//2)
    hand.draw(hand_x, hand_y)
    if direct>0:
        character.clip_draw(frame*100, 100, 100, 100, dx, dy)
    else:
        character.clip_draw(frame * 100, 0, 100, 100, dx, dy)

    update_canvas()
    frame=(frame+1)%8
    delay(0.05)


def trace_hand():
    global hand_x, hand_y, hand_flag, dx, dy, direct

    if not hand_flag:
        direct=hand_x-dx
        for i in range(0, 100 + 1):
            t = i / 100
            dx = (1 - t) * dx + t * hand_x
            dy = (1 - t) * dy + t * hand_y
            distance = ((hand_x-dx)**2 + (hand_y-dy)**2)**0.5
            if distance < 1:
                break;
            draw_scene()
        dx=hand_x
        dy=hand_y
        draw_scene()

def check():
    global hand_x, hand_y, hand_flag, dx, dy
    if dx==hand_x and dy==hand_y:
        hand_flag=True

while True:

    
    random_hand()
    trace_hand()
    check()

