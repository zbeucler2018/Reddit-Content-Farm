
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


def makeFilm():
    clips = []
    paths = []
    listOfVideos = os.listdir("./videos")
    for clip in listOfVideos:
        clip = os.path.join("./videos/", clip)
        paths.append(clip)

        clips.append(VideoFileClip(clip))

    final_clip = concatenate_videoclips(clips, method='compose')
    final_clip.write_videofile(
        "./final.mp4", codec='libx264', audio_codec="aac")

    for item in paths:
        os.remove(item)


if __name__ == '__main__':
    main()
