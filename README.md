# Vid2Bin
 A simple monochrome video to binary converter

## Setup
 First you need to install [opencv](https://opencv.org/) for python: [PyPi Page](https://pypi.org/project/opencv-python/).
 NumPy and PyYAML should be installed automaticly with python 3.11, if you don't have them they are required, Versions of
 what I am using are at the bottom, 
 <pre>
 I am using:
 Python version: 3.11.2 (64-bit)
 Module versions:
   numpy              1.24.2
   opencv-python      4.7.0.72
   PyYAML             6.0
 </pre>
 #### Module List:
 <pre>
   cv2
   os
   subprocess
   numpy
   time
   yaml
   requests
 </pre>

## Usage
  Used to convert a monochrome video to binary.
  You can modify settings in the config.yaml file.

## Config
  #### Rules
    ALL FILENAMES MUST NOT HAVE AN EXTENSION IN THE CONFIG.
    Any input video must be a MP4 file or it wont work.
  #### Video Options
    width: The width of the output video.
    height: The height of the output video.
    input_name: the name of the monochrome video to use.
    output_name: the name of the output video.
  #### Binary Options
    output_name: the name of the binary string file.
  #### Danger Options
    The items in the danger section can break the process so ONLY use if you know what you are doing.
