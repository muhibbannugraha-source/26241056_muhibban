#input output
#nama = input("masukan nama anda:")
#nim = input("masukan nim anda:")
#alamat = input("masukan alamat anda:")

#print("========output========")

#print("nama anda :",nama)
#print("nim anda :",nim)
#print("alamat anda :",alamat)

#tipe data interger, bilangan bulat
#a = 10
#print("nilai a :", a)
#print("tipe data a :", type(a))

# tipe data string, tulisan
#b = "f"
#print("nilai b :", b)
#print("tipe data b :", type(b))

# tipe data float, bilangan pecahan
#c = 10.5
#print("nilai c :", c)
#print("tipe data c :", type(c))

# tipe data bolean
#d = True
#print("nilai d :", d)
#print("tipe data d :", type(d))

#pertemuan 3.py
# ================================
#      IDENTITAS MAHASISWA
# ================================

# Meminta input dari pengguna
nama = input("Masukkan Nama Mahasiswa : ")
nim = int(input("Masukkan NIM : "))
prodi = input("Masukkan Program Studi : ")
dua_digit_nim = int(input("Masukkan 2 Digit Terakhir NIM : "))

# ================================
#        HASIL PROGRAM
# ================================
print("================================")
print("      IDENTITAS MAHASISWA")
print("================================")
print("        HASIL PROGRAM")
print("================================")

print(f"Nama         : {nama}")
print(f"NIM          : {nim}")
print(f"Prodi        : {prodi}")
print(f"2 Digit NIM  : {dua_digit_nim}\n")

print(f"Tipe Data Nama        : {type(nama)}")
print(f"Tipe Data NIM         : {type(nim)}")
print(f"Tipe Data Prodi       : {type(prodi)}")
print(f"Tipe Data 2 Digit NIM : {type(dua_digit_nim)}")
print("================================")