try:
    import os
    import moviepy.editor
    from moviepy.editor import *
except ImportError:
    print()
    print("ERROR: Problem importing packages in {}").format(
        os.path.realpath(__file__))
    print("Please try \'pip install -r requirements.txt\' to install all required packages")
    print()
    exit()


def combineAudioAndImage(audioLength, videoNumber):
    filepath = "image.jpg"
    # print(filepath)
    clip = ImageClip(filepath).set_duration(audioLength+6)
    # creates a video thats 10 seconds long
    clip.write_videofile("video.mp4", fps=5)

    video_clip = VideoFileClip("./video.mp4")
    audio_clip = AudioFileClip("./text.mp3")

    final_clip = video_clip.set_audio(audio_clip)
    videoName = "./videos/{}.mp4".format(videoNumber)
    final_clip.write_videofile(
        videoName, codec='libx264', audio_codec="aac")

    os.remove("video.mp4")
    os.remove("image.jpg")
    os.remove("text.mp3")


if __name__ == '__main__':
    main()
