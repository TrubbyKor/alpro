from PyQt5.QtWidgets import *
import sys

class InvestasiApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(500, 400) 
        self.setWindowTitle("NOMOR 2")

        # Buat widget pusat dan layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.label_investasi = QLabel("Jumlah Investasi:", self)
        self.label_bunga = QLabel("Suku Bunga %:", self)
        self.label_jangka_waktu = QLabel("Jangka Waktu :", self)
        self.label_hasil = QLabel("", self)

        self.ledit_investasi = QLineEdit(self)
        self.ledit_bunga = QLineEdit(self)
        self.ledit_jangka_waktu = QLineEdit(self)

        self.button_hitung = QPushButton("Hitung", self)
        self.button_reset = QPushButton("Reset", self)

        # Tambahkan widget ke layout
        self.layout.addWidget(self.label_investasi)
        self.layout.addWidget(self.ledit_investasi)

        self.layout.addWidget(self.label_bunga)
        self.layout.addWidget(self.ledit_bunga)

        self.layout.addWidget(self.label_jangka_waktu)
        self.layout.addWidget(self.ledit_jangka_waktu)

        self.layout.addWidget(self.button_hitung)
        self.layout.addWidget(self.button_reset)

        self.layout.addWidget(self.label_hasil)

        # Hubungkan sinyal ke slot
        self.button_hitung.clicked.connect(self.hitung_investasi)
        self.button_reset.clicked.connect(self.reset_input)

    def hitung_investasi(self):
        try:
            investasi_awal = float(self.ledit_investasi.text())
            suku_bunga = float(self.ledit_bunga.text())
            jangka_waktu = int(self.ledit_jangka_waktu.text())

            if investasi_awal <= 0 or suku_bunga < 0 or jangka_waktu <= 0:
                raise ValueError("Nilai harus positif.")

            nilai_akhir = investasi_awal * ((1 + suku_bunga / 100) ** jangka_waktu)
            total_bunga = nilai_akhir - investasi_awal

            self.label_hasil.setText(f"Nilai Investasi Akhir: {nilai_akhir:.2f}\nTotal Bunga: {total_bunga:.2f}")
        except ValueError as e:
            QMessageBox.warning(self, "Input Error", str(e))

    def reset_input(self):
        self.ledit_investasi.clear()
        self.ledit_bunga.clear()
        self.ledit_jangka_waktu.clear()
        self.label_hasil.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InvestasiApp()
    window.show()
    sys.exit(app.exec_())