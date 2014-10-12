#coding: utf-8
import threading
import shutil
import os
import time

class ManuShotThread(threading.Thread):
    def __init__(self,shotpath,filename):
        threading.Thread.__init__(self)
        self.shotpath = shotpath
        print self.shotpath
        self.filename = filename
        self.sourcefile = 'D:\\screenshot\\monkeyPic.png'

    def run(self):
        self.state = 0
        temp = 0
        while(self.state == 0):
            print 'run'
            temp = temp + 1
            time.sleep(0.01)
            try:
                self.file = self.file = open('D:\\screenshot\\ctrl.txt','r')
                self.state = int(self.file.read())
                self.file.close()
            except:
                print 'ctrl file is empty'
            if temp > 10:
                print 'hahahaha'
                self.state = 1
                print '------' + str(self.state)
        self.targetfile = self.shotpath + self.filename
        self.copyfile()

    def copyfile(self):
        print 'copy'
        if os.path.exists(self.shotpath):
            if os.path.exists(self.targetfile):
                print 'file exit'
                temp = 0
                self.targetfile = self.shotpath + self.filename[:len(self.filename) - 4] + str(temp) + '.png'
                print self.targetfile
                while(os.path.exists(self.targetfile)):
                    temp = temp + 1
                    self.targetfile = self.shotpath + self.filename[:len(self.filename) - 4] + str(temp) + '.png'
                    print self.targetfile
                shutil.copy(self.sourcefile,self.targetfile)
            else:
                print 'file not exit'
                shutil.copy(self.sourcefile,self.targetfile)
        else:
            os.makedirs(self.shotpath)
            if os.path.exists(self.targetfile):
                temp = 0
                self.targetfile = self.shotpath + self.filename[:len(self.filename) - 4] + str(temp) + '.png'
                while(os.path.exists(self.targetfile)):
                    temp = temp + 1
                    self.targetfile = self.shotpath + self.filename[:len(self.filename) - 4] + str(temp) + '.png'
                shutil.copy(self.sourcefile,self.targetfile)
            else:
                shutil.copy(self.sourcefile,self.targetfile)
                    
                
        
