import wx
from MyProject1MyFrame1 import MyProject1MyFrame1
 
if __name__ == '__main__':
    app = wx.App()
    frame = MyProject1MyFrame1(None)
    frame.Show()
    app.MainLoop()