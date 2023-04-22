from pytube import YouTube
import os

def Download(link,yt_format):
    youtubeObject = YouTube(link)
    try:
        if yt_format == "mp3":
            youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
            destination = str("DownLoadMp3List")
            out_file = youtubeObject.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'

        elif yt_format == "mp4":
            youtubeObject = youtubeObject.streams.filter().get_highest_resolution()
            destination = str("DownLoadMp4List")
            out_file = youtubeObject.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp4'
        os.rename(out_file, new_file)
    except:
        print("An error has occurred")
    print("Download is completed successfully")



link_list=[]
with open('downloader_list.txt', 'r') as fh:
    for line in fh:
        if "https://www.youtube.com/" in str(line):
            link_list.append(str(line))

print("Link List",link_list)

def working(yt_format):
    while True:
        list_length = len(link_list)
        list_length = 0 if list_length == 0 else list_length
        for link in link_list: 
            if "https://www.youtube.com/" in link:
                list_length = len(link_list)
                try: 
                    Download(link,yt_format)
                    link_list.remove(link)
                except:
                    print(link)
            else:
                link_list.remove(link)

            print("Link List: ",list_length)
        if list_length == 0 or list_length == 1:
            break

get_one_link = str(input("Add a link or add links to the downloader_list.txt file and run it again: "))

if "https://www.youtube.com/" in get_one_link:
    print("Link Added successfully")
    link_list.append(get_one_link)
    yt_format = str(input("what is the format to download(mp3 or mp4): "))
    if yt_format == "mp3" or yt_format == "mp4":
        working(yt_format)
    else:
        print("Not Working")
else:
    print("Not Link Working, If the file is full it will work with")
    yt_format = str(input("what is the format to download(mp3 or mp4): "))
    if yt_format == "mp3" or yt_format == "mp4":
        working(yt_format)
    else:
        print("Not Working")


