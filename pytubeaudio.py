import pytube

outro = 's'
while outro == 's':
    url = input('Link: ')
    try:
        yt = pytube.YouTube(url)
        video = yt.streams.get_audio_only()
        video.download('C:/Downloads')
        print('Download completo')
    except:
        print('link incorreto')
    outro = input('Outro Link?[s/n]\n')
