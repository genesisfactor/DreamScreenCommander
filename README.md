# DreamScreenCommander
**Overview**

Python script that allows you to locally integrate control your DreamScreen Ambient TV device with other systems.

Consider this is a backend service script.  You will need some sort of local front end for yourself, like Openhab, Window Speech Marcos, a Harmony remote control, keyboard marcos, or some event based scripts

While this can be used in many ways where you can have your computer call the script upon events and programatically enter the option values.

My solution will be with a Raspberry Pi, a FLIRC, and a Harmony remote.  Got tired of having to whip out my phone just to change a setting when my remote was right there... :)

This was one of my weekend projects (1/13/18 - 1/14/18).  I hope this helps someone else.  Stay tuned for others!

**For you to do:**

Only ONE thing that you HAVE to do: Please enter you IP address between the "" in the IP constant (it will be in the first line after the comment block).  Example: IP = "192.168.1.2"
Optional changes: change the group number (default is 0)

**How to use the script:**

**python \<path-to-this-file> \<option> \<value>**
For Windows users, it will be **\<path-to-python.exe> \<path-to-this-file> \<option> \<value>**

- Changing Modes:                   **-m \<number>**
- Changing Brightness:              **-b \<number>**
- Changing Sources:                 **-s \<number>**
- Temporarily setting IP address:   **-i \<ip address>**
- Changing Scenes:                  **-a \<number>**
    
**Example: "python dreamscreen.py -m 0"** will turn off the dreamscreen

Options **should** be able to be daisy chained.  E.G, if you have more than one DreamScreen, you can temporarily specify which one to talk to.  This is a feature of the way it was written, and there aren't too many other options to be daisy chained...soooo...take it with a grain of salt?

**Example: "python dreamscreen.py -i 192.168.1.2 -m 0"** **should** turn off that particular dreamscreen (untested as I only have one Dream screen)

**Ideas for usage**

- Automatically adjust Dreamscreen brightness based on room ambient brightness
- Control your Dreamscreen inputs with a Harmony remote control - no phone needed!
- Use Dreamscreen as a light with with your smart home instance and a raspberry pi (full features coming soon)
- Do Voice UI (Alexa-styled) control of the Dreamscreen (Windows Speech Marcos, Jasper)
- Automate with your android phone SL4A and Tasker(the script should work there too as it only imports sys, socket, optparse, and time)

**What works**
- Changing Modes
- Changing Brightness
- Changing Inputs
- Changing Scenes (still debugging)

**Untested by SHOULD work**
- Temporarily setting IP address
- Daisy chaining commands


****Limitations:****

    1) I don't have groups so nothing having to do with groups works
    2) right now, everything works based on the values from the docs.  No labeling just yet.  This may never happen as I will be running an external ervice for a UI, so I'll be labeling elsewhere
    3) Ambient Scenes may need some work
    4) Colors not working yet as I haven't figured out how I want to implement them- which itself may be custom...
    5) Groups does not -and probably will not- work as I don't have groups
