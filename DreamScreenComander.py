#############################################################################
## DreamScreen Commander
## By Taurean Dyer 
## www.taureandyer.com
## v 1.02
## Based on example code from Dreamscreen SDK Docs and inspired by avwuff's DreamScreenControl.cs 
## (use avwff's if you just want a C# app: https://github.com/avwuff/DreamScreenControl)

import socket
import sys
import optparse
import time

##TODO
# Save IP address to a file and read from file.  For now, just hard code it
# Add colors chart and the ability to read from chart and put it in there.  Maybe have dec, hex, and human readible options
# Add better help text for some modes


#####Edit these values as needed###############################################
#IP and group number here (see readme).  Touch anything else at your own risk!
IP = "<enter IP here>" ##Put your IP address here
group = 0              ##Optional change only if you have group numbers assigned
#####End Editabe Values########################################################

### NO TOUCHIE FROM HERE DOWN!!!!##############################################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # INTERNET, UDP datagram
PORT = 8888
endpoint = (IP, PORT)
crcTable = [0, 7, 4, 9, 28, 27, 18, 21, 56, 63, 54, 49, 36, 35, 42, 45, 112, 119, 126, 121, 108, 107, 98, 101, 72, 79, 70, 65, 84, 83, 90, 93, 224, 231, 238, 233, 252, 251, 242, 245, 216, 223, 214, 209, 196, 195, 202, 205, 144, 151, 158, 153, 140, 139, 130, 133, 168, 175, 166, 161, 180, 179, 186, 189, 199, 192, 201, 206, 219, 220, 213, 210, 255, 248, 241, 246, 227, 228, 237, 234, 183, 176, 185, 190, 171, 172, 165, 162, 143, 136, 129, 134, 147, 148, 157, 154, 39, 32, 41, 46, 59, 60, 53, 50, 31, 24, 17, 22, 3, 4, 13, 10, 87, 80, 89, 94, 75, 76, 69, 66, 111, 104, 97, 102, 115, 116, 125, 122, 137, 142, 135, 0, 149, 146, 155, 156, 177, 182, 191, 184, 173, 170, 163, 164, 249, 254, 247, 240, 229, 226, 235, 236, 193, 198, 207, 200, 221, 218, 211, 212, 105, 110, 103, 96, 117, 114, 123, 124, 81, 86, 95, 88, 77, 74, 67, 68, 25, 30, 23, 16, 5, 2, 11, 12, 33, 38, 47, 40, 61, 58, 51, 52, 78, 73, 64, 71, 82, 85, 92, 91, 118, 113, 120, 255, 106, 109, 100, 99, 62, 57, 48, 55, 34, 37, 44, 43, 6, 1, 8, 15, 26, 29, 20, 19, 174, 169, 160, 167, 178, 181, 188, 187, 150, 145, 152, 159, 138, 141, 132, 131, 222, 217, 208, 215, 194, 197, 204, 203, 230, 225, 232, 239, 250, 253, 244, 243]

#### Functions
#### prototyping area (don't except to work)###################################

#def initialSetup(ip, group):
#   coming....maybe

def setIP(ip): #temporary as every time you run the code, it will default back to the hard coded one
    ##check IP
    IP= ip
    endpoint = (ip, PORT)

def color(color): ##!!!!!Not working yet!!!!!!
    payload=[1]
    buildAndSendPacket(3,8, 1) #set to ambient scene mode
    ## decide whether to look up or split
    ##split
    payload = color.split(',')
    for i in range(len(payload)):
        payload[i] = int(payload[i])
    buildAndSendPacket(3,13, payload) #set scene
####End prototyping area#########################################################

    
#### Things get real from here

def setAmbience(ambience):
    payload=[ambience]
    buildAndSendPacket(3,8, payload)
    
def setScene(scene): #this one is finicky at times.  Need feedback
    ##0x00 - Random Color
    ##0x01 - Fireside
    ##0x02 - Twinkle
    ##0x03 - Ocean
    ##0x04 - Rainbow
    ##0x05 - July 4th
    ##0x06 - Holiday
    ##0x07 - Pop
    ##0x08 - Enchanted Forest
    
    #setMode(3) #set mode to Ambient ###  sometmes it works without this.  Will need feedback from others...
    setAmbience(1)#set to ambient scene mode
    time.sleep(2) #delay to let previous packets get sent correctly.  Sometimes errored out with unexpected behavior...
    payload=[scene]
    buildAndSendPacket(3,13, payload) #set scene
    
