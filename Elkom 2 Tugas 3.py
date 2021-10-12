# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:16:49 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")   

P = int(input("Ketik total belanjaan: Rp."))
Q= int(input("Ketik uang yang diserahkan: Rp."))
kembalian = Q-P

print("Uang kembalian: Rp.",kembalian)
print("Uang pecahan yang dibutuhkan: ")
Uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 1]
Jumlah_pecahan = {}
Sisa = kembalian

if (Q < P):
    print("Error: Uang yang diberikan kurang")
elif (P == Q):
    print("Tidak ada uang kembalian")
    
for pecahan in Uang_pecahan:
    if Sisa < pecahan:
        continue
    Banyak_pecahan = int(Sisa / pecahan)
    Sisa = Sisa - ( pecahan * Banyak_pecahan )
    print('pecahan {} : {}'.format(pecahan, Banyak_pecahan))