from __future__ import unicode_literals
import youtube_dl
import os
from video import Video

ydl_options = {}
os.chdir('./videos')

with youtube_dl.YoutubeDL(ydl_options) as ydl:
  info = ydl.extract_info('https://www.youtube.com/watch?v=tVWF0hcbx58&t=88s')
  # ydl.download(['https://www.youtube.com/watch?v=tVWF0hcbx58&t=88s'])


os.chdir('../') 
video = Video('saitama', './videos/'+info['title'] + '-' + info['id'] + '.mp4')
video.cut()
# print(info['title'],info['id'])
