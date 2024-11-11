# use "py" - - pip install flask opencv-python
# py -m pip install <package>   -- this is the only command that works!!

'''
To convert an MP4 file to an RTSP stream using Python and Flask, you can utilize GStreamer and Flask. Here's a basic approach:
Install Dependencies: Ensure you have GStreamer and Flask installed. You might also need pygobject for GStreamer bindings.
GStreamer Setup: Use GStreamer to create an RTSP server. The following code provides a basic setup:

'''

import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GLib

Gst.init(None)

class TestRtspMediaFactory(GstRtspServer.RTSPMediaFactory):
    def do_create_element(self, url):
        pipeline = "filesrc location=/path/to/video.mp4 ! decodebin ! x264enc ! rtph264pay name=pay0 pt=96"
        return Gst.parse_launch(pipeline)

class GstServer:
    def __init__(self):
        self.server = GstRtspServer.RTSPServer()
        factory = TestRtspMediaFactory()
        factory.set_shared(True)
        self.server.get_mount_points().add_factory("/test", factory)
        self.server.attach(None)

if __name__ == '__main__':
    server = GstServer()
    loop = GLib.MainLoop()
    loop.run()

   