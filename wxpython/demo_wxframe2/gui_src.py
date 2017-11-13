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
        
        
        self.m_mgr.Update()
        self.Centre( wx.BOTH )
    
    def __del__( self ):
        self.m_mgr.UnInit()
        
    

###########################################################################
## Class MyPanel3
###########################################################################

class MyPanel3 ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
        
        self.m_mgr = wx.aui.AuiManager()
        self.m_mgr.SetManagedWindow( self )
        self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
        
        self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_mgr.AddPane( self.m_button1, wx.aui.AuiPaneInfo() .Left() .PinButton( True ).Float().FloatingPosition( wx.Point( 516,403 ) ).Resizable().FloatingSize( wx.Size( 104,65 ) ) )
        
        
        self.m_mgr.Update()
    
    def __del__( self ):
        self.m_mgr.UnInit()
        
    

