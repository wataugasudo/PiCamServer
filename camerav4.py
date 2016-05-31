import picamera
from picamera import PiCamera
import time
from datetime import datetime
import os.path
from subprocess32 import Popen

print "\nSecurity Camera Logger v3 | Ben Broce & William Hampton\n\n"
print "Streams video to vids/vidstream.h264 | Captures to pics/[timestamp].jpg"
print "Ctrl-C quits.\n\n"

stream = raw_input("Should I stream video (y/n)? ")
length = float(raw_input("How long should I run (in minutes): "))*60
interval = float(raw_input("How often should I take a picture (in seconds): "))

print "Running..."

if stream == "y":
	Popen(["./livestream.sh"])

camera = PiCamera()
camera.annotate_background = picamera.Color('black')
camera.rotation = 180
camera.resolution = (640, 480)

counter = 0

try:
	camera.start_preview()
	while (counter <= length):
		timestamp = datetime.now().strftime("%m-%d-%Y_%H:%M:%S")
		camera.annotate_text = timestamp
		path = '/var/www/PiCamServer/pics/' + timestamp + '.jpg'
		camera.capture(path, use_video_port=True)
		time.sleep(interval)
		counter += interval
finally:
	print "Exiting..."
	camera.stop_preview()
