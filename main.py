import os, time, Data, cv2
import numpy as np
import matplotlib.pyplot as plt
from optical_flow import flow
from img_registration import register
from dataProcessing import *

directory = os.getcwd() + "/out/"

#reads data of one output file
#return list of data objects and 2d list of values
def read(file):
	file = open(directory+file, "r")
	inp = file.read().split("\n")[:-1]
	data = []
	for line in inp:
		data.append(Data.Data.fromStr(line))

	dataArray = np.array(data)
	dataMap = formatMap(dataArray)

	return dataArray, dataMap

#formats a list of data objects into a 2d map
#returns 2d list
def formatMap(data):
	m = np.empty([551, 501, 3], dtype=np.uint8)
	for d in data:
		if d.val * 255 < -4:
			for i in range(3):
				m[551-(d.lat+1)][501-(d.lon+1)][i] = abs(d.val) * 255
	return m

if __name__ == "__main__":

	# just list of file names
	files = sortFiles(initFiles(directory))

	# list of data objects
	data, dataMap = (read(files[0]))

	imgs = []
	for i in range(len(files)): 
		imgs.append(read(files[i])[1])

	first_frame, last_frame, overlay = flow(imgs)
	display(first_frame, name="first frame")
	display(last_frame, name="last frame")
	display(overlay, name="overlay")
	save(overlay, "last.png")