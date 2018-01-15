# DreamScreenCommander
Python script that allows you to locally integrate control your DreamScreen Ambient TV device with other systems.  You don't need your phone anymore to switch outputs!

While this can be used in many ways where you can have a computer call the script and programatically enter options.
My solution was with a Raspberry Pi, a FLIRC, and a Harmony remote.  Got tired of having to whip out my phone just to change a setting when my remote was right there... :)

****For you to do:****

Only ONE thing that you HAVE to do: Please enter you IP address between the "" in the IP constant (it will be in the first line after the comment block).  Example: IP = "192.168.1.2"
Optional changes: change the group number (default is 0)

****How to use the script:****

python <path to this file> <option> <value>
Example: "python dreamscreen.py -m 0" will turn off the dreamscreen

Options can be daisy chained.  E.G, if you have more than one DreamScreen, you can temporarily specify which one to talk to.
Example: "python dreamscreen.py -i 192.168.1.2 -m 0" will turn off that particular dreamscreen

****Limitations:****

    1) I don't have groups so nothing having to do with groups works
    2) right now, everything works based on the values from the docs.  No labeling just yet.  This may never happen as I will be running an external ervice for a UI, so I'll be labeling elsewhere
