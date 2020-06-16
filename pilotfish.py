from random import choice, shuffle

import PySimpleGUI as sg

# directions, positions = ['left', 'right'], ['above', 'below_front', 'below_rear']
directions, positions = ['left', 'right'], ['above']
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

get_images()

shark_layout = [
    [sg.Image(filename=shark_image, key='-SHARK-')],
    # [sg.Button('Debug')],
    ]

pilotfish_layout = [
    [sg.Image(filename=pilot_image, key='-PILOT-')],
    ]

shark_win = sg.Window('Shark Window',
    shark_layout,
    element_padding=(0,0),
    margins=(0,0),
    border_depth=0,
    grab_anywhere=True,
    no_titlebar=True,
    finalize=True,
    )

pilot_win = sg.Window('Pilot Fish Window',
    pilotfish_layout,
    # background_color='red',
    # transparent_color='red',
    element_padding=(0,0),
    margins=(0,0),
    border_depth=0,
    grab_anywhere=True,
    no_titlebar=True,
    keep_on_top=True,
    finalize=True,
    )

def set_images():
    if direction == 'left':
        shark_win['-SHARK-'].update('images/blueshark_l.png')
        pilot_win['-PILOT-'].update('images/pilotfish_l.png')
    elif direction == 'right':
        shark_win['-SHARK-'].update('images/blueshark_r.png')
        pilot_win['-PILOT-'].update('images/pilotfish_r.png')

set_images()

while True:
    event, values = shark_win.read(timeout=50)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
