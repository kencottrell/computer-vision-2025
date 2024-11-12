Windows
----

Go to https://www.msys2.org/ and download the x86_64 installer

Follow the instructions on the page for setting up the basic environment

Run C:\msys64\ucrt64.exe - a terminal window should pop up

Execute pacman -Suy

Execute pacman -S mingw-w64-ucrt-x86_64-gtk4 mingw-w64-ucrt-x86_64-python3 mingw-w64-ucrt-x86_64-python3-gobject

To test that GTK is working you can run gtk4-demo

Copy the hello.py script you created to C:\msys64\home\<username>

In the mingw32 terminal execute python3 hello.py - a window should appear.