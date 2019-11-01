from __future__ import unicode_literals
import youtube_dl
import os
from video import Video

ydl_options = {}
os.chdir('./videos')#trocando de diretorio para salvar no diretorio ./videos

with youtube_dl.YoutubeDL(ydl_options) as ydl:
  info = ydl.extract_info('https://www.youtube.com/watch?v=WNeLUngb-Xg')
  # ydl.download(['https://www.youtube.com/watch?v=tVWF0hcbx58&t=88s'])


os.chdir('../') #voltando para o diretório raiz

os.rename('./videos/'+info['title'] + '-' + info['id'] + '.mp4', './videos/In the end.mp4')

video = Video('In the end', './videos/In the end.mp4')
video.cut()
# print(info['title'],info['id'])
