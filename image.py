try:
    import os
    import PIL
    from PIL import Image, ImageDraw, ImageFont
    import textwrap
    import unihandecode
except ImportError:
    print()
    print("ERROR: Problem importing packages in {}").format(
        os.path.realpath(__file__))
    print("Please try \'pip install -r requirements.txt\' to install all required packages")
    print()


def createImage(postContent):
    font = ImageFont.truetype("Andale Mono.ttf", 15)

    im = Image.new(mode="RGB", size=(
        1280, 720), color=(153, 153, 255))
    draw = ImageDraw.Draw(im)
    # convert from latin-1 encoding to ascii
    postContent = unihandecode.unidecode(postContent)
    # lines are only 120 characters
    text = textwrap.fill(postContent, 120)
    draw.text((100, 100), text, fill=(255, 255, 0))     # draw lines on image
    # im.show()
    im.save("image.jpg")


if __name__ == '__main__':
    main()
