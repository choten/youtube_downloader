import sys
from pytube import YouTube
import re

def downLoadVideo():
    yt = YouTube(url)
    yt.register_on_progress_callback(show_progress_bar)
    yt.register_on_complete_callback(convert_to_aac)
    yt.streams.filter(progressive=True).order_by('resolution').desc().first().download()

def convert_to_aac(stream, file_handle):
         return print('\n下載成功!')

def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
        percent =  (1 - (bytes_remaining/stream.filesize))*100
        sys.stdout.write("\r下載進度: %d%%" % percent)
        sys.stdout.flush()

def is_url_valid(url):
    pattern = re.compile(r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$")
    result = pattern.search(url)
    return False if result == None else True
    
url = input("請輸入youtube影片網址:\n")

while is_url_valid(url) == False:
    print("youtube影片網址有誤!")
    url = input("請重新輸入youtube影片網址:\n")

try:
    downLoadVideo()
    
except Exception as e:
    print('發生錯誤，無法下載影片。')
    print(e)

input()