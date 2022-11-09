#flag=imp

from metadata_remover.commons import cls, exiftool, wait, validate, filetype
from metadata_remover.mrt import bulk, bulk1, singly, meta

import os
from shutil import move,copy

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="name of file")
parser.add_argument("-x", "--exif", action="store_true",
                    help="view metadata in a file")
parser.add_argument("-b", "--batch", action="store_true",
                    help="run for all files in a directory")
parser.add_argument("-r", "--recursive", action="store_true",
                    help="with -b, search recursively through directory")
args = parser.parse_args()

# Validate input
validate(args.file, args)

# To check 
if args.exif:
    exiftool()
    meta(args.file)
    wait()

# If it's a single file
if not args.batch:
    singly(args.file, filetype(args.file))

# If it's a directory
else:
    print("else")
    # All images
    # All videos


# x='1'
# while x in ['1','2','3','4','5','6','7']:
#     cls()
#     print('''
#     \n |------ Metadata Removal Tool ------|\n
#         3)Remove Metadata from a audio.
#         4)Remove Metadata from a Torrent.
#         5)Remove Metadata from all images in folder.
#         6)Remove Metadata from all videos in folder.
#         c)Close.
#     ''')
#     x = input('\n Enter command(1,2,3,4,5,6,7 or c):')
#     match x:
#         case '3':
#             file=input('\n Enter Audio File:')
#             # os.makedirs('tmp')
#             # y=copy(file,'tmp')
#             # os.chdir('tmp')
#             os.system('py ../mat2.py ' + file)
#             y=move(file.split('.')[0]+'.cleaned.'+file.split('.')[1],'..')
#             os.remove(file)
#             os.rmdir('tmp')
#             os.chdir('..')
#         case '4':
#             file=input('\n Enter Torrent File:')
#             os.makedirs('tmp')
#             y=copy(file,'tmp')
#             os.chdir('tmp')
#             os.system('py ../mat2.py '+file)
#             y=move(file.split('.')[0]+'.cleaned.'+file.split('.')[1],'..')
#             os.remove(file)
#             os.chdir('..')
#         case '5':
#             bulk()
#         case '6':
#             bulk1()
# exit()