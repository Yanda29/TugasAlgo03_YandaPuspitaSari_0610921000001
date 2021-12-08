# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 07:11:08 2021

@author: Yanda Puspita Sari
"""
import sys

def main():
    print("Daftar Hotkey\nj->Jabodetabek\ndj->Pulau Jawa\nlj->Luar Jawab")
    tujuan= bacavalidinput1("Tujuan Barang(q-quit)= ")
    berat = bacavalidinput2("Masukan Berat Barang = ")
def baner():
    print("PROGRAM MENGHITUNG BIAYA PENGIRIMAN")

def bacavalidinput1(s):
    while True:
        global tujuan
        global harga
        tujuan=input(s)    
        if tujuan == "j":
            print("Jabodetabek")
            harga=10000
            break
        elif tujuan=="q":
            sys.exit(0)
        elif tujuan == "dj":
            print("Dalam Pulau Jawa")
            harga=25000
            break
        elif tujuan == "lj":
            print("Luar pulau Jawa")
            harga=50000
            break
    return harga    
def bacavalidinput2(s):
    while True:
        global berat
        global harga1
        berat=int(input(s))
        if berat >0 and berat <= 20:
            harga1 = 15000
            break
        elif berat > 20:
            harga1 = 15000 +((berat-20)*1500)
            break
    return harga1,berat
def Rincian():
    print("xxxxxxxxxxxxxxx Rincian Biaya xxxxxxxxxxxxxxx")
    print(f'1.tujuan  = {tujuan}                 Rp.{harga}')
    print(f'2.Berat   = {berat}kg               Rp.{harga1}')
    print(f'3.PPN 10% =                    Rp.{int((harga+harga1)*(10/100))}')
    print(f'4.Total   =                    Rp.{int(harga+harga1+(harga+harga1)*(10/100))}')
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
if __name__ == '__main__':
    baner()
    main()
    Rincian()
