import PySimpleGUI as sg

from utils import shark_icon, pilot_icon, images
from utils import update_images, randomize
from utils import make_shark, make_pilotfish, position_pilotfish

direction, position = randomize()
shark_list = [make_shark(direction)]
pilotfish_list = [make_pilotfish(shark_list[0])]

while shark_list:
    for shark in shark_list:
        event, values = shark.read(timeout=15)
        if event == sg.TIMEOUT_KEY:
            shark_x, shark_y = shark.CurrentLocation()
            last_shark_x = shark.metadata['last_shark_x']
            last_shark_y = shark.metadata['last_shark_y']
            if (shark_x, shark_y) != (last_shark_x, last_shark_y):
                if shark_x > (last_shark_x + 10):
                    direction = 'right'
                elif shark_x < (last_shark_x - 10):
                    direction = 'left'
                pilot = pilotfish_list[shark_list.index(shark)]
                update_images(shark, pilot, direction)
                position_pilotfish(pilot, direction)
                shark.metadata['last_shark_x'] = shark_x
                shark.metadata['last_shark_y'] = shark_y
        elif event == 'Add another pair':
            direction, position = randomize()
            next_shark_str = 'shark' + str(len(shark_list))
            next_pilot_str = 'pilot' + str(len(shark_list))
            exec(f'{next_shark_str} = make_shark("{direction}")')
            exec(f'shark_list.append({next_shark_str})')
            exec(f'{next_pilot_str} = make_pilotfish({next_shark_str})')
            exec(f'pilotfish_list.append({next_pilot_str})')
        elif event == 'Exit':
            shark.metadata['pilot'].close(), position
            shark.close()
            del pilotfish_list[shark_list.index(shark)]
            shark_list.remove(shark)
        elif event == 'Close all':
            shark_list = []
            break
