## Import the Camera class from the picamzero (picamera-zero) module
# from picamzero import Camera
#
# # Create an instance of the Camera class
# cam = Camera()
#
# cam.capture_sequence("sequence", num_images=3, interval=3)
#
# from astro_pi_orbit import ISS
# from picamzero import Camera
#
# iss = ISS()
#
# def get_gps_coordinates(iss):
#     """
#     Returns a tuple of latitude and longitude coordinates expressed
#     in signed degrees minutes seconds.
#     """
#     point = iss.coordinates()
#     return (point.latitude.signed_dms(), point.longitude.signed_dms())
#
# cam = Camera()
# cam.take_photo("gps_image1.jpg", gps_coordinates=get_gps_coordinates(iss))




# EXAMPLE OF WRITING TO results.txt -------------------------------------
# estimate_kmps = 7.1234567890  # Replace with your estimate
#
# # Format the estimate_kmps to have a precision
# # of 5 significant figures
# estimate_kmps_formatted = "{:.4f}".format(estimate_kmps)
#
# # Create a string to write to the file
# output_string = estimate_kmps_formatted
#
# # Write to the file
# file_path = "result.txt"  # Replace with your desired file path
# with open(file_path, 'w') as file:
#     file.write(output_string)
#
# print("Data written to", file_path)




