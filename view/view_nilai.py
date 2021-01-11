
from Model.daftar_nilai import data_mahasiswa


def cetak_daftar_nilai():
    for raw in data_mahasiswa:
        print("Nama     : ", raw["nama"])
        print("NIM      : ", raw["nim"])
        print("Nilai UTS    : ", raw["nilai_uts"])
        print("Nilai UAS    : ", raw["nilai_uas"])
        print("==============================")
