# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"wxFrame Demo", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.MAXIMIZE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow( self )
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
        
        self.m_statusBar2 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_menu1 = wx.Menu()
        self.m_menubar1.Append( self.m_menu1, u"File" ) 
        
        self.m_menu2 = wx.Menu()
        self.m_menubar1.Append( self.m_menu2, u"Edit" ) 
        
        self.m_menu3 = wx.Menu()
        self.m_menubar1.Append( self.m_menu3, u"View" ) 
        
        self.m_menu4 = wx.Menu()
        self.m_menubar1.Append( self.m_menu4, u"Tools" ) 
        
        self.m_menu5 = wx.Menu()
        self.m_menubar1.Append( self.m_menu5, u"Help" ) 
        
        self.SetMenuBar( self.m_menubar1 )
        
        self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_mgr.AddPane( self.m_panel, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Hide().Float().FloatingPosition( wx.Point( 471,358 ) ).Resizable().FloatingSize( wx.Size( 214,121 ) ) )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_button3 = wx.Button( self.m_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )
        
        
        self.m_panel.SetSizer( bSizer2 )
        self.m_panel.Layout()
        bSizer2.Fit( self.m_panel )
        
        self.m_mgr.Update()
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        self.m_mgr.UnInit()
        
    

