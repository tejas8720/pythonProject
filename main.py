import time
import pyautogui
from tkinter import Tk, filedialog
from datetime import datetime

n=6
a=n-1
b=1
root = Tk()
root.withdraw()
root.attributes('-topmost', True)
open_file = filedialog.askdirectory()
print(open_file)

for i in range(n):
    print((" "*a)+"*"*b+(" "*a))
    b+=2
    a-=1
    time.sleep(5)
    filename1 = datetime.now().strftime("%Y_%m_%d-%H:%M:%S")
    pyautogui.screenshot((open_file+"/"+filename1+'.png'))