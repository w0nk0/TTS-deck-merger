__author__ = 'w0nk0'

import sys

from PySide.QtGui import *
from PySide.QtCore import *
from style import default_style as default_style

imgur_client_id = "faecd226b95e22c"

DECK_IMAGE_NAME = "_deck.jpg"

x_total = 5000
y_total = 5000

JPEG_QUALITY = 40

import os
from PIL import Image
import pyimgur
import time

# import requests
from requests.packages.urllib3 import disable_warnings

disable_warnings()


def get_files(dir=".", pattern=".png"):
    files = [os.path.join(dir, x) for x in os.listdir(dir) if pattern in x]
    key = lambda x: x[::-1]
    files.sort(key=key)
    return files


def make_url_link(url, path=""):
    text = "[InternetShortcut]\nURL="
    with open(os.path.join(path, "deck-link.url"), "wt") as f:
        f.write(text + url + "\n")
        f.close()


def card70(path):
    cards = get_files(path, "70")
    if len(cards):
        if os.path.exists(cards[0]):
            return cards[0]


def assemble_image(files, path, card70file=None, deck_path=None):
    if not deck_path:
        deck_path = os.environ["TEMP"]

    # print "ass_img.", str(locals())

    i = Image.new('RGBA', (x_total, y_total), "Blue")
    x = y = 0
    x_size = x_total / 10
    y_size = y_total / 7
    size_box = (x_size, y_size)
    failed = []
    for f in files:
        print ".",
        # print f
        try:
            cur = Image.open(f)
            cur = cur.resize(size_box, Image.FLOYDSTEINBERG)
            i.paste(cur, (x, y))
            x += x_size
            if x >= x_total:
                x = 0
                y += y_size
        except:
            failed.append(f)

    if failed:
        print "ADDING following cards failed!"
        for img in failed:
            print img

    # Add Card # 70
    try:
        c70 = card70file or card70(path)
        if c70:
            c70img = Image.open(c70)
            c70img = c70img.resize(size_box, Image.FLOYDSTEINBERG)
            i.paste(c70img, (x_total - x_size, y_total - y_size))
    except:
        print "\nAdding card 70 failed. None provided or other error."

    global DECK_IMAGE_NAME
    try:
        DECK_IMAGE_NAME = os.path.split(DECK_IMAGE_NAME)[-1]
    except Exception, err:
        print err
    out_name = os.path.join(deck_path, DECK_IMAGE_NAME)
    print "Saving as " + out_name  # /*deck_path +*/ on next line
    # print "DECK_IMAGE_NAME", DECK_IMAGE_NAME
    #print "ass_img.", str(locals())
    i.save(out_name, format="JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
    # i.save("_deck.png", format="PNG", optimize=True, progressive=True)
    return out_name


def make_deck(files, path, pattern, do_upload=True, card70=None):
    print len(files), "found in ", path, "matching", pattern
    if not len(files):
        print "Nothing to do!"
        return
    image_path = assemble_image(files, path, card70file=card70, deck_path=path)
    global DECK_IMAGE_NAME
    DECK_IMAGE_NAME = image_path
    try:
        print len(files), "cards in this deck!"
        if do_upload:
            print "initializing Imgur"
            imgur = pyimgur.Imgur(imgur_client_id, verify=False)
            print "uploading...."
            uploaded = imgur.upload_image(image_path, title="Tabletop Simulator deck")
            print "Success!"
            print "\n** Image link: %s **\n" % uploaded.link
            make_url_link(uploaded.link, path)
            os.system("echo " + uploaded.link + " | clip")
            print "..copied to clipboard!"
    except Exception, err:
        print err
        print "Something went wrong :/, probably imgur."
        print "\nThe image has been saved to %s though!" % DECK_IMAGE_NAME


def main():
    path = raw_input("Directory to use ('.' = current -> just press Enter): ") or "."
    pattern = raw_input("Pattern of the card files (Enter -> '.png'): ") or ".png"
    files = get_files(path, pattern)
    make_deck(files, path, pattern)

    dummy = raw_input("\nDone. Please press Enter to exit.")


class Writer(QObject):
    writer = Signal(object)

    def __init__(self, parent, stream):
        super(Writer, self).__init__(parent)
        try:
            assert isinstance(stream, file)
            self._stdout = stream
        except:
            print "No valid stream, won't also print"
            self._stdout = None
            # sys.stdout = self

    def __getattr__(self, item):
        # self._stdout.write("Getattr " + str(item))
        # print "getattr!"
        return getattr(self._stdout, item)

    def x__getattribute__(self, item):
        # if not item == self._stdout:
        try:
            self._stdout.write("Getattribute " + str(item))
        except:
            pass

    def write(self, txt):
        # print "Emitting!",txt
        self.writer.emit(txt)
        try:
            self._stdout.write(str(txt))
        except:
            pass
            # self.stdout.write(txt)
            #    #self.output.setPlainText(self.output.toPlainText() + txt)
            #    #self.output.repaint()
            #    write.emit(txt)


class DeckWorker(QObject):
    done = Signal()

    def __init__(self, files, path, ptn, upld, c70=None):
        super(DeckWorker, self).__init__()
        self.files = files
        self.path = path
        self.pattern = ptn
        self.upload = upld
        self.c70 = c70

    def make_deck(self):
        make_deck(self.files, self.path, self.pattern, self.upload, card70=self.c70)
        self.done.emit()


class Deck_Merger_Window(QDialog):
    def __init__(self, parent=None):
        super(Deck_Merger_Window, self).__init__(parent)

        header_style = "font: bold; background-color: #333;"

        self.pic = QPixmap()
        self.files = None

        self.hlayout = QHBoxLayout()
        self.layout = QVBoxLayout()
        self.hlayout.addLayout(self.layout)

        box = QHBoxLayout()

        self.lbl_header = QLabel("Input options:")
        self.lbl_header.setStyleSheet(header_style)
        self.layout.addWidget(self.lbl_header)
        self.layout.addSpacing(10)

        lbl = QLabel("Card images path")
        self.layout.addWidget(lbl)
        self.e_path = QLineEdit(parent)
        self.e_path.setText(os.path.curdir)
        lbl.setBuddy(self.e_path)
        box.addWidget(self.e_path)

        self.btn_path = QPushButton("Find")
        box.addWidget(self.btn_path)
        self.layout.addLayout(box)

        lbl = QLabel("Card images pattern (Deck will use all filenames that contain this)")
        self.layout.addWidget(lbl)

        self.e_pattern = QLineEdit(parent)
        self.e_pattern.setText(".png")
        lbl.setBuddy(self.e_pattern)
        self.layout.addWidget(self.e_pattern)
        self.btn_selectfiles = QPushButton("Optional: Select files manually")
        self.btn_selectfiles.clicked.connect(lambda: self.set_imagefiles())
        # self.layout.addWidget(self.btn_selectfiles)

        lbl = QLabel("Card 70 pattern (or click 'Find' to choose one)")
        self.layout.addWidget(lbl)

        box = QHBoxLayout()
        self.e_card70 = QLineEdit(parent)
        lbl.setBuddy(self.e_card70)
        self.e_card70.setText("70")
        self.e_card70.setReadOnly(True)
        box.addWidget(self.e_card70)

        self.btn_c70 = QPushButton("Find")
        self.btn_c70.clicked.connect(self.set_c70_path)
        box.addWidget(self.btn_c70)
        self.layout.addLayout(box)

        self.layout.addSpacing(20)

        # ## options
        optionbox = QHBoxLayout()

        lbl = QLabel("Save deck as:")
        self.e_deck_name = QLineEdit()
        self.e_deck_name.setText(DECK_IMAGE_NAME)
        lbl.setBuddy(self.e_deck_name)
        optionbox.addWidget(lbl)
        optionbox.addWidget(self.e_deck_name)

        self.chk_upload = QCheckBox("Upload to imgur")
        optionbox.addWidget(self.chk_upload)

        lbl = QLabel("Output options:")
        self.layout.addWidget(lbl)
        lbl.setStyleSheet(header_style)
        self.layout.addSpacing(10)
        self.layout.addLayout(optionbox)
        ## end options

        self.layout.addSpacing(20)

        self.btn_run = QPushButton("Run")
        self.layout.addWidget(self.btn_run)

        self.layout.addSpacing(10)

        lbl = QLabel("Messages:")
        self.layout.addWidget(lbl)
        #lbl.setStyleSheet("background-color: #034;")
        self.output = QTextEdit()
        #self.output.setText("\nLet's do this!\n")
        #self.output.setMaximumHeight(250)
        self.output.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addWidget(self.output)

        self.lbl_image = QLabel()
        self.lbl_image.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.lbl_image.hide()

        # layout done
        self.setLayout(self.hlayout)
        self.setGeometry(300, 100, 500, 500)

        self.hlayout.addWidget(self.lbl_image)

        self.setStyleSheet(default_style)

        self.writer = Writer(self, sys.stdout)
        sys.stdout = self.writer
        self.writer.writer.connect(self.write)

        self.btn_run.clicked.connect(self.run)
        self.btn_path.clicked.connect(self.path_opener)

        self.setWindowTitle('Tabletop Simulator deck merger by W0nk0')
        #self.show()

    def path_opener(self):
        dlg = QFileDialog(None, directory=self.path)
        dlg.setFileMode(QFileDialog.Directory)
        dlg.exec_()
        self.e_path.setText(dlg.selectedFiles()[0])
        # print dir(dlg)
        # print dlg.locals()

    def set_imagefiles(self, event=None):
        self.files = QFileDialog.getOpenFileNames(self)
        self.btn_selectfiles.setText("%d files selected manually instead of pattern" % len(self.files))

    def test(self):
        # self.write("Test write")
        # sys.stdout.write("print Test!")
        print "print!"

    def run(self):
        files = self.files or get_files(self.path, self.pattern)
        print("%d files!\n" % len(files))
        # for f in files:
        # print(f)
        print("Running make_deck(files, %s,%s)" % (self.path, self.pattern))
        self.wthread = QThread()
        global DECK_IMAGE_NAME
        DECK_IMAGE_NAME = os.path.abspath(os.path.curdir) + os.path.sep + self.e_deck_name.text()
        self.worker = DeckWorker(files, self.path, self.pattern, self.do_upload, self.e_card70.text())
        self.worker.moveToThread(self.wthread)
        self.wthread.started.connect(self.worker.make_deck)
        self.worker.done.connect(self.worker_done)
        self.wthread.start()
        self.btn_run.setText("Running..")
        self.btn_run.setEnabled(False)
        # missing exit and work done stuff, see http://stackoverflow.com/questions/11265812/pyside-pyqt-starting-a-cpu-intensive-thread-hangs-the-whole-application

    def worker_done(self):
        global DECK_IMAGE_NAME

        self.wthread.exit()
        print "\nDeck made and saved as %s!" % DECK_IMAGE_NAME
        # self.btn_run.clicked.disconnect()
        # self.btn_run.clicked.connect(lambda: self.open_deck_file(DECK_IMAGE_NAME))
        #self.btn_run.setText("Open deck file!")
        self.btn_run.setText("Run again")
        self.btn_run.setEnabled(True)

        lbl = self.lbl_image

        #p = QImage("_deck.jpg")
        #p.load("_deck.jpg")
        if not self.pic:
            self.pic = QPixmap()
        if self.pic.load(DECK_IMAGE_NAME):
            lbl.setMinimumWidth(200)
            lbl.setMinimumHeight(200)
            lbl.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            lbl.setPixmap(self.pic)
            lbl.setPixmap(self.pic.scaled(lbl.width(), lbl.height()))
            self.resizeEvent(None)
            self.refresh_pic()
        else:
            self.pic = None
            lbl.setText("Couldn't load preview, click here to open it.")
            print "Failed to load image {} into preview :(".format(DECK_IMAGE_NAME)
            lbl.setMinimumHeight(50)

        lbl.mouseReleaseEvent = lambda x: os.startfile(DECK_IMAGE_NAME)
        lbl.show()


    def resizeEvent(self, *args, **kwargs):
        super(Deck_Merger_Window, self).resizeEvent(*args, **kwargs)
        try:
            if not self.pic: return
            # self.lbl_image.setFixedHeight(self.lbl_image.width())
            # self.lbl_image.setMinimumHeight(self.width() - 15)
            #self.lbl_image.setFixedWidth(self.width()-15)
            self.refresh_pic()
        except:
            pass

    def set_c70_path(self):
        fn, ok = QFileDialog.getOpenFileName(self, 'Open Card 70 file', self.path)
        if ok:
            self.e_card70.setText(fn)

    def refresh_pic(self):
        if not self.pic: return
        lbl = self.lbl_image
        try:
            w = min(self.height() * 0.95 - 15, self.width() * 0.6 - 15)
            lbl.setPixmap(self.pic.scaled(w, w))
            lbl.setFixedWidth(w)
            lbl.setFixedHeight(w)
        except:
            lbl.setPixmap(self.pic)
            # raise

    @staticmethod
    def open_deck_file(filename):
        os.startfile(filename)

    @property
    def do_upload(self):
        return self.chk_upload.isChecked()

    @property
    def path(self):
        return self.e_path.text()

    @property
    def pattern(self):
        return self.e_pattern.text()

    def write(self, txt):
        # self.writer.write(txt)
        # print "write(",txt
        self.output.setPlainText(self.output.toPlainText() + "" + txt)
        o = self.output
        o.verticalScrollBar().setValue(o.verticalScrollBar().maximum())


def pyside_main():
    from sys import argv
    import sys

    tmpdir = os.environ["TEMP"] + os.sep
    sys.stderr = open(tmpdir + "deckmerge-err.log", "wt")

    app = QApplication(argv)
    # clipboard = app.clipboard()
    win = Deck_Merger_Window()

    # w = QMainWindow()
    #w.setCentralWidget(win)
    #w.show()

    win.show()

    try:
        sys.stdout = win.writer
    except:
        pass
    sys.exit(app.exec_())

if __name__ == "__main__":
    pyside_main()
