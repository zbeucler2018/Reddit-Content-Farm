try:
    from gtts import gTTS
    import os
    from mutagen.mp3 import MP3
except ImportError:
    print()
    print("ERROR: Problem importing packages in {}").format(
        os.path.realpath(__file__))
    print("Please try \'pip install -r requirements.txt\' to install all required packages")
    print()
    exit()


def textToSpeech(text):
    speech = gTTS(text=text, lang='en', slow=False)
    # print(text)
    speech.save("text.mp3")
    audio = MP3("text.mp3")
    # print(audio.info.length)
    return audio.info.length  # float for seconds


if __name__ == '__main__':
    main()
