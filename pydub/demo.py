import pydub

if __name__ == "__main__":
    audio = pydub.AudioSegment.from_mp3('1.mp3')
    print(audio)
