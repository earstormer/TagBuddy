from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
import Interface
import sys
import TagQuerry
import webbrowser

def main():
    class MainDialog(QMainWindow, Interface.Ui_MainWindow):
        def __init__(self, parent=None):
            super(MainDialog, self).__init__(parent)
            self.setupUi(self)
            self.setFixedSize(451, 474)

            self.hashtagSearch.clicked.connect(self.tagSearch)
            self.browserOpen.clicked.connect(self.browserNav)
            self.addButton.clicked.connect(self.addToTextbox)
            self.listLow.clicked.connect(self.lowCompSelection)
            self.listMed.clicked.connect(self.medCompSelection)
            self.listHigh.clicked.connect(self.highCompSelection)

            self.browserOpen.setEnabled(False)
            self.addButton.setEnabled(False)

            self.tagSearchObject = None
            self.list = None
            self.lowSelectedTag = None
            self.medSelectedTag = None
            self.highSelectedTag = None
            self.tagHighlight = None

        def tagSearch(self):
            self.listLow.clear()
            self.listMed.clear()
            self.listHigh.clear()
            self.browserOpen.setEnabled(True)
            self.addButton.setEnabled(True)

            self.tagSearchObject = TagQuerry.instaTag()
            searchedText = self.hashtagText.text()
            self.tagSearchObject.tagQuery(tag=searchedText)
            self.list = self.tagSearchObject.compList

            for item in self.list:
                if item[0] == 'Low':
                    self.listLow.addItem(QListWidgetItem(item[1]))
                elif item[0] == 'Medium':
                    self.listMed.addItem(QListWidgetItem(item[1]))
                elif item[0] == 'High':
                    self.listHigh.addItem(QListWidgetItem(item[1]))

        def addToTextbox(self):
            self.plainTextTags.insertPlainText("#" + self.tagHighlight + " ")

        def lowCompSelection(self):
            self.tagHighlight = None
            self.lowSelectedTag = None
            self.lowSelectedTag = self.listLow.currentItem().text()
            self.tagHighlight = self.listLow.currentItem().text()
            self.updateTagInfo()

        def medCompSelection(self):
            self.tagHighlight = None
            self.medSelectedTag = None
            self.medSelectedTag = self.listMed.currentItem().text()
            self.tagHighlight = self.listMed.currentItem().text()
            self.updateTagInfo()

        def highCompSelection(self):
            self.tagHighlight = None
            self.highSelectedTag = None
            self.highSelectedTag = self.listHigh.currentItem().text()
            self.tagHighlight = self.listHigh.currentItem().text()
            self.updateTagInfo()

        def updateTagInfo(self):
            for item in self.list:
                if item[1] == self.tagHighlight:
                    numbF = f'{int(item[2]):,}'
                    self.tagLbl.setText(self.tagHighlight)
                    self.tagLblNum.setText(numbF)
                    self.tagLblCmp.setText(item[0])

        def browserNav(self):
            url = 'https://www.instagram.com/explore/tags/' + self.tagHighlight
            webbrowser.open_new_tab(url)

    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    QApplication.processEvents()
    app.exec_()

if __name__ == "__main__":
    main()