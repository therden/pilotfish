from random import choice, shuffle

import PySimpleGUI as sg

directions, positions = ['left', 'right'], ['above', 'below_front', 'below_rear']
shuffle(directions); shuffle(positions)
direction = choice(directions); last_direction = direction
position = choice(positions)

def get_images():
    global shark_image, pilot_image

    if direction == 'left':
        shark_image = 'images/blueshark_l.png'
        pilot_image = 'images/pilotfish_l.png'
    elif direction == 'right':
        shark_image = 'images/blueshark_r.png'
        pilot_image = 'images/pilotfish_r.png'

def update_images():
    get_images()
    shark_win['-SHARK-'].update(shark_image)
    pilot_win['-PILOT-'].update(pilot_image)

def position_pilotfish():
    global shark_x, shark_y
    shark_x, shark_y = shark_win.CurrentLocation()
    if direction == 'left':
        if position == 'above': # above and behind left-facting shark
            pilot_x = shark_x + 10
            pilot_y = shark_y + 10
        elif position == 'below_front': # below and before left-facting shark
            pilot_x = (shark_x + 20)
            pilot_y = (shark_y + shark_h - pilot_h - 20)
        elif position == 'below_rear': # below and behind left-facting shark
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
    pilot_win.move(pilot_x, pilot_y)


get_images()

shark_win = sg.Window(
    title='Shark Window',
    layout=[[sg.Image(filename=shark_image, key='-SHARK-')]],
    element_padding=(0,0),
    margins=(0,0),
    border_depth=0,
    grab_anywhere=True,
    no_titlebar=True,
    finalize=True,
    )

pilot_win = sg.Window(
    title='Pilot Fish Window',
    layout=[[sg.Image(filename=pilot_image, key='-PILOT-')]],
    element_padding=(0,0),
    margins=(0,0),
    border_depth=0,
    grab_anywhere=True,
    no_titlebar=True,
    keep_on_top=True,
    finalize=True,
    )

shark_w, shark_h = shark_win.size
pilot_w, pilot_h = pilot_win.size
# shark_x, shark_y = shark_win.CurrentLocation()

position_pilotfish()

while True:
    event, values = shark_win.read(timeout=50)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
