from model.daftar_nilai import *
from view.view_nilai import *

#Mulai
print("===========================================")
print("               PROGRAM 1                   ")
print("NAMA         : TIARA PUTRI                 ")
print("NIM          : 312210064                   ")
print("KELAS        : TI.22.A1                    ")
print("===========================================")

while True:
    print("\n")
    menu = input("(L) Lihat, (T) Tambah, (H) Hapus, (U) Ubah, (C) Cari, (K) Keluar\nPilih menu: ")
    print("\n")

    # menu
    if menu.lower() == 't':
        tambah_data()

    elif menu.lower() == 'c':
        cari_data()

    elif menu.lower() == 'l':
        lihat_data()

    elif menu.lower() == 'u':
        ubah_data()

    elif menu.lower() == 'h':
        hapus_data()

    # Keluar
    elif menu.lower() == 'k':
        break

    else:
        print("Ada yang salah, silahkan cek kembali.")