import os
import shutil
import sys


dwnldPath = "/Users/USERNAME/Downloads"
imagePath = "/Users/USERNAME/Documents/Images"
videoPath = "/Users/USERNAME/Documents/Videos"
docsPath = "/Users/USERNAME/Documents/Docs"
musicPath = "/Users/USERNAME/Documents/Music"


def checkDir(path):
	if not os.path.isdir(path):
		os.mkdir(path)

def move(oldPath, newPath):
	shutil.move(oldPath, newPath)


def LoggingEventHandler():


	with os.scandir(dwnldPath) as files:
		for file in files:
			if file.name.endswith((".jpg", ".jpeg", ".HEIC", ".heic")):
				checkDir(imagePath)
				move(file, imagePath)
			elif file.name.endswith((".mov", ".mp4", ".MP4")):
				checkDir(videoPath)
				move(file, videoPath)
			elif file.name.endswith((".mp3", ".m4a")):
				checkDir(musicPath)
				move(file, musicPath)
			elif file.name.endswith((".png", ".pdf")):
				checkDir(docsPath)
				move(file, docsPath)
			else:
				pass


LoggingEventHandler()
