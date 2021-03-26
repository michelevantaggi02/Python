import wx
from wx import *

class bg(wx.Frame):
    def __init__(self, parent):
        super(wx.Frame, self).__init__(None, wx.ID_ANY, "Ciao Mondo!")
        super(wx.Frame, self).SetBackgroundStyle(wx.BG_STYLE_TRANSPARENT)
app = wx.App(False)
frame = bg(app)

app.MainLoop()