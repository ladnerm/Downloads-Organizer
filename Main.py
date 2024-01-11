import os
import shutil
import sys


dwnldPath = "/Users/maxladner/Downloads"
imagePath = "/Users/maxladner/Documents/Downloaded Images"
videoPath = "/Users/maxladner/Documents/Downloaded Videos"
docsPath = "/Users/maxladner/Documents/Downloaded Docs"
musicPath = "/Users/maxladner/Documents/Downloaded Music"
miscellaneousPath = "/Users/maxladner/Documents/Miscellaneous"

def move(oldPath, newPath):
	shutil.move(oldPath, newPath)


def LoggingEventHandler():
	with os.scandir(dwnldPath) as files:
		for file in files:
			if file.name.endswith((".jpg", ".jpeg", ".HEIC", ".heic")):
				move(file, imagePath)
			elif file.name.endswith((".mov", ".mp4", ".MP4")):
				move(file, videoPath)
			elif file.name.endswith((".mp3", ".m4a")):
				move(file, musicPath)
			elif file.name.endswith((".png", ".pdf")):
				move(file, docsPath)
			else:
				move(file, miscellaneousPath)



			

LoggingEventHandler()
