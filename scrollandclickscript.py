import mouse
import time

i = 0
while i == 0:
    mouse.click(button='left')
    # mouse.release(button='left')
    mouse.wheel(delta=-1)

    if mouse.is_pressed(button='middle'):
        i += 1

    if mouse.is_pressed(button='right'):
        i += 1

    time.sleep(3)
