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
        
    

