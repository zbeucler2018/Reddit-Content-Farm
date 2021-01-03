try:
    import asyncio
    import os

    from Reddit import getRedditPost
    from image import createImage
    from TTS import textToSpeech
    from merge import combineAudioAndImage
    from final import makeFilm
except ImportError:
    print()
    print("ERROR: Problem importing packages in {}").format(
        os.path.realpath(__file__))
    print("Please try \'pip install -r requirements.txt\' to install all required packages")
    print()


def main():
    postType = str(input(
        "Please enter what type of posts you want (t = top, n = new, h = hot): ")).lower()
    postTypes = ["t", "n", "h"]
    while postType not in postTypes:
        print("Incorrect entry")
        postType = str(input(
            "Please enter what type of posts you want (t = top, n = new, h = hot): ")).lower()

    amount = input(
        "Please enter the amount (1-10) of posts you want in the video: ")
    while amount.isnumeric() == False:
        print("incorrect input, please try again")
        amount = input(
            "Please enter the amount (1-10) of posts you want in the video: ")
    amount = int(amount)
    while amount > 10:
        print("Value too high, please try again")
        amount = input(
            "Please enter the amount (1-10) of posts you want in the video: ")

    x = asyncio.run(getRedditPost(postType, amount))
    count = 0
    '''
    for i in x:
        count += 1
        createImage(i)
        y = textToSpeech(i)
        combineAudioAndImage(y, count)
    makeFilm()

    '''


main()
