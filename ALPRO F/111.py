from PyQt5.QtWidgets import *
import sys

class InvestasiApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Mengatur ukuran jendela yang lebih besar
        self.setFixedSize(500, 400)  # Ukuran tetap
        self.setWindowTitle("Penghitung Investasi")

        # Membuat widget
        self.label_investasi = QLabel("Jumlah Investasi:", self)
        self.label_bunga = QLabel("Suku Bunga %:", self)
        self.label_jangka_waktu = QLabel("Jangka Waktu (tahun):", self)
        self.label_hasil = QLabel("", self)

        self.ledit_investasi = QLineEdit(self)
        self.ledit_bunga = QLineEdit(self)
        self.ledit_jangka_waktu = QLineEdit(self)

        self.button_hitung = QPushButton("Hitung", self)
        self.button_reset = QPushButton("Reset", self)

        # Mengatur posisi setiap widget secara absolut
        self.label_investasi.move(20, 20)
        self.ledit_investasi.move(180, 20)
        self.ledit_investasi.resize(200, 25)  # Atur ukuran line edit

        self.label_bunga.move(20, 60)
        self.ledit_bunga.move(180, 60)
        self.ledit_bunga.resize(200, 25)  # Atur ukuran line edit

        self.label_jangka_waktu.move(20, 100)
        self.ledit_jangka_waktu.move(180, 100)
        self.ledit_jangka_waktu.resize(200, 25)  # Atur ukuran line edit

        self.button_hitung.move(100, 140)  # Pindahkan tombol hitung
        self.button_reset.move(220, 140)   # Pindahkan tombol reset

        self.label_hasil.move(20, 180)
        self.label_hasil.resize(400, 100)  # Atur ukuran label hasil

        # Menghubungkan tombol ke fungsi
        self.button_hitung.clicked.connect(self.hitung_investasi)
        self.button_reset.clicked.connect(self.reset_input)

    def hitung_investasi(self):
        try:
            # Mengambil nilai dari input
            investasi_awal = float(self.ledit_investasi.text())
            suku_bunga = float(self.ledit_bunga.text())
            jangka_waktu = int(self.ledit_jangka_waktu.text())

            # Validasi input
            if investasi_awal <= 0 or suku_bunga < 0 or jangka_waktu <= 0:
                raise ValueError("Nilai harus positif.")

            # Menghitung nilai akhir investasi
            nilai_akhir = investasi_awal * ((1 + suku_bunga / 100) ** jangka_waktu)
            total_bunga = nilai_akhir - investasi_awal

            # Menampilkan hasil
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