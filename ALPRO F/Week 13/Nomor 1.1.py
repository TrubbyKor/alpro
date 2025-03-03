from PyQt5.QtWidgets import *
import sys

app = QApplication([])

window = QMainWindow()
window.setGeometry(500, 300, 600, 400)
window.setWindowTitle("NOMOR 1")

# Widget utama
central_widget = QWidget()
window.setCentralWidget(central_widget)

# Layout
layout = QGridLayout(central_widget)

label_nama = QLabel("Nama Barang:")
layout.addWidget(label_nama, 0, 0)

ledit_nama = QLineEdit()
ledit_nama.setToolTip("Masukkan nama barang")
layout.addWidget(ledit_nama, 0, 1)

label_harga = QLabel("Harga Barang:")
layout.addWidget(label_harga, 1, 0)

ledit_harga = QLineEdit()
ledit_harga.setToolTip("Masukkan harga barang")
layout.addWidget(ledit_harga, 1, 1)

tombol_tambah = QPushButton("Tambah")
layout.addWidget(tombol_tambah, 2, 1)

tabel_barang = QTableWidget()
tabel_barang.setColumnCount(2)
tabel_barang.setHorizontalHeaderLabels(["Nama Barang", "Harga"])
layout.addWidget(tabel_barang, 3, 0, 1, 2)  # Menggunakan 2 kolom untuk tabel

def tambah_data():
    nama_barang = ledit_nama.text()
    harga_barang = ledit_harga.text()
    
    if not nama_barang or not harga_barang:
        QMessageBox.warning(window, "Peringatan", "Nama dan Harga barang harus diisi")
    elif not harga_barang.isdigit():
        QMessageBox.warning(window, "Peringatan", "Harga barang harus berupa angka")
    else:
        row_position = tabel_barang.rowCount()
        tabel_barang.insertRow(row_position)
        tabel_barang.setItem(row_position, 0, QTableWidgetItem(nama_barang))
        tabel_barang.setItem(row_position, 1, QTableWidgetItem(harga_barang))

        ledit_nama.clear()
        ledit_harga.clear()

tombol_tambah.clicked.connect(tambah_data)

window.show()
sys.exit(app.exec_())