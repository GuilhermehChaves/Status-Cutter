from __future__ import unicode_literals
import youtube_dl
import os

ydl_options = {}
os.chdir('./videos')

with youtube_dl.YoutubeDL(ydl_options) as ydl:
  ydl.download(['https://www.youtube.com/watch?v=GZgnl5Ocuh8'])
