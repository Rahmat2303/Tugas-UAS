
from view.input_nilai import input_data
from view.view_nilai import cetak_daftar_nilai

data_mahasiswa = []

# Menambah data
def tambah():
    input_data()

# Mengubah data
def ubah():
    tambah()

# Menghapus data
def hapus():
    data.clear()
    print("Data berhasil di hapus !")

# Cari data
def cari(nim):
    mencari_data = input("Masukkan NIM : ")
    if mencari_data == nim:
        cetak_daftar_nilai()