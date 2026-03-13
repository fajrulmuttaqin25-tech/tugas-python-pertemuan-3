# 1. Menghitung jumlah baris dalam file
def hitung_baris(nama_file):
    jumlah = 0
    with open(nama_file, "r") as file:
        for baris in file:
            jumlah += 1
    return jumlah
# membuat file jika belum ada
with open("data.txt", "a") as file:
    pass

print("Jumlah baris:", hitung_baris("data.txt"))

# 2. Menulis daftar nama ke file dipisahkan koma
def tulis_nama(nama_list, nama_file):
    with open(nama_file, "w") as file:
        file.write(",".join(nama_list))

# daftar nama
nama = ["Fajrul", "Reza", "Fathur", "Melann"]
tulis_nama(nama, "nama.txt")

# 3. Menambahkan catatan baru dan menampilkan semua catatan
catatan = input("Masukkan catatan baru: ")

with open("catatan.txt", "a") as file:
    file.write(catatan + "\n")

print("Daftar catatan:")
with open("catatan.txt", "r") as file:
    print(file.read())
   
# 4. Mencari nama dalam file 
def cari_nama(nama_file, nama_cari):
    with open(nama_file, "r") as file:
        for baris in file:
            if nama_cari in baris:
                print("Data ditemukan:", baris.strip())

# contoh penggunaan
cari_nama("nama.txt", "Fajrul")