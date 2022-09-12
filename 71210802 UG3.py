a = input("Masukan Kalimat Anda : ")
b = input("Masukkan Kata yang Anda Cari : ")

a = a.split()

jumlah = 0

for i in a : 
    if i == b : 
        jumlah += 1

print(jumlah)