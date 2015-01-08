__author__ = 'nico'

imgur_client_id = "faecd226b95e22c"

deck_image = "_deck.jpg"

x_total = 6000
y_total = 6000

JPEG_QUALITY = 30

import os
from PIL import Image
import pyimgur

# import requests
from requests.packages.urllib3 import disable_warnings

disable_warnings()

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


def card70(path):
    cards = get_files(path, "70")
    if len(cards):
        if os.path.exists(cards[0]):
            return cards[0]

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
    size_box = (x_size, y_size)
    for f in files:
        print ".",
        # print f
        cur = Image.open(f)
        cur = cur.resize(size_box, Image.FLOYDSTEINBERG)
        i.paste(cur, (x, y))
        x += x_size
        if x >= x_total:
            x = 0
            y += y_size

    # Add Card # 70
    try:
        c70 = card70(path)
        if c70:
            c70img = Image.open(c70)
            c70img = c70img.resize(size_box, Image.FLOYDSTEINBERG)
            i.paste(c70img, (x_total - x_size, y_total - y_size))
    except:
        print "Adding card 70 failed."

    i.save(deck_image, format="JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
    # i.save("_deck.png", format="PNG", optimize=True, progressive=True)
    try:
        print len(files), "cards in this deck!"
        print "initializing Imgur"
        imgur = pyimgur.Imgur(imgur_client_id, verify=False)
        print "uploading...."
        uploaded = imgur.upload_image(deck_image, title="Tabletop Simulator deck")
        print "Success!"
        print "Image link:", uploaded.link
        make_url_link(uploaded.link)
        os.system("echo " + uploaded.link + " | clip")
        print "..copied to clipboard!"
    except Exception, err:
        print err
        print "Something went wrong :/, probably imgur."
        print "\nThe image has been saved to %s though!" % deck_image

    dummy = raw_input("\nDone. Please press Enter to exit.")


if __name__ == "__main__":
    main()
