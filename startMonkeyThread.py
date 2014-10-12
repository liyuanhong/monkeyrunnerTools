import os
import threading

class startMonkeyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        cmd = 'monkeyrunner ' + os.getcwd()
        cmd = cmd + '\\GetBitmapThread.py'
        os.system(cmd)
        
