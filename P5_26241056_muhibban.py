# 1. Meminta input dari pengguna
nama = input("Nama mahasiswa : ")
nim_lengkap = input("NIM lengkap    : ")
digit_a = int(input("Digit A        : "))
digit_b = int(input("Digit B        : "))

# 2. Menampilkan hasil perbandingan keenam operator komparasi
print("\n===== HASIL PERBANDINGAN =====")
print(f"A > B  : {digit_a > digit_b}")
print(f"A < B  : {digit_a < digit_b}")
print(f"A == B : {digit_a == digit_b}")
print(f"A != B : {digit_a != digit_b}")
print(f"A >= B : {digit_a >= digit_b}")
print(f"A <= B : {digit_a <= digit_b}")