# Use tkinter GUI to open URL inside webview

from tkinter import Tk
from tkwebview2.tkwebview2 import WebView2, have_runtime, install_runtime
# clr.AddReference('System.Windows.Forms')
# clr.AddReference('System.Threading')
from System.Threading import Thread,ApartmentState,ThreadStart    
import os
from threading import Timer

def run_server():    
    os.system('python -m tfjsa.run silent')

    '''
    stream = os.popen("python -m tfjsa.run")
    temp = stream.readlines()
    output = []
    for l in temp:
        output.append(l.strip())
    print(output)
    '''

    # import subprocess
    # result = subprocess.run(["python", "-m tfjsa.run"])
    # print(result)
    # print(result.returncode)

def show_main():

    if not have_runtime():#没有webview2 runtime
        install_runtime()

    root=Tk()
    root.title('tfjsa desktop app')
    # root.geometry('1200x600+5+5')
   
    frame2=WebView2(root, 1000,600)
    frame2.pack(side='top', padx=0,fill='both',expand=True)
    frame2.load_url('http://localhost:5007')
    
    root.mainloop()

if __name__ == "__main__":

    Timer(0.001, run_server).start()

    t = Thread(ThreadStart(show_main))
    t.ApartmentState = ApartmentState.STA
    t.Start()
    t.Join()