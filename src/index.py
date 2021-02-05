from pynput.mouse import Listener, Controller, Button
mouse = Controller() 
def on_scroll(x, y, dx, dy):
    # executed while pynput detects scroll
    print('Scroll Detected, Clicking')
    mouse.press(Button.left) #clicks, ofc
with Listener(on_scroll=on_scroll) as listener: # listening scrolls
    listener.join() # executes on_scroll