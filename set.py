print("1. Cara Membuat Set di Python")
t = {1234, 4321, 'Hello', 4321}
print(t)

print("\n2. Membuat Set Kosong dan Singleton")
kosong = set()
satu = {'Isinya'}
print(kosong, satu)

print("\n3. Pengecekan Element di Set")
nama = {'petani', 'kode', 'linux'}
print("kode" in nama)
print("dukuh" in nama)


print("\n4. Tambah dan kurang Element di Set")
nama.add("nelayan")
print(nama)

nama.remove("linux")
print(nama)

print("\n5. Mengambil Panjang Set")
hari = {'Senin', 'Selasa', 'Rabu', 'Kamis', "Jum'at", 'Sabtu', 'Minggu'}
print(f"Jumlah hari: {len(hari)}")

print("\n6. Tuple Nested")
set1 = {"aku", "cinta", "kamu"}
set2 = {"selama", 3, "tahun"}
set3 = set1, set2
print(set3)

import traceback

try:
    t = {[1,2,3,3], {'nama': 'Petani Kode', 'rank': 123}, True}
except TypeError as error:
    traceback.print_tb(error.__traceback__)

u = {
    (1,2,3,3),
    tuple({'nama': 'Petani Kode', 'rank': 123}.items()),
    True
}
print(u)

print("\n7. Set Unpacking Not In Order")
web = {123, "Petani Kode", "https://www.petanikode.com"}
c, a, b = web
print(a)
print(b)
print(c)
