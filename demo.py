# modified from https://raw.githubusercontent.com/wbsoft/python-poppler-qt4/master/demo.py

import sys
from PySide import QtGui, QtCore
import poppler

usage = """
Demo to load a PDF and display the first page.

Usage:

    python demo.py file.pdf

"""


def pdf_view(filename):
    """Return a Scrollarea showing the first page of the specified PDF file."""

    label = QtGui.QLabel()

    doc = poppler.Poppler.Document.load(filename)
    # doc.setRenderHint(poppler.Poppler.Document.Antialiasing)
    # doc.setRenderHint(poppler.Poppler.Document.TextAntialiasing)

    page = doc.page(0)
    image = page.renderToImage()

    label.setPixmap(QtGui.QPixmap.fromImage(image))

    area = QtGui.QScrollArea()
    area.setWidget(label)
    area.setWindowTitle(filename)
    return area


def main():
    app = QtGui.QApplication(sys.argv)
    argv = QtGui.QApplication.arguments()
    if len(argv) < 2:
        sys.stderr.write(usage)
        sys.exit(2)

    filename = argv[-1]
    view = pdf_view(filename)
    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
