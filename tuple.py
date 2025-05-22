import traceback

print("1. Cara Membuat Tuple di Python")
t = (1234, 4321, 'Hello')
print(t)
u = 1234, 4321, 'Hello'
print(u)

print("\n2. Membuat Tuple Kosong dan Singleton")
kosong = ()
satu = ('Isinya',)
siji = "isinya siji",
print(kosong, satu, siji)

print("\n3. Mengakses Nilai Tuple")
nama = ('petani', 'kode', 'linux')
print(nama[1])

try:
    nama[0] = 'coding'
except TypeError as error:
    traceback.print_tb(error.__traceback__)

print("\n4. Memotong Tuple")
web = (123, 'Petani Kode', 'https://www.petanikode.com')
print(web[1:2])
print(web[1:3])
print(web[1:])
print(web[:2])
print(web[:])
print(web)
print(web[:] == web)

print("\n5. Mengambil Panjang Tuple")
hari = ('Senin', 'Selasa', 'Rabu', 'Kamis', "Jum'at", 'Sabtu', 'Minggu')
print(f"Jumlah hari: {len(hari)}")

print("\n6. Tuple Nested")
tuple1 = "aku", "cinta", "kamu"
tuple2 = "selama", 3, "tahun"
tuple3 = tuple1, tuple2
print(tuple3)
t = ([1,2,3], {'nama': 'Petani Kode', 'rank': 123}, True)
print(t)

print("\n7. Sequence Unpacking")
web = 123, "Petani Kode", "https://www.petanikode.com"
id_web, nama, url = web
print(id_web)
print(nama)
print(url)
