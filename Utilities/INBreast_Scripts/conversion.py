#Convert dicoms to png (without mode equalization)

import mritopng

# Convert a since file
mritopng.convert_folder('/home/anvit/Desktop/Data/RSNA/stage1/', '/home/anvit/Desktop/Data/RSNA/images/')

# Convert a whole folder recursively
#mritopng.convert_folder('/home/user/DICOM/', '/home/user/PNG/')

