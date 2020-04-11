import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication


print(sys.argv)
app = QApplication(sys.argv)

web = QWebEngineView()
src = sys.argv[1]
url = "http://www.tamilradios.com/embed/index.php?src={}"
web.load(QUrl(url.format(src)))

web.show()

sys.exit(app.exec_())
