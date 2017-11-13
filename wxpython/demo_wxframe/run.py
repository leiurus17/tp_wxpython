import wx

#import the newly created GUI file
import frame_source

app = wx.App()
frame = frame_source.window
frame.Show(True)
#start the application
app.MainLoop()