import os
import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QResizeEvent
from PySide6.QtWidgets import QApplication, QMainWindow

from image_generator import create_images
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("AI image generator")
        self.setMinimumSize(400, 300)  # Define o tamanho mínimo da janela
        self.setMaximumSize(900, 680)

        self.image_folder = 'images'
        self.current_img_index = 0
        self.image_files = [f for f in os.listdir(
            self.image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        self.right_btn.clicked.connect(self.change_image)
        self.btn_generate.clicked.connect(self.create_img)
        self.update_image()

    def create_img(self):
        text = self.txt_description.text()
        image = create_images(text, self.txt_name_file.text())
        self.img_lbl.setPixmap(image)

    def change_image(self):
        if self.image_files:
            self.current_img_index = (
                self.current_img_index + 1) % len(self.image_files)
            self.update_image()

    def update_image(self):
        if self.image_files:
            image_path = os.path.join(
                self.image_folder, self.image_files[self.current_img_index])
            pixmap = QPixmap(image_path)
            self.img_lbl.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    app.exec()
