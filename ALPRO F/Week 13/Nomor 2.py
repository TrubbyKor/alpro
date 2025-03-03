import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class Kalkulator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Kalkulator Sederhana')

        # Layout utama
        layout = QVBoxLayout()

        # Input angka
        self.angka1 = QLineEdit(self)
        self.angka2 = QLineEdit(self)
        self.hasil = QLineEdit(self)
        self.hasil.setReadOnly(True)

        # Label
        layout.addWidget(QLabel('Angka 1:'))
        layout.addWidget(self.angka1)
        layout.addWidget(QLabel('Angka 2:'))
        layout.addWidget(self.angka2)
        layout.addWidget(QLabel('Hasil:'))
        layout.addWidget(self.hasil)

        # Tombol operasi
        button_layout = QHBoxLayout()
        button_layout.addWidget(QPushButton('Penjumlahan', self, clicked=self.penjumlahan))
        button_layout.addWidget(QPushButton('Pengurangan', self, clicked=self.pengurangan))
        button_layout.addWidget(QPushButton('Perkalian', self, clicked=self.perkalian))
        button_layout.addWidget(QPushButton('Pembagian', self, clicked=self.pembagian))
        button_layout.addWidget(QPushButton('Pangkat', self, clicked=self.pangkat))
        button_layout.addWidget(QPushButton('Modulus', self, clicked=self.modulus))

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def penjumlahan(self):
        self.hitung(lambda x, y: x + y)

    def pengurangan(self):
        self.hitung(lambda x, y: x - y)

    def perkalian(self):
        self.hitung(lambda x, y: x * y)

    def pembagian(self):
        self.hitung(lambda x, y: x / y if y != 0 else "Error: Pembagian dengan nol")

    def pangkat(self):
        self.hitung(lambda x, y: x ** y)

    def modulus(self):
        self.hitung(lambda x, y: x % y)

    def hitung(self, operasi):
        try:
            a = float(self.angka1.text())
            b = float(self.angka2.text())
            hasil = operasi(a, b)
            self.hasil.setText(str(hasil))
        except ValueError:
            self.hasil.setText("Error: Input tidak valid")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    kalkulator = Kalkulator()
    kalkulator.resize(400, 200)
    kalkulator.show()
    sys.exit(app.exec_())