import socket
import time
from imutils.video import VideoStream  #imutils
import imagezmq

#image를 보내는 허브 (같은 내부망에 연결)
sender = imagezmq.ImageSender(connect_to = "tcp://192.168.0.1:5555")

#RPI hostname 에 each image를 보낸다
rpi_name = socket.gethostname() 

picam = VideoStream(usePiCamera = True).start()
#카메라 센서 워밍업
time.sleep(2.0)

while True:
    #Vidoe Stream을 읽는다
    image = picam.read()

    sender.send_image(rpi_name, image)