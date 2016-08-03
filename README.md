#Dependencies

    apt-get install libpyside1.2 libpyside-dev libpoppler-qt4-4 libpoppler-qt4-dev shiboken libshiboken-dev

#Installation

	mkdir build
	cd build
	cmake ..
	make
	sudo make install


#Usage

	from pyside_poppler import Poppler as QtPoppler

#Troubleshooting
	if you get error like "ImportError: dynamic module does not define init function (initpyside_poppler)", check PythonLibs in cmake message.

#Reference

	http://qt-devnet.developpez.com/tutoriels/python/pyside/binding-shiboken/

	http://pyside.github.io/docs/api-extractor/typesystem.html

	https://people.freedesktop.org/~aacid/docs/qt4/poppler-qt4_8h_source.html
