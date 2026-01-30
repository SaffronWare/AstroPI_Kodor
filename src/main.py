from picamzero import Camera
import time

SAMPLE_RATE = 1 # per second
TIME_STEP = 1/SAMPLE_RATE

cam = Camera()

def test():
    picture_index = 0
    frame_time = 0
    start = time.monotonic()
    last_frame_end = time.monotonic()
    while time.monotonic() - start < 10:
        cam.take_photo(f"picture{picture_index}_time:{time.monotonic()-start}")
        picture_index += 1
        frame_time = time.monotonic()- last_frame_end
        if frame_time < TIME_STEP:
            # time.sleep(TIME_STEP - frame_time)
            pass # for now imma just take pics as quickly as possible
        last_frame_end = time.monotonic()
    
    return 100 # random exmample



with open("result.txt", "w") as f:
    speed = test()
    f.write(str(round(speed,5)))



