# -*- coding:utf-8 -*-

# First things, first. Import the wxPython package.
import wx

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")
frm.SetBackgroundColour((255, 255, 255))
bSizer3 = wx.BoxSizer( wx.VERTICAL )
m_staticText1 = wx.StaticText(frm, wx.ID_ANY, u"Hello,World", wx.DefaultPosition, wx.DefaultSize, 0 )
font =wx.Font(18, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString )
m_staticText1.SetFont(font)

hSizer = wx.BoxSizer(wx.HORIZONTAL)
hSizer.Add(m_staticText1, 0, wx.CENTER)

bSizer3.Add((0, 0), 1, wx.EXPAND)
bSizer3.Add(hSizer, 0, wx.CENTER)
bSizer3.Add((0, 0), 1, wx.EXPAND)

frm.SetSizer(bSizer3)

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
