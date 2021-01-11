
from Model.daftar_nilai import tambah, ubah, hapus, cari
from view.view_nilai import cetak_daftar_nilai


def menu():
    print("\n")
    print("=========== MENU ==============")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("5. Cari Data")


    menu = int (input("Masukkan pilihan dalam angka => "))

    if (menu == 1):
        tambah()
    elif (menu == 2):
        cetak_daftar_nilai()
    elif (menu == 3):
        ubah()
    elif (menu == 4):
        hapus()
    elif (menu == 5):
        cari()
    else:
        print("ANDA SALAH MEMASUKKAN PILIHAN !!!")
while (True):
    menu()

