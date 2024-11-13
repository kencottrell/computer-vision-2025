Test Code for Demos
-----------------
1. collect events via REST from Aira (camera events) and Situm (mobile phone accelerometer tracking) and send to Xano
2. use OpenCV neural nets to perform things like face recognition, object detection, object tracking
3. use of OpenCV and other Python libs to create an IP Camera simulator that reads mp4 and image files to act like a hard ware ip camera feed into Aira and OpenCV neural nets

------------------------------
Notes to use unsigned cert in your VSCode Python code
------------------------
This python code uses a self signed cert which is not recognized by Aira REST interface. Added verify=False to each REST call but for any non-test use cases these here are some steps recommended by Perplexity.ai to get a trusted cert, for reference: 

    https://www.perplexity.ai/search/caused-by-sslerror-sslcertveri-SAkx.H57SAmZiLFKCylb3A

----------------------------
To install Python libs on VSCode Windows, use of "py" instead of other install tools. for example
command to use to install :
    -------------------
    py -m pip install <package>   -- this is the only command that works!!
    --------------------------------
on the web saw this: "Why can I use py but not Python?
    ----------------------------------
    "...py is itself located in C:\Windows (which is always part of the PATH ), '
    which is why you find it.  When you installed Python, you didn't check the box to add it to your PATH , which is why it isn't there. In general, it's best to use the Windows Python Launcher, py.exe anyway,  so this is no big deal... "

-------------------
1. use of Aira in VM guest
----------------
To allow guest VMware access through Windows Firewall, follow these steps:
    Open Windows Firewall Settings: Use the wf.msc command to access the firewall settings.
    
    Enable ICMP Requests: Run the command netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes to allow ping requests (ICMPv4-In)2.
    
    Check Network Configuration: Ensure the VM is using a bridged network connection, which places it on the same network as the host2.

    Adjust Firewall Rules: If necessary, manually configure firewall rules to allow specific ports used by your VMware setup7.

    Verify Connectivity: Test connectivity by pinging between host and guest VMs.

1. add FFMPeg to Python path
-------------------------------
To add the Python path for FFmpeg, you have a few options:

    Place FFmpeg in the same directory as your Python script: The simplest solution is to place the ffmpeg.exe file in the same folder as your Python script1. This allows Python to find FFmpeg without modifying any system paths.
    
    Add FFmpeg to your system PATH: You can add the directory containing ffmpeg.exe to your system's PATH environment variable3. Here's how:
            Open the Start menu and search for "Environment Variables"
            Click "Edit the system environment variables"
            Click the "Environment Variables" button
            Under "System Variables", find and select the "Path" variable, then click "Edit"
            Click "New" and add the full path to the directory containing ffmpeg.exe (e.g., C:\ffmpeg\bin)
            Click "OK" to save the changes
            Restart any open command prompts for the changes to take effect

    Specify the FFmpeg path in your Python script: You can explicitly set the path to FFmpeg in your Python code2:

        import ffmpeg
        ffmpeg.FFMPEG_BINARY = r"C:\path\to\ffmpeg.exe"

            Replace "C:\path\to\ffmpeg.exe" with the actual path to your ffmpeg.exe file.

    Use the ffmpeg-python library: If you're using the ffmpeg-python library, you can install it using pip5:

        pip install ffmpeg-python

        (This library provides a Python wrapper for FFmpeg, making it easier to use FFmpeg functionality in your Python scripts.)

After implementing one of these solutions, you should be able to use FFmpeg in your Python scripts without encountering "FileNotFoundError" issues. Remember to restart your Python environment or IDE after making changes to ensure they take effect.

