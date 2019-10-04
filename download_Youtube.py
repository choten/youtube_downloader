import sys
from pytube import YouTube

def DownLoadVideo():
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

url = input("請輸入youtube影片網址:\n")

try:
    DownLoadVideo()
    
except Exception as e:
    print('發生錯誤，無法下載影片。')
    print(e)

input()