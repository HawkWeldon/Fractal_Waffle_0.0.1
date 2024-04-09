import cv2
import os
os.system('clear')
current_directory = os.getcwd()
###########################################################################################
vid = cv2.VideoCapture(current_directory+'/output/output.avi')
success,image = vid.read()
c = 0
###########################################################################################
while success:
  cv2.imwrite(current_directory+"/reverse_output/image%3d.jpg" % c, image)    
  success,image = vid.read()
  print('Reading frame: ', c)
  c = c + 1
###########################################################################################
print('done')
###########################################################################################