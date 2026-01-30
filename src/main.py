from picamzero import Camera

cam = Camera()

cam.take_photo("image1.jpg")

with open("result.txt", "w") as f:
    f.write("100")
