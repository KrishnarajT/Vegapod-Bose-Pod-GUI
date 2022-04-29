# import sys
# import urllib

# from PyQt5 import QtCore, QtGui


# class DownloadThread(QtCore.QThread):

#     data_downloaded = QtCore.pyqtSignal(object)

#     def __init__(self, parent):
#         QtCore.QThread.__init__(self, parent)
#         self.url = url

#     def run(self):
#         info = urllib2.urlopen(self.url).info()
#         self.data_downloaded.emit('%s\n%s' % (self.url, info))


# class MainWindow(QtGui.QWidget):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.list_widget = QtGui.QListWidget()
#         self.button = QtGui.QPushButton("Start")
#         self.button.clicked.connect(self.start_download)
#         layout = QtGui.QVBoxLayout()
#         layout.addWidget(self.button)
#         layout.addWidget(self.list_widget)
#         self.setLayout(layout)

#     def start_download(self):
#         urls = ['http://google.com', 'http://twitter.com', 'http://yandex.ru',
#                 'http://stackoverflow.com/', 'http://www.youtube.com/']
#         self.threads = []
#         for url in urls:
#             downloader = DownloadThread(url)
#             downloader.data_downloaded.connect(self.on_data_ready)
#             self.threads.append(downloader)
#             downloader.sdef __init__(self):
# 	work over here...
# 	self.Button.clicked.connect(self.another_function) #Here we call the function over the action
	
# 	self threadingFunction(self, args):
# 		Do your stuff..
# 		change UI or load big files 
# 		Another stuff..

# 	self another_function(self):
# 		do things
# 	threadingFunction
# 	t = Thread(target=threadingFunction,your args and needs...) #Here you are calling the thread to avoid killing the UI
# 	t.start()tart()

#     def on_data_ready(self, data):
#         print (data)
#         self.list_widget.addItem(unicode(data))


# if __name__ == "__main__":
#     app = QtGui.QApplication(sys.argv)
#     window = MainWindow()
#     window.resize(640, 480)
#     window.show()
#     sys.exit(app.exec_())


# def __init__(self):
#     	work over here...
# 	self.Button.clicked.connect(self.another_function) #Here we call the function over the action
	
# 	self threadingFunction(self, args):
# 		Do your stuff..
# 		change UI or load big files 
# 		Another stuff..

# 	self another_function(self):
# 		do things
# 	threadingFunction
# 	t = Thread(target=threadingFunction,your args and needs...) #Here you are calling the thread to avoid killing the UI
# 	t.start()