import gi
gi.require_version('Gst', '1.0')
gi.require_version('GstRtspServer', '1.0')
from gi.repository import Gst, GstRtspServer, GLib

# Initialize GStreamer
Gst.init(None)

class TestRtspMediaFactory(GstRtspServer.RTSPMediaFactory):
    def do_create_element(self, url):
        pipeline = "filesrc location=/path/to/video.mp4 ! qtdemux ! h264parse ! rtph264pay name=pay0 pt=96"
        return Gst.parse_launch(pipeline)

# Set up RTSP server
server = GstRtspServer.RTSPServer()
factory = TestRtspMediaFactory()
factory.set_shared(True)
server.get_mount_points().add_factory("/test", factory)
server.attach(None)

# Run the main loop
loop = GLib.MainLoop()
loop.run()