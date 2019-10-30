from moviepy.editor import *

class Video:
  def __init__(self, name,path):
    self._name = name
    self._path = path
  
  def getName(self):
    return self._name

  def setName(self, name):
    self._name = name

  def getPath(self):
    return  self._path
  
  def setPath(self, path):
    self._path = path
  

  def cut(self):
    video = VideoFileClip(self._path)
    times = int((video.duration)/30)
    
    initTime = 0
    finalTime = 30

    hasRest = isinstance((video.duration/30), int)

    for i in range(times):
      video = VideoFileClip(self._path).subclip(initTime, finalTime)
      video.write_videofile("./cutted/"+self._name+"-"+str(i)+".mp4")

      initTime += 30
      finalTime +=30
    

    if(not hasRest): #Caso tenha resto o video (Parte final com menos de 30seg)
      video = VideoFileClip(self._path)
      rest = int(video.duration - (times * 30))
      initTimeRest = times * 30
      finalTimeRest = initTimeRest + rest

      video = VideoFileClip(self._path).subclip(initTimeRest, finalTimeRest)
      video.write_videofile("./cutted/"+self._name+"-"+str(times)+".mp4")
  