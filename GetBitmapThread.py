#coding: utf-8

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import threading
import os
import time

class GetBitmapThread(threading.Thread):
    
    def __init__(self):
        self.temFile = 'temFile.png'
        #0表示结束线程，1表示循环运行线程
        self.ctrl = 0
        print 'start monkeyrunner'
        try:
            self.device = MonkeyRunner.waitForConnection()
            self.path = 'D:\\screenshot\\'
            self.filename = 'monkeyPic'
            if os.path.exists(self.path):
                print 'path is exit'
            else:
                print'creat the path'
                os.makedirs('D:\\screenshot\\')
        except:
            print 'fail to connect the androidPhone'
            print '请点击中断连接，结束不必要的线程！'.decode('UTF-8')


    def run(self):
        self.ctrl = 1
        while self.ctrl == 1:
            self.file = open('D:\\screenshot\\ctrl.txt','w')
            self.file.write('0')
            print '0'
            self.file.close()
            self.result = self.device.takeSnapshot()
            self.result.writeToFile (self.path + self.filename + '.png', 'png')
            self.file = open('D:\\screenshot\\ctrl.txt','w')
            self.file.write('1')
            self.file.close()
            print '1'
            print 'thread is running'
            time.sleep(0.15)

    def closeThread(self):
        self.ctrl = 0

GetBitmapThread().run()
