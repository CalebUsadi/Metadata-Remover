# Preliminaries 
It is recommended to compile the run.c file using mingw C Compiler in windows.

Mingw C compiler is available with Dev C++ and Code Blocks IDE try them out!

# Installation

1: Install Codeblocks IDE from https://www.codeblocks.org/downloads/binaries/ , choose installer which ends with mingw-setup.exe 

2: Open run.c and build in code blocks.

<img src="../img/compile.png">

3: Download [ exiftool ](https://exiftool.org/) and [ ffmpeg ](https://www.ffmpeg.org/) , Create Images and Videos folder and organize all stuff as shown in image below: -

<img src="../img/organize.png">

# Usage

To clean a single image:- [ RECOMMENDED ]

1. Put all images in Images Folder.
2. Click run.exe
3. In Menu . Type 1 to select image sanitization.
4. Program will ask 'Enter Image name:',Enter a single image file name which is inside the Images Folder.

Example:-

let as assume a.jpg is in Images Folder.Then when program prompts you then:-

Enter Image name:a.jpg

If you get metadata was cleaned successfully message then most metadata should have been removed.
THOUGH THIS NEVER COMPLETELY REMOVES ALL  METADATA COMPLETELY .

To clean images in bulk:- [ NOT RECOMMENDED ]

1. Put all images in Images Folder.
2. Click run.exe
3. In Menu . Type 1 to select image sanitization.
4. Program will ask 'Enter Image name:',Enter * imagename extension which will clean all images with that extension
  present in the Images Folder.

Example:-

let as assume you have 10 jpg images in Images Folder you want to clean them all then:-

Enter Image name:*.jpg

You may get metadata was cleaned successfully message but it MAY BE MISLEADING.IN THIS CASE YOU ARE STRONGLY
RECOMMENDED TO MANUALLY CHECK WHETHER EACH IMAGE WAS CLEANED SUCCESSFULLY USING input.txt AND output.txt FILES
WHICH HAS METADATA OF IMAGES BEFORE CLEANING AND AFTER CLEANING RESPECTIVELY. 

To Clean Videos:-

1. First put the videos in Videos Folder.
2. Click run.exe
3. In Menu , Type 2 to select video sanitization.
4. Program will ask 'Enter Video name:',Enter a single video file name which is inside the Videos Folder.

Example:-

let as assume a.mp4 is in Videos Folder.Then when program prompts you then:-

Enter Video name:a.mp4

THIS NEVER COMPLETELY REMOVES ALL METADATA.
DUE TO LIMITATIONS OF SANITIZATION ,NO MESSAGE WILL BE DISPLAYED IF VIDEO WAS SUCCESSFULLY CLEANED OR NOT!
U HAVE TO MANUALS CHECK METADATA USING FILE PROPERTIES OR BETTER USE EXIFTOOL TO VIEW METADATA.

NOTE BULK SANTIZATION OF VIDEO FILES IS NOT CURRENTLY SUPPORTED AT THIS MOMENT.