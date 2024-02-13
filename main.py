from pynput import keyboard

def on_press(key):
    try:
        if key == '\t':
            print("f.jeden('tab')")
    except AttributeError:
        pass

# Tworzymy obiekt monitora klawiatury
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
