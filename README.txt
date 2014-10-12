双击 monkeyTakeScreenshot.pyw 即可运行该程序

注意，运行所需要的环境：
安装了python2.7.6
安装了wxpython
配置好了monkeyrunner的运行时环境
配置好了adb运行环境

其中结束monkeyrunner连接的方法调用了window的系统命令taskkill

adb运行环境主要是用来判断设备是否连接的作用

monkeyrunner与python的通讯采用的是将文件写入磁盘的方法，故性能上有点差
截图实际上是连接手机后截图的复制，因此可能截图不是实时的，要截取正确的截图，需要保持手机的屏幕画面处于短时间的非运动状态

此小工具还存在很多优化的地方，希望大家给出建议

http://blog.csdn.net/lyhdream

https://github.com/liyuanhong?tab=repositories