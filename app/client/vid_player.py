from subprocess import Popen

movie1 = '/home/kyle/Desktop/vids/vid.mp4'
omxc = Popen(['omxplayer', '-b', movie1])
