from argparse import ONE_OR_MORE
from pynput import *

def get_coords(x, y):
    print("Present coordinates: {}".format((x, y)))
    
with mouse.Listener(on_move=get_coords) as listen:
    listen.join()