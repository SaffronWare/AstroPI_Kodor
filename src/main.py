from picamzero import Camera

cam = Camera()

cam.take_photo("image1.jpg")


def accelerometerCalculation():
    return 1000


with open("result.txt", "w") as f:
    speed = accelerometerCalculation()
    speed = str(round(speed,5)) 
    f.write(speed)



