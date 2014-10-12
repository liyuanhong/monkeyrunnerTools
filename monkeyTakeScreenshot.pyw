#coding: utf-8
import wx
import string
import IndentationClass
import GetPicThread
import startMonkeyThread
import os
import signal
import ManuShotThread
import time
import AutoShotThread


class MonkeyWindow:
    def __init__(self):
        self.indent = IndentationClass.IndentationClass()
        self.printStart('__init__')
        #截取方式控制变量，0表示手动，1表示自动
        self.shotWay = 0
        #自动截图的数量默认为6张
        self.shotNum = 6
        #自动截取的时间间隔默认为10分钟
        self.shotTimeInterval = 10
        #刷新率默认为0.05秒每次
        self.freshRate = 0.05
        #线程数默认为1个
        self.threadNum = 1
        #截图保存路劲
        self.screenshot = 'D:\\screenshot\\'
        self.filename = 'screenshot.png'
        #定义一个list用来保存启动的线程
        self.threadList = []
        
        self.printEnd('__init__')    

    def mainFrame(self):
        self.printStart('mainFrame')                  

        #控件
        tempSize = wx.Size(750,735)
        self.frame = wx.Frame(None,wx.ID_ANY, 'simple.py',size=tempSize)
        panel = wx.Panel(self.frame,wx.ID_ANY)
        self.imageShower = wx.Panel(panel,wx.ID_ANY,style=wx.BORDER_DOUBLE)        
        label1 = wx.StaticText(panel,wx.ID_ANY,'手机屏幕：'.decode('utf-8'))
        label2 = wx.StaticText(panel,wx.ID_ANY,'截图保存路径：'.decode('utf-8'))
        self.pathText = wx.TextCtrl(panel,wx.ID_ANY,'D:\\screenshot'.decode('utf-8'),size = wx.Size(250,25))
        pathButton = wx.Button(panel,wx.ID_ANY,'选择路径'.decode('utf-8'),size = wx.Size(75,25))
        shotPanel = wx.Panel(panel,wx.ID_ANY,size = wx.Size(328,350),style=wx.BORDER_SIMPLE)
        connetPanel = wx.Panel(panel,wx.ID_ANY,size = wx.Size(328,220),style=wx.BORDER_SIMPLE)

        self.manualRadio = wx.RadioButton(shotPanel,wx.ID_ANY,'手动截图'.decode('utf-8'),style = wx.RB_GROUP,pos = wx.Point(10,20))
        self.autoRadio = wx.RadioButton(shotPanel,wx.ID_ANY,'自动截图'.decode('utf-8'),pos = wx.Point(120,20))
        self.shotButton = wx.Button(shotPanel,wx.ID_ANY,'截取'.decode('utf-8'),pos = wx.Point(10,70))
        line = wx.StaticLine(shotPanel,wx.ID_ANY,pos = wx.Point(10,110),size = wx.Size(308,2))

        label3 = wx.StaticText(shotPanel,wx.ID_ANY,'时间间隔：'.decode('utf-8'),pos = wx.Point(10,135))
        self.textField1 = wx.TextCtrl(shotPanel,wx.ID_ANY,'10'.decode('utf-8'),size = wx.Size(100,25),pos = wx.Point(85,135))
        label4 = wx.StaticText(shotPanel,wx.ID_ANY,'分钟'.decode('utf-8'),pos = wx.Point(190,135))
        self.textField1.SetEditable(False)

        label5 = wx.StaticText(shotPanel,wx.ID_ANY,'数量：'.decode('utf-8'),pos = wx.Point(10,180))
        self.textField2 = wx.TextCtrl(shotPanel,wx.ID_ANY,'6'.decode('utf-8'),size = wx.Size(100,25),pos = wx.Point(85,180))
        label6 = wx.StaticText(shotPanel,wx.ID_ANY,'张'.decode('utf-8'),pos = wx.Point(190,180))
        self.startButton = wx.Button(shotPanel,wx.ID_ANY,'开始'.decode('utf-8'),pos = wx.Point(10,230))
        self.textField2.SetEditable(False)
        self.startButton.Enable(False)

        label7 = wx.StaticText(connetPanel,wx.ID_ANY,'刷新率：'.decode('utf-8'),pos = wx.Point(10,20))
        self.textField3 = wx.TextCtrl(connetPanel,wx.ID_ANY,'0.05'.decode('utf-8'),size = wx.Size(100,25),pos = wx.Point(85,20))
        label8 = wx.StaticText(connetPanel,wx.ID_ANY,'秒/次'.decode('utf-8'),pos = wx.Point(190,20))

        label9 = wx.StaticText(connetPanel,wx.ID_ANY,'线程数：'.decode('utf-8'),pos = wx.Point(10,70))
        self.textField4 = wx.TextCtrl(connetPanel,wx.ID_ANY,'1'.decode('utf-8'),size = wx.Size(100,25),pos = wx.Point(85,70))
        label10 = wx.StaticText(connetPanel,wx.ID_ANY,'个'.decode('utf-8'),pos = wx.Point(190,70))
        
        self.connectButton = wx.Button(connetPanel,wx.ID_ANY,'连接手机'.decode('utf-8'),pos = wx.Point(10,120))
        self.disconnectButton = wx.Button(connetPanel,wx.ID_ANY,'中断连接'.decode('utf-8'),pos = wx.Point(190,120))

        
        #位图
        self.img = wx.Image('阳光小秒拍.png'.decode('utf-8'),wx.BITMAP_TYPE_PNG,-1)

        #控件设置
        self.frame.Center()        
        font = label1.GetFont()
        self.pathText.SetEditable(False)
        font.SetPointSize(10)
        label1.SetFont(font)
        label2.SetFont(font)

        self.height = self.img.GetHeight()
        self.width = self.img.GetWidth()
        self.img.Rescale(self.width/2,self.height/2)
        self.bitmap = self.img.ConvertToBitmap()               
        self.imageShower.SetAutoLayout(True)

        #布局
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer = wx.BoxSizer(wx.VERTICAL)
        screenSizer = wx.BoxSizer(wx.HORIZONTAL )
        selectPathSizer = wx.BoxSizer(wx.VERTICAL)
        selectPathSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        panel.SetSizer(sizer)        
        boxSizer.Add(label1, flag=wx.LEFT | wx.TOP , border=15)
        boxSizer.Add(self.imageShower, flag=wx.LEFT | wx.BOTTOM | wx.RIGHT,border=15)
        selectPathSizer.Add(label2)
        selectPathSizer2.Add(self.pathText)
        selectPathSizer2.Add(pathButton,flag=wx.LEFT,border = 5)
        selectPathSizer.Add(selectPathSizer2,flag=wx.TOP,border = 5)
        selectPathSizer.Add(shotPanel,flag=wx.TOP,border = 10)
        selectPathSizer.Add(connetPanel,flag=wx.TOP,border = 10)
        screenSizer.Add(boxSizer)        
        sizer.Add(boxSizer)
        sizer.Add(selectPathSizer,flag=wx.ALIGN_LEFT|wx.TOP, border=35)       
        self.backgroundImage=wx.StaticBitmap(self.imageShower,wx.ID_ANY,self.bitmap)

        #绑定事件
        self.frame.Bind(wx.EVT_BUTTON,self.startConnect,self.connectButton)
        self.frame.Bind(wx.EVT_BUTTON,self.endConnect,self.disconnectButton)
        self.frame.Bind(wx.EVT_BUTTON,self.selectPath,pathButton)
        self.frame.Bind(wx.EVT_BUTTON,self.getScreenshot,self.shotButton)
        self.frame.Bind(wx.EVT_BUTTON,self.autoScreenshot,self.startButton)
        self.manualRadio.Bind(wx.EVT_RADIOBUTTON,self.shotWayCtrl)
        self.autoRadio.Bind(wx.EVT_RADIOBUTTON, self.shotWayCtrl)
        
        
        
        self.frame.Show()
        self.printEnd('mainFrame')

    def showWindow(self):
        self.printStart('showWindow')
        app = wx.App()
        self.mainFrame()
        app.MainLoop()
        self.printEnd('showWindow')

    #连接手机并开始屏幕的同步显示
    def startConnect(self,arg):
        #通过judge判断设置是否连接，如果连接着就会返回一个3个元素的数组，没有则返回2个元素的数组
        judge = os.popen('adb devices').readlines()
        if len(judge) == 3:
            self.connectButton.Enable(False)
            self.freshRate = float(self.textField3.GetValue())
            try:
                self.threadNum = int(self.textField4.GetValue())
                if self.threadNum <= 0:
                    dialog = wx.MessageDialog(self.frame,'必须填写大于0的整数！'.decode('UTF-8'),'消息'.decode('UTF-8'),wx.OK_DEFAULT)
                    dialog.ShowModal()
                else:
                    pass
            except:
                dialog = wx.MessageDialog(self.frame,'必须填写大于0的整数！'.decode('UTF-8'),'消息'.decode('UTF-8'),wx.OK_DEFAULT)
                dialog.ShowModal()
            path = 'D:\\screenshot\\'
            filename = 'monkeyPic'
            if os.path.exists(path):
                print 'path is exit'
            else:
                print'creat the path'
                os.makedirs('D:\\screenshot\\')
            file = open('D:\\screenshot\\ctrl.txt','w')
            file.write('0')
            file.close()
            self.monkeyrunnerThread = startMonkeyThread.startMonkeyThread()
            self.monkeyrunnerThread.start()
            print self.monkeyrunnerThread.ident
            for i in range(0,self.threadNum):
                self.connectThread = GetPicThread.GetPicThread(self.img,self.height,self.width,self.bitmap,self.backgroundImage,self.imageShower,self.freshRate)
                self.connectThread.start()
                self.threadList.append(self.connectThread)
                print 'start thread : ' + str(self.connectThread.ident)
            for j in range(0,len(self.threadList)):
                print str(self.threadList[j].ident)
        else:
            dialog = wx.MessageDialog(self.frame,'请连接你的android手机！'.decode('UTF-8'),'消息'.decode('UTF-8'),wx.OK_DEFAULT)
            dialog.ShowModal()
        
        
    #断开与手机的连接，并结束相关线程
    def endConnect(self,arg):
        self.connectButton.Enable(True)
        cmd = 'getProId'
        os.system(cmd)
        for j in range(0,len(self.threadList)):
            self.threadList[j].stop()
            print 'stop thread : ' + str(self.threadList[j].ident)
        self.threadList = []

    #手动截图
    def getScreenshot(self,arg):
        manuShotThread = ManuShotThread.ManuShotThread(self.screenshot,self.filename)
        manuShotThread.start()

    #自动获取屏幕截图
    def autoScreenshot(self,arg):
        try:
            self.shotTimeInterval = float(self.textField1.GetValue())
            self.shotNum = float(self.textField2.GetValue())
        except:
            print 'autoScreenShot get an exception'
        autoShotThread = AutoShotThread.AutoShotThread(self.screenshot,self.filename,self.shotTimeInterval,self.shotNum)
        autoShotThread.start()

    #设置截取屏幕的方式
    def shotWayCtrl(self,arg):
        if arg.GetId() == self.manualRadio.GetId():
            self.shotWay = 0
            self.shotButton.Enable(True)
            self.textField2.SetEditable(False)
            self.startButton.Enable(False)
            self.textField1.SetEditable(False)
        elif arg.GetId() == self.autoRadio.GetId():
            self.shotWay = 1
            self.textField2.SetEditable(True)
            self.startButton.Enable(True)
            self.textField1.SetEditable(True)
            self.shotButton.Enable(False)

    def printStart(self,txt):
        self.indent.appentBlank()
        print self.indent.getBlank() + 'start' + txt + '() method'
        
    def printEnd(self,txt):
        print self.indent.getBlank() + 'end' + txt + '() method'
        self.indent.delBlank()

    #选择截图存储路径
    def selectPath(self,arg):
        self.openDialog =  wx.DirDialog(self.frame,'打开'.decode('UTF-8'),'.',style = wx.DD_DEFAULT_STYLE)
        temp = self.openDialog.ShowModal()
        self.filePath = self.openDialog.GetPath()
        if (temp == wx.ID_OK):
            if self.filePath != '':
                self.pathText.Clear()
                self.pathText.WriteText(self.filePath)
                self.screenshot = self.filePath + '\\'
                print self.screenshot
        
            
    
MonkeyWindow().showWindow()




