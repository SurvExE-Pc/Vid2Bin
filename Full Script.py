#  ALL CODE BELONGS TO SURVEXE-PC
#  Written 2023, March 19 | Licensed under MIT on 2023, March 19 | And released 2023, March 19 | Current Version: v3.03192023
#  https://github.com/SurvExE-Pc/




# FFmpeg: https://ffmpeg.org/
# Bad Apple: https://youtu.be/FtutLA63Cp8/
































import cv2
import os
import subprocess
import numpy as np
import time
import yaml

prgrm_t = time.time()

#Config

config = None
with open("config.yaml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        exit(-1)

#Danger options
convertVideo = config['danger']['convertVideo']
splitVideo = config['danger']['splitVideo']
writeOut = config['danger']['writeOut']
convertToBinary = config['danger']['convertToBinary']

#Video options
VID_WIDTH = config['video']['width']
VID_HEIGHT = config['video']['height']
INVID_NAME = config['video']['input_name']
VID_NAME = config['video']['output_name']

#Binary Options
BIN_NAME = config['binary']['output_name']

#End Config

#Cleanup
if os.path.exists(f"{VID_NAME}.mp4"):
    os.remove(f"{VID_NAME}.mp4")
if os.path.exists(f"{BIN_NAME}.bin"):
    os.remove(f"{BIN_NAME}.bin")

#Resize and convert video.
if convertVideo:
    cnvv_t = time.time()
    cmd = subprocess.Popen(f"ffmpeg.exe -i {INVID_NAME}.mp4 -vf scale=w={VID_WIDTH}:h={VID_HEIGHT},format=pix_fmts=monow {VID_NAME}.mp4")
    cmd.communicate()
    cnvv_te = time.time()

#Split Video Into Frames.
if splitVideo:
    splv_t = time.time()
    cam = cv2.VideoCapture(f"{VID_NAME}.mp4")
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')
    currentframe = 0
    while(True):
        ret,frame = cam.read()
        if ret:
            name = './data/frame' + str(currentframe) + '.png'
            print('Creating...' + name)
            cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break
    cam.release()
    cv2.destroyAllWindows()
    splv_te = time.time()

#Convert All Frames to binary
binary_frames = []

if convertToBinary:
    cftb_t = time.time()
    for i in range(len(os.listdir("data"))):
        image = cv2.imread(f"data/frame{i}.png") 
        print(f"Binning data/frame{i}.png")
        binary_frame = []
        for i, j in np.ndindex(image.shape[:-1]):
            pixel = image[i,j]
            if pixel[0] < 127.5:
                pixel = [0,0,0]
            elif pixel[0] > 127.5:
                pixel = [255,255,255]
            else:
                pixel = [0,0,0]
            if pixel == [0,0,0]:
                binary_frame.append(str(0))
            elif pixel == [255,255,255]:
                binary_frame.append(str(1))
        binary_frames.append("".join(binary_frame))
    cftb_te = time.time()

#Write final binarystring to a file.
if writeOut:
    wrto_t = time.time()
    with open(f'{BIN_NAME}.bin',mode='w') as binFile:
        binaryData = "".join(binary_frames)
        binFile.write(binaryData)
    wrto_te = time.time()

#Timing stuff
try:
    print(f"Converting video took {0-(cnvv_t-cnvv_te)}s.")
except:
    print("No time recorded for converting video.")
try:
    print(f"Spliting video took {0-(splv_t-splv_te)}s.")
except:
    print("No time recorded for spliting video.")
try:
    print(f"Converting frame to binary took {0-(cftb_t-cftb_te)}s.")
except:
    print("No time recorded for binary conversions.")
try:
    print(f"Writing binary took {0-(wrto_t-wrto_te)}s.")
except:
    print("No time recorded for writing process.")
print(f"Final program took {0-(prgrm_t-time.time())}s.")