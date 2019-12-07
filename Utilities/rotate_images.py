from PIL import Image
import os

def rotate(image_path, degrees_to_rotate, saved_location):
    """
    Rotate the given photo the amount of given degreesk, show it and save it
    @param image_path: The path to the image to edit
    @param degrees_to_rotate: The number of degrees to rotate the image
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image.save(saved_location)

if __name__ == '__main__':
    for img in os.listdir("/home/anvit/Desktop/Data/INbreast/equalized_PNG_394_resized_ambiremoved/"):
        print(img)
        rotate("/home/anvit/Desktop/Data/INbreast/equalized_PNG_394_resized_ambiremoved/" + img, 90, "/home/anvit/Desktop/Data/INbreast/equalized_PNG_394_resized_ambiremoved_rotated/" + img)
