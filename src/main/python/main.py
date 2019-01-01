from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QMenu, QAction
from PyQt5.QtGui import QIcon

import sys


def get_translation(modname, dirname=None):

    def translate_dumb(x):
        """Dumb function to not use translations."""
        #if not is_unicode(x):
        #    return to_text_string(x, "utf-8")
        return x

    return translate_dumb


# Translation callback
_ = get_translation('lftool')



class lftMainWindow(QMainWindow):
    def __init__(self, appctxt):
        QMainWindow.__init__(self)
        self._appctxt = appctxt

        version = self._appctxt.build_settings['version']
        self.setWindowTitle("lftool v" + version)
        self.resize(250, 150)

        # menubar = QMenuBar(self)
        # menuFile = QMenu(self)
        # m_file_open = QAction(self)
        # m_file_open.setText('Open')
        # m_file_open.setShortcut('Ctrl+Q')
        # menuFile.addAction(m_file_open)
        # self.setMenuBar(menubar)


        self.file_menu = self.menuBar().addMenu(_("&File"))
        self.edit_menu = self.menuBar().addMenu(_("&Edit"))
        self.tools_menu = self.menuBar().addMenu(_("&Tools"))


        newButton  = QAction('&New File', self)
        newButton.setShortcut('Crtl+N')
        openButton  = QAction('&Open File', self)
        openButton.setShortcut('Crtl+O')
        saveButton = QAction('&Save', self)
        saveButton.setShortcut('Crtl+S')
        saveAsButton = QAction('Save &As', self)
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        self.file_menu.addAction(newButton)
        self.file_menu.addAction(openButton)
        self.file_menu.addAction(saveButton)
        self.file_menu.addAction(saveAsButton)
        self.file_menu.addAction(exitButton)


class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext
    def run(self):                              # 2. Implement run()
        #window = QMainWindow()
        #version = self.build_settings['version']
        #window.setWindowTitle("lftool v" + version)
        #window.resize(250, 150)
        window = lftMainWindow(self)
        window.show()
        #window.raise_()
        return self.app.exec_()                 # 3. End run() with this line

if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)
