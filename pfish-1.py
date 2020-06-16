from random import choice, shuffle

import PySimpleGUI as sg
import imwatchingyou as sg_debug


def center_window(target_window):
    w, h = sg.Window.get_screen_size()
    ctr_x, ctr_y = (round(w/2), round(h/2))
    target_window.size
    target_window.move()

def set_images(direction):
    if direction == 'left':
        shark_win['-SHARK-'].update('blueshark_l.png')
        pilot_win['-PILOT-'].update('pilotfish_l.png')
    elif direction == 'right':
        shark_win['-SHARK-'].update('blueshark_r.png')
        pilot_win['-PILOT-'].update('pilotfish_r.png')

def locate_pilotfish():
    pass
    # global sx, sy
    # global direction, position, shark_win_width, shark_win_height
    # sx, sy = shark_win.CurrentLocation()
    # if direction == 'left':
    #     if position == 'above': # above and behind left-facting shark
    #         px = sx
    #         py = sy
    #     elif position == 'below_front': # below and before left-facting shark
    #         px = (sx + 10)
    #         py = (sy + shark_win_height - pilot_win_height)
    #     elif position == 'below_rear': # below and behind left-facting shark
    #         px = round(sx + (shark_win_width*3/5))
    #         py = (sy + shark_win_height - pilot_win_height)
    # elif direction == 'right':
    #     if position == 'above':
    #         px = (sx + shark_win_width)
    #         py = sy
    #     elif position == 'below_front':
    #         px = round(sx + (shark_win_width*18/25) + 1)
    #         py = round(sy + (shark_win_height*4/5) - pilot_win_height/2)
    #     elif position == 'below_rear':
    #         px = round(sx + (shark_win_width*1/5) + 1)
    #         py = round(sy + (shark_win_height*3/4) - pilot_win_height/2)
    # else:  # keep pilotfish on right edge of sharkwindow
    #     px = round(sx + shark_win_width + 1)
    #     py = round(sy + shark_win_height/2 - pilot_win_height/2)
    # pilot_win.move(px, py)

directions, positions = ['left', 'right'], ['above', 'below_front', 'below_rear']
shuffle(directions)
shuffle(positions)
direction = choice(directions); print(direction)
position = choice(positions); print(position)
last_direction = direction

shark_layout = [
    [sg.Image(filename=None, key='-SHARK-')],
    # [sg.Button('Debug')],
    ]

pilotfish_layout = [
    [sg.Image(filename=None, key='-PILOT-')],
    ]

shark_win = sg.Window('Shark Window',
    shark_layout,
    element_padding=(0,0),
    margins=(0,0),
    border_depth=0,
    grab_anywhere=True,
    # no_titlebar=True,
    finalize=True,
    )

shark_win_width, shark_win_height = shark_win.size
shark_win.move()

pilot_win = sg.Window('Pilot Fish Window',
    pilotfish_layout,
    background_color='red',
    transparent_color='red',
    element_padding=(0,0),
    margins=(0,0),
    border_depth=0,
    grab_anywhere=True,
    # no_titlebar=True,
    keep_on_top=True,
    finalize=True,
    )

set_images(direction)

while True:
    event, values = shark_win.read(timeout=50)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break



shark_win_width, shark_win_height = shark_win.size
pilot_win_width, pilot_win_height = pilot_win.size

sx, sy = shark_win.CurrentLocation()
last_sx, last_sy = sx, sy
print(sx, sy)
locate_pilotfish()


# while True:
#     sg_debug.refresh_debugger()
#     event, values = shark_win.read(timeout=50)
#     sx, sy = shark_win.CurrentLocation()
#     if event == '__TIMEOUT__':
#         if (sx, sy) != (last_sx, last_sy):
#             last_sx, last_sy = sx, sy
#             if sx > last_sx:
#                 if last_direction != 'right':
#                     direction = 'right'
#                     last_direction = 'right'
#                     print(f'Turned to the {direction}')
#                     set_images(direction)
#                     # locate_pilotfish()
#             elif sx < last_sx:
#                 if last_direction != 'left':
#                     direction = 'left'
#                     last_direction = 'left'
#                     print(f'Turned to the {direction}')
#                     set_images(direction)
#                     # locate_pilotfish()
#             locate_pilotfish()
#         continue
#     elif event in (sg.WIN_CLOSED, 'Exit'):
#         break
#     elif event == 'Debug':
#         sg_debug.show_debugger_window()
#         continue
#     # else:
#     # locate_pilotfish()

pilot_win.close()
shark_win.close()
