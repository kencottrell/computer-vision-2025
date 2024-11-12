#!/usr/bin/env python
'''

Go to https://www.msys2.org/ and download the x86_64 installer

Follow the instructions on the page for setting up the basic environment

Run C:\msys64\ucrt64.exe - a terminal window should pop up

Execute pacman -Suy

Execute pacman -S mingw-w64-ucrt-x86_64-gtk4 mingw-w64-ucrt-x86_64-python3 mingw-w64-ucrt-x86_64-python3-gobject

To test that GTK is working you can run gtk4-demo

Copy the hello.py script you created to C:\msys64\home\<username>

In the mingw32 terminal execute python3 hello.py - a window should appear.

Note that

this code will expose RTSP stream named stream1 on default port 8554
I used qtdemux to get video from MP4 container. You could extend above pipeline to extract audio too (and expose it too via RTSP server)
to decrease CPU processing you can only extract video without decoding it and encoding it again to H264. However, if transcoding is needed, I left one commented line that will do the job (but it might choke less powerful CPUs).
You can play this with VLC

vlc -v rtsp://127.0.0.1:8554/stream1
or with Gstreamer

gst-launch-1.0 playbin uri=rtsp://127.0.0.1:8554/stream1

'''


import sys
import gi

gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GObject, GLib

loop = GLib.MainLoop()
Gst.init(None)

class TestRtspMediaFactory(GstRtspServer.RTSPMediaFactory):
    def __init__(self):
        GstRtspServer.RTSPMediaFactory.__init__(self)

    def do_create_element(self, url):
        #set mp4 file path to filesrc's location property
        src_demux = "filesrc location=/path/to/dir/test.mp4 ! qtdemux name=demux"
        h264_transcode = "demux.video_0"
        #uncomment following line if video transcoding is necessary
        #h264_transcode = "demux.video_0 ! decodebin ! queue ! x264enc"
        pipeline = "{0} {1} ! queue ! rtph264pay name=pay0 config-interval=1 pt=96".format(src_demux, h264_transcode)
        print ("Element created: " + pipeline)
        return Gst.parse_launch(pipeline)

class GstreamerRtspServer():
    def __init__(self):
        self.rtspServer = GstRtspServer.RTSPServer()
        factory = TestRtspMediaFactory()
        factory.set_shared(True)
        mountPoints = self.rtspServer.get_mount_points()
        mountPoints.add_factory("/stream1", factory)
        self.rtspServer.attach(None)

if __name__ == '__main__':
    s = GstreamerRtspServer()
    loop.run()