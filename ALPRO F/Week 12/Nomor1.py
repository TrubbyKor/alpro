from PyQt5.QtWidgets import *
import sys

app = QApplication([])

window = QMainWindow()
window.setGeometry(500, 300, 600, 400)
window.setWindowTitle("NOMOR 1")

label_nama = QLabel("Nama Barang:", window)
label_nama.setFixedWidth(100)
label_nama.move(20, 20)  

ledit_nama = QLineEdit(window)
ledit_nama.setToolTip("Masukkan nama barang")
ledit_nama.move(150, 20)  
ledit_nama.setFixedWidth(200)

label_harga = QLabel("Harga Barang:", window)
label_harga.setFixedWidth(100)
label_harga.move(20, 60)  

ledit_harga = QLineEdit(window)
ledit_harga.setToolTip("Masukkan harga barang")
ledit_harga.move(150, 60)  
ledit_harga.setFixedWidth(200)

tombol_tambah = QPushButton("Tambah", window)
tombol_tambah.move(150, 100)  

tabel_barang = QTableWidget(window)
tabel_barang.setColumnCount(2)
tabel_barang.setHorizontalHeaderLabels(["Nama Barang", "Harga"])
tabel_barang.setGeometry(20, 150, 550, 200) 

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