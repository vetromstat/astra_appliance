import sys
from pathlib import Path
                  
from PyQt5.QtWidgets import QFileSystemModel,QTreeView,QHBoxLayout,QLabel,QApplication
from PyQt5.QtWidgets import QWidget, QVBoxLayout,QSizePolicy,QLineEdit
from PyQt5.QtCore import QDir



class App(QWidget):
    def __init__(self):
        super().__init__()  

        self.vertical_layout = QVBoxLayout(self)         #Layot ы для компоновки элементов 
        self.horizontal_layout = QHBoxLayout(self)                   

        self.lbl = QLabel("Найти ")                                
        self.line_edit = QLineEdit()

        self.horizontal_layout.addWidget(self.lbl)              #добавление label и line edit в верхний горизонтальный Layout
        self.horizontal_layout.addWidget(self.line_edit)
        
        dir = str(Path.home())                              #определение стартовой директории текущего пользователя
        self.model = QFileSystemModel()
        self.model.setFilter(QDir.AllEntries | QDir.NoDotAndDotDot | QDir.Hidden)      #отображение всех файлов, в том числе скрытых(кросс-платформенно)
        self.model.setNameFilterDisables(False)    #есл определить true при поиске элемента, найденный элемент будет выделяться цветом, но оставшиеся все равно будут отображаться       
        self.tree = QTreeView()
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)  #опредение size policy для того чтобы верхний layout не занимал полэкрана
        self.tree.setSizePolicy(sizePolicy)
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.setRootPath(dir)) #устнавовка стартовой директории
        self.tree.setSortingEnabled(True)       #Включение сортировок по столбцам

        self.vertical_layout.addLayout(self.horizontal_layout)  #компановка в общий вертикальный layout
        self.vertical_layout.addWidget(self.tree)

        self.line_edit.textChanged.connect(self.TextChanged)    #присоединение функции к сигналу об изменении текста в line edit


    def TextChanged(self):
        if self.line_edit.text() != "":         #условие для того чтобы когда line edit стирают фильтры сбрасывались
            self.model.setNameFilters(["*"+self.line_edit.text()+"*"]) #поиска включений строки в имена файлов и папок
        else:
            self.model.setNameFilters([])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.resize(640, 480)                
    window.show()                            
    sys.exit(app.exec())