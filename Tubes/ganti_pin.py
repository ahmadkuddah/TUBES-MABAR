import pickle
from Data_Id import *

def ganti_pin():
    id = 1 #udah ada dari awal
    pin_lama = input("Masukkan PIN Lama: ")
    if pin_lama == nasabah[id]['pin']:
        pin_baru = input("Masukkan PIN Baru: ")

        print("PIN sudah terganti")
        nasabah[id]['pin'] = pin_baru

        pickle.dump(nasabah, open("nasabah.dat", "wb"))
    else:
        print("PIN-mu salah ngab!!")
        ganti_pin()

ganti_pin()