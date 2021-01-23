# pip install moviepy
from moviepy.editor import VideoFileClip

clip = VideoFileClip("video.mp4")
# clip.write_gif("simple.gif")

clip.write_gif("simple3.gif",fps = 5)