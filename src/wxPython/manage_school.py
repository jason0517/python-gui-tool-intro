import wx
import wx.xrc
import wx.grid

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"School Management System", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
        self.m_toolBar1.SetToolBitmapSize( wx.Size( 12,12 ) )
        self.m_tool1 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"images/new_file.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )


        self.m_tool2 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"images/cut.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Remove", u"Remove a row", None )

        self.m_toolBar1.Realize()

        bSizer1.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )

        self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.m_grid1.CreateGrid( 5, 4 )
        self.m_grid1.EnableEditing( True )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.SetColSize( 0, 150 )
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( True )
        self.m_grid1.SetColLabelSize( 30 )
        self.m_grid1.SetColLabelValue( 0, u"Name" )
        self.m_grid1.SetColLabelValue( 1, u"Age" )
        self.m_grid1.SetColLabelValue( 2, u"Gender" )
        self.m_grid1.SetColLabelValue( 3, u"Level" )
        self.m_grid1.SetColLabelValue( 4, wx.EmptyString )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Rows
        self.m_grid1.SetRowSize( 0, 25 )
        self.m_grid1.EnableDragRowSize( True )
        self.m_grid1.SetRowLabelSize( 50 )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer1.Add( self.m_grid1, 1, wx.TOP|wx.BOTTOM|wx.EXPAND, 5 )

        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_TOOL, self.on_new_clicked, id = self.m_tool1.GetId() )
        self.Bind( wx.EVT_TOOL, self.one_remove_clicked, id = self.m_tool2.GetId() )

    def __del__( self ):
        pass

    def add_new_row(self, row):
        self.m_grid1.AppendRows()
        r_count = self.m_grid1.GetNumberRows()
        for i in range(len(row)):
            self.m_grid1.SetCellValue(r_count-1, i, row[i])

    def on_new_clicked( self, event ):
        self.newWin = MyDialog1(self)
        self.newWin.ShowWindowModal()

    def one_remove_clicked( self, event ):
        s= self.m_grid1.GetSelectedRows()
        s.sort()
        print s
        self.m_grid1.DeleteRows(s[0], len(s))


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add a New Student", pos = wx.DefaultPosition, size = wx.Size( 329,249 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.HORIZONTAL )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        fgSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl1.SetMinSize( wx.Size( 200,30 ) )

        fgSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Age:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl2.SetMinSize( wx.Size( 200,30 ) )

        fgSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Gender:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl3.SetMinSize( wx.Size( 200,30 ) )

        fgSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_textCtrl4.SetMinSize( wx.Size( 200,30 ) )

        fgSizer1.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

        bSizer3.Add((0, 0),1, wx.EXPAND)

        bSizer3.Add( fgSizer1, 0, wx.EXPAND, 5 )

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1Save = wx.Button( self, wx.ID_SAVE )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Save )
        self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
        m_sdbSizer1.Realize();

        bSizer3.Add( m_sdbSizer1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        bSizer3.Add( (0,0), 1, wx.EXPAND)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.on_cancel_clicked)
        self.m_sdbSizer1Save.Bind( wx.EVT_BUTTON, self.on_save_clicked)

        self.parentWin = parent

    def __del__( self ):
        pass

    def on_save_clicked( self, event ):
        n = [self.m_textCtrl1.GetValue(),
             self.m_textCtrl2.GetValue(),
             self.m_textCtrl3.GetValue(),
             self.m_textCtrl4.GetValue()]

        self.parentWin.add_new_row(n)
        self.Hide()

        self.m_textCtrl1.SetValue("")
        self.m_textCtrl2.SetValue("")
        self.m_textCtrl3.SetValue("")
        self.m_textCtrl4.SetValue("")

    def on_cancel_clicked( self, event ):
        self.Destroy()



###########################################################################
## Main
###########################################################################
if __name__ == '__main__':

    # Next, create an application object.
    app = wx.App()

    # Then a frame.
    frm = MyFrame1(None)

    g_data =[
        ["Name", "Age", "Gender", "Grade"],
        ["Fred", 16, "Male", "G11"],
        ["Tina", 15, "Female", "G12"],
        ["Clive", 18, "Male", "G10"],
        ["Betty", 20, "Female", "G12"]
    ]

    for i in range(len(g_data)):
        for j in range(len(g_data[i])):
            frm.m_grid1.SetCellValue(i, j, str(g_data[i][j]))

    frm.Show()

    # Start the event loop.
    app.MainLoop()
