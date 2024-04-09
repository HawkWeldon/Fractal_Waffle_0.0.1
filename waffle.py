import cv2
import os
import shutil
import ffmpeg
os.system('clear')
current_directory = os.getcwd()
###########################################################################################
def form_using_image_folder(image_folder):
    video_name = 'vid.avi'
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    fourcc = 0
    video = cv2.VideoWriter(video_name, fourcc, 10, (1920,1080))
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    cv2.destroyAllWindows()
    video.release()
###########################################################################################
image_folder = current_directory + '/input'
form_using_image_folder(image_folder)
###########################################################################################
(
    ffmpeg.input("vid.avi")
          .output('output/output.avi',vcodec = 'h264')
          .run()
)
os.remove('vid.avi')
###########################################################################################