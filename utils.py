from random import choice, shuffle
import sys

import PySimpleGUI as sg

shark_image, pilot_image = None, None
directions = ['left', 'right']
positions = ['above', 'below_front', 'below_rear']

def randomize():
    shuffle(directions)
    shuffle(positions)
    direction = choice(directions)
    position = choice(positions)
    return direction, position

if sys.platform.startswith("win"):
    shark_icon = 'images/win_blueshark48.ico'
    pilot_icon = 'images/win_pilotfish48.ico'
    images = {'left':  {'shark': 'images/win_blueshark_l.png',
                        'pilot': 'images/win_pilotfish_l.png'},
              'right': {'shark': 'images/win_blueshark_r.png',
                        'pilot': 'images/win_pilotfish_r.png'}}
else:
    shark_icon = 'images/icon_blueshark.png'
    pilot_icon = 'images/icon_pilotfish.png'
    images = {'left':  {'shark': 'images/blueshark_l.png',
                        'pilot': 'images/pilotfish_l.png'},
              'right': {'shark': 'images/blueshark_r.png',
                        'pilot': 'images/pilotfish_r.png'}}


def get_images(direction):
    return images[direction]['shark'], images[direction]['pilot']


def update_images(shark, pilot, direction):
    shark_image, pilot_image = get_images(direction)
    shark['-SHARK-'].update(shark_image)
    pilot['-PILOT-'].update(pilot_image)


def position_pilotfish(pilot_win, direction):
    shark_win = pilot_win.metadata['shark']
    shark_w, shark_h = shark_win.size
    pilot_w, pilot_h = pilot_win.size
    shark_x, shark_y = shark_win.CurrentLocation()
    last_shark_x, last_shark_y = shark_x, shark_y
    position = pilot_win.metadata['position']

    if direction == 'left':
        if position == 'above': # above and behind left-facing shark
            pilot_x = shark_x + 10
            pilot_y = shark_y + 10
        elif position == 'below_front': # below and before left-facing shark
            pilot_x = (shark_x + 20)
            pilot_y = (shark_y + shark_h - pilot_h - 20)
        elif position == 'below_rear': # below and behind left-facing shark
            pilot_x = round(shark_x + shark_w - pilot_w - 35)
            pilot_y = (shark_y + shark_h - pilot_h - 35)
    elif direction == 'right':
        if position == 'above':
            pilot_x = shark_x + shark_w - pilot_w - 10
            pilot_y = shark_y + 10
        elif position == 'below_front':
            pilot_x = round(shark_x + shark_w - pilot_w - 20)
            pilot_y = round(shark_y + shark_h - pilot_h - 20)
        elif position == 'below_rear':
            pilot_x = round(shark_x + 35)
            pilot_y = round(shark_y + shark_h - pilot_h - 35)
    # else:  # keep pilotfish on right edge of sharkwindow
    #     pilot_x = round(shark_x + shark_w + 1)
    #     pilot_y = round(shark_y + shark_h/2 - pilot_h/2)
    pilot_win.SetAlpha(0)
    pilot_win.move(pilot_x, pilot_y)
    pilot_win.SetAlpha(1)


def make_shark(direction):
    shark_image = images[direction]['shark']
    shark_win = sg.Window(
        title='Shark Window',
        layout=[[sg.Image(filename=shark_image, key='-SHARK-')]],
        element_padding=(0,0),
        margins=(0,0),
        border_depth=0,
        grab_anywhere=True,
        no_titlebar=True,
        transparent_color='white',
        icon=shark_icon,
        right_click_menu = ['blah',['Continue', 'Add another pair', 'Exit', 'Close all'],],
        metadata={},
        finalize=True,
        )
    shark_x, shark_y = shark_win.CurrentLocation()
    shark_win.metadata['last_shark_x'] = shark_x
    shark_win.metadata['last_shark_y'] = shark_y
    shark_win.metadata['last_direction'] = direction
    return shark_win


def make_pilotfish(shark):
    direction = shark.metadata['last_direction']
    pilot_image = images[direction]['pilot']
    _, position = randomize()
    pilot_win = sg.Window(
        title='Pilot Fish Window',
        layout=[[sg.Image(filename=pilot_image, key='-PILOT-')]],
        element_padding=(0,0),
        margins=(0,0),
        border_depth=0,
        grab_anywhere=True,
        no_titlebar=True,
        keep_on_top=True,
        alpha_channel=0,
        transparent_color='white',
        icon=pilot_icon,
        metadata={'shark': shark, 'position': position},
        finalize=True,
        )
    position_pilotfish(pilot_win, direction)
    shark.metadata['pilot'] = pilot_win
    return pilot_win
