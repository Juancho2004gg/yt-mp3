from pytube import YouTube


print("""░█░█░█▀█░█░█░▀█▀░█░█░█▀▄░█▀▀░░░░░█▄█░█▀█░▀▀█
░░█░░█░█░█░█░░█░░█░█░█▀▄░█▀▀░▄▄▄░█░█░█▀▀░░▀▄
░░▀░░▀▀▀░▀▀▀░░▀░░▀▀▀░▀▀░░▀▀▀░░░░░▀░▀░▀░░░▀▀░""")

VIDEO_URL = input("Enter video url: ")

##SAVE_PATH = input("Select destination folder")


yt = YouTube(VIDEO_URL)

mp3_streams = yt.streams.filter(only_audio=True)

song = mp3_streams.get_by_itag("251")

try:
    song.download()
except Exception as e:
    print("Error trying to download audio from your link.")
else:
    print("Audio downloaded")