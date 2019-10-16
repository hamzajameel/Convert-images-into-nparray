import numpy as np
from PIL import Image
import PIL
import cv2
import glob

def main(im):
  img = Image.open(im)
  num =np.array(im)
  # print("Image" , num)
  # im = cv2.imread(im)
  arr = np.asarray(img,dtype="int32")
  maximum = (100,100)
  img.thumbnail(maximum,PIL.Image.ANTIALIAS)
  # print ('Image',type(im),im.shape,num,ar)
  arr=np.array(img)

  print("Image",img,arr)
  img.show()

for i in glob.glob('photos/*.jpg'):
    # img_name=str(i)
    # img_name_com=img_name + 'Photos/"*.jpg"'
    main(i)
