import cv2
import imagezmq

#image를 받는 허브 
image_hub = imagezmq.ImageHub()

while True:
    rpi_name, image = image_hub.recv_image()

    cv2.imshow(rpi_name, image)
    if cv2.waitKey(1) ==ord('q'):
        break
#허브에 응답을 보내준다 
    image_hub.send_reply(b"OK")

