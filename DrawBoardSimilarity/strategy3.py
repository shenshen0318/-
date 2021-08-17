import os

import imagehash
import PIL
from PIL import Image
import numpy as np
from hexhamming import hamming_distance

material_root_path = "./Material/"

material_name_list = []
material_dis_list = []

for imgPath in os.listdir(material_root_path):
    material_name_list.append(imgPath)
    _tmp_hash = imagehash.whash(PIL.Image.open(os.path.join(material_root_path, imgPath)))
    material_dis_list.append(_tmp_hash)

target_image_hash = imagehash.whash(PIL.Image.open("Handwriting/handwrite2.JPG"))

distance = np.ones(len(material_dis_list), dtype=np.uint8) * 1e10
for i, mater_hash in enumerate(material_dis_list):
    distance[i] = ((mater_hash - target_image_hash)/len(target_image_hash.hash)**2) # hamming_distance(mater_hash, target_image_hash)

_index_similar = np.argmin(distance)
print(material_name_list[_index_similar])