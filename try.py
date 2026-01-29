from pynput import keyboard

def on_prexss(key):
    print(f"Key pressed: {key}")

with keyboard.Listener(on_press=on_prexss) as listener:
    listener.join()
