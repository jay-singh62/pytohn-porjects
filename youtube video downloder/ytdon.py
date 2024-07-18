from pytube import YouTube

link= "https://youtu.be/HY-TBa_Y2-M?si=U8YZk99tYMkM8Agh"
youtube_1  =  YouTube(link)

print (youtube_1.thumbnail_url)
print(youtube_1.title)

video =  youtube_1.streams.all()


print(video)
print()