def setMode(mode):
    ##0 - Sleep
    ##1 - Video
    ##2 - Music
    ##3 - Ambient

    payload=[mode]
    buildAndSendPacket(3,1, payload)
    
def setSource(source):
    # 0- input 1
    # 1- input 2
    # 2- input 3
    payload=[source]
    buildAndSendPacket(3,32, payload)

def setBrightness(brightness):
    payload=[brightness]
    buildAndSendPacket(3,2, payload)

def buildAndSendPacket(upperC, lowerC, payload):
    resp=[] #starts the response object
    resp.append(252) #0xFC
    resp.append(len(payload) + 5)
    resp.append(group) 
    resp.append(17)
    resp.append(upperC)
    resp.append(lowerC)
    for i in range(0,len(payload)): #for loop to handle colors.  I know that there are cleaner ways to write it, but I like controlling my iterators.
        resp.append(payload[i])
    crc = calcCRC8(resp) #calc the crc
    resp.append(crc)
    resp = bytearray(resp) #forms response object into a byte to be sent out
    sock.sendto(resp, endpoint)

def calcCRC8(resp):
    size = resp[1] + 1
    crc = 0
    for i in range(0,size):
        crc = crcTable[(resp[i] ^ crc) & 255]
        #print crc #just in for verification
    return crc

###OPTION HANDLING#####################################################
scenes = "Which scenes (use the number)?"\
         "\n0 - Random Color"\
         "\n1 - Fireside"\
         "\n2 - Twinkle"\
         "\n3 - Ocean"\
         "\n4 - Rainbow"\
         "\n5 - July 4th"\
         "\n6 - Holiday"\
         "\n7 - Pop"\
         "\n8 - Enchanted Forest"

modes = "Which mode? (use the number)"\
        "\n0 - Sleep"\
        "\n1 - Video"\
        "\n2 - Music"\
        "\n3 - Ambient"

sources = "Which mode? (use the number)"\
        "\n0 - input 1"\
        "\n1 - input 2"\
        "\n2 - input 3"

parser = optparse.OptionParser()
parser.add_option('-m', '--mode', dest='mode', help=modes)
parser.add_option('-s', '--source', dest='source', help=sources)
parser.add_option('-a', '--ambient scene', dest='scene', help=scenes)
parser.add_option('-b', '--brightness', dest='brightness', help="Enter from 0-100 to control brightness")
parser.add_option('-i', '--ip', dest='ip', help="Please enter your Dreamscreen's IP address")
##parser.add_option('-c', '--color', dest='color', help='Which color?') ##coming soon
options, args = parser.parse_args()
if options.ip:
    try:
        ##check IP's validity
        payload = ip.split('.')
        if len(payload) == 3:
            for i in range(len(payload)): ## check if all ip is valid numerically (you can add in more octets)
                int(payload[i])
            #do we need to ping the IP as well?  Probably not...maybe we can ask a set of questions for setup?
            endpoint(ip, PORT)
        else:
            print "This has an error in your IP's length"
    except:
        print "This has an error in your IP"
if options.mode:
    try:
        options.mode = int(options.mode) #options come in as strings, must cast as int
        #Data forming for integer edge cases
        if options.mode > 3:
            options.mode = 3
        elif options.mode < 0:
            options.mode = 0
        setMode(options.mode)
    except:
        print "error: mode not a number"
        sys.exit(0)

if options.source:
    try:
        options.source = int(options.source) #options come in as strings, must cast as int
        if options.source > 2:
                options.source = 2
        elif options.source < 0:
                options.source = 0
        setSource(options.source)
    except:
        print "error: source not a number"
        sys.exit(0)

if options.scene:
    try:
        options.scene = int(options.scene) #options come in as strings, must cast as int
        if options.scene > 8:
                options.scene = 8
        elif options.scene < 0:
                options.scene = 0
        setScene(options.scene)
    except:
        print "error: source not a number"
        sys.exit(0)

if options.brightness:
    try:
        options.brightness = int(options.brightness) #options come in as strings, must cast as int
        if options.brightness > 100:
                options.brightness = 100
        elif options.brightness < 0:
                options.brightness = 0
        setBrightness(options.brightness)
    except:
        print "error: source not a number"
        sys.exit(0)
        
if (options.mode is None) and (options.source is None) and (options.scene is None) and (options.ip is None) and (options.brightness is None):
    print "error: no options were selected"
    sys.exit(0)
