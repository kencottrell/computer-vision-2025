Test Code to 
-----------------
1. collect events via REST from Aira (camera events) and Situm (mobile phone accelerometer tracking) and send to Xano
2. use OpenCV neural nets to perform things like face recognition, object detection, object tracking
3. use of OpenCV and other Python libs to create an IP Camera simulator that reads mp4 and image files to act like a hard ware ip camera feed into Aira and OpenCV neural nets

Notes to use
-----------------
This python code uses a self signed cert which is not recognized by Aira REST interface. Added verify=False to each REST call but for any non-test use cases these here are some steps recommended by Perplexity.ai to get a trusted cert, for reference: 

https://www.perplexity.ai/search/caused-by-sslerror-sslcertveri-SAkx.H57SAmZiLFKCylb3A

3. To install Python libs on Windows, use of "py" instead of other install tools. for example
command to use to install :
    -------------------
    py -m pip install <package>   -- this is the only command that works!!
    --------------------------------
on the web saw this: "Why can I use py but not Python?
    ----------------------------------
    "...py is itself located in C:\Windows (which is always part of the PATH ), '
    which is why you find it.  When you installed Python, you didn't check the box to add it to your PATH , which is why it isn't there. In general, it's best to use the Windows Python Launcher, py.exe anyway,  so this is no big deal... "


