import os
import json
import cv2
import numpy as np

# Paths to Labelme JSON file and output mask file
img_json_folder = "/home/subblue-3/nextGen/data/attitude_estimation_in_lab_20250820/image_mask/labelme_json/"
output_mask_folder = "/home/subblue-3/nextGen/data/attitude_estimation_in_lab_20250820/image_mask/mask/"
os.makedirs(output_mask_folder, exist_ok=True)

# define label grayscale value
label_map = {
    "disc": 255
}


#=========== loop through all json files to convert to mask ===========#
count_int = 0
for json_file in os.listdir(img_json_folder):
    # load lableme_json file
    json_path = img_json_folder + json_file
    with open(json_path, 'r') as f:
        data = json.load(f)

    # image dimension
    image_width = data["imageWidth"]
    image_height = data["imageHeight"]

    # create a blank mask image
    mask = np.zeros((image_height, image_width), dtype=np.uint8)

    # loop through each shape in the json
    for shape in data["shapes"]:
        label = shape["label"]
        points = np.array(shape["points"], dtype=np.int32)

        # draw "disc" as filled polygon
        if label == "disc":
            cv2.fillPoly(mask, [points], color=label_map[label])

    # save mask
    output_mask_path = os.path.join(output_mask_folder, json_file.replace(".json", ".png"))
    cv2.imwrite(output_mask_path, mask)

    count_int = count_int + 1
    print(f"mask saved {count_int}")


"""
#=========== test on single json ===========#
# load lableme_json file
json_file = "roll1.65_pitch-10.85.json"
test_json_path = img_json_folder + json_file
with open(test_json_path, 'r') as f:
    data = json.load(f)

# Print all top-level keys
print("Top-level keys in this JSON:")
for key in data.keys():
    print("-", key)

# image dimension
image_width = data["imageWidth"]
image_height = data["imageHeight"]

# create a blank mask image
mask = np.zeros((image_height, image_width), dtype=np.uint8)

# loop through each shape in the json
for shape in data["shapes"]:
    label = shape["label"]
    points = np.array(shape["points"], dtype=np.int32)

    # draw "disc" as filled polygon
    if label == "disc":
        cv2.fillPoly(mask, [points], color=label_map[label])

# save mask
output_mask_path = os.path.join(output_mask_folder, json_file.replace(".json", ".png"))
cv2.imwrite(output_mask_path, mask)
print(f"mask saved to {json_file}")
"""



