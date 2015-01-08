__author__ = 'nico'

imgur_client = "faecd226b95e22c"

deck_image = "_deck.jpg"

x_total = 5000
y_total = 5000

JPEG_QUALITY = 40

import os
from PIL import Image
import pyimgur


def get_files(dir=".", pattern=".png"):
    files = [os.path.join(dir, x) for x in os.listdir(dir) if pattern in x]
    key = lambda x: x[::-1]
    files.sort(key=key)
    return files


def make_url_link(url):
    text = "[InternetShortcut]\nURL="
    with open("deck-link.url", "wt") as f:
        f.write(text + url + "\n")
        f.close()


def main():
    path = raw_input("Directory to use ('.' = current -> just press Enter): ") or "."
    pattern = raw_input("Pattern of the card files (Enter -> '.png'): ") or ".png"
    files = get_files(path, pattern)
    print len(files), "found in ", path, "matching", pattern

    if not len(files):
        raise SystemExit

    i = Image.new('RGBA', (x_total, y_total), "Blue")
    x = y = 0
    x_size = x_total / 10
    y_size = y_total / 7
    for f in files:
        print ".",
        # print f
        cur = Image.open(f)
        cur = cur.resize((x_size, y_size), Image.FLOYDSTEINBERG)
        i.paste(cur, (x, y))
        x += x_size
        if x >= x_total:
            x = 0
            y += y_size
    i.save(deck_image, format="JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
    # os.execl("Deck.jpg")
    try:
        print len(files), "cards in this deck!"
        print "initializing Imgur"
        imgur = pyimgur.Imgur(imgur_client)
        print "uploading...."
        uploaded = imgur.upload_image(deck_image, title="Tabletop Simulator deck")
        print "Success!"
        print "Image link:", uploaded.link
        make_url_link(uploaded.link)
        # execfile(uploaded.permalink)
    except Exception, err:
        print err
        print "Something went wrong :/, probably imgur."
        print "\nThe image has been saved to %s though!" % deck_image
    dummy = raw_input("\nDone. Please press Enter to exit.")
    # execfile(deck_image)

    pass


if __name__ == "__main__":
    main()
