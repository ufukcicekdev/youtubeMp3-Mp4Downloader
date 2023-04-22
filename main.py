from pytube import YouTube
import os

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
    try:
        destination = str("DownLoadList")
        out_file = youtubeObject.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    except:
        print("An error has occurred")
    print("Download is completed successfully")



link_list=[]
with open('downloader_list.txt', 'r') as fh:
    link_list = [str(line) for line in fh]

def working():
    while True:
        list_length = len(link_list)
        list_length = 0 if list_length == 0 else list_length
        for link in link_list: 
            list_length = len(link_list)
            try: 
                Download(link)
                link_list.remove(link)
            except:
                print(link)
            print("Link List: ",list_length)
        if list_length == 0 or list_length == 1:
            break

get_one_link = str(input("Add a link or add links to the downloader_list.txt file and run it again: "))

if "https://www.youtube.com/" in get_one_link:
    print("Link Added successfully")
    link_list.append(get_one_link)
    working()
else:
    print("Not Link Working, If the file is full it will work with")
    working()


