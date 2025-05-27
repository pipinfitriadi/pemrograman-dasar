import traceback

print("1. Apa itu Dictionary pada Python?")
aku = {
    "nama": "Petani Kode",
    "url": "https://www.petanikode.com"
}
print(aku)
print(aku["nama"])
print(aku["url"])

try:
    print(aku["alamat"])
except KeyError as error:
    traceback.print_tb(error.__traceback__)

print({(1,2): "tes"})  # Key itu harus immutable: str, int, float, bool, tuple

print("\n2. Membuat Dictionary")
value = True
key3 = "key3"
nama_dict = {
    "key1": value,
    "key2": "value",
    key3: "value"
}
print(nama_dict)
pak_tani = {
    "nama": "Petani Kode",
    "umur": 22,
    "hobi": ["coding", "membaca", "cocok tanam"],
    "menikah": False,
    "sosmed": {
        "facebook": "petanikode",
        "twitter": "@petanikode"
    } 
}
print(pak_tani)
warna_buah = dict(jeruk="orange", apel="merah", pisang="kuning")
print(warna_buah)

print("\n3. Mengakses Nilai Item dari Dictionary")
print(f"Nama saya adalah {pak_tani['nama']}")
print(f'Twitter: {pak_tani["sosmed"]["twitter"]}')
print(f"Hobi ke-2: {pak_tani["hobi"][1]}")
print(pak_tani.get("nama"))

try:
    print(pak_tani["alamat"])
except KeyError as error:
    traceback.print_tb(error.__traceback__)

print(pak_tani.get("alamat"))

print("\nMenggunakan Perulangan")
web = {
    "name": "petanikode",
    "url": "https://www.petanikode.com",
    "rank": "5"
}

for key in web:
    print(web[key])

for key, val in web.items():
    print(f"{key}: {val}")

print("\n4. Mengubah Nilai Item Dictionary")
print(web)
web["rank"] = '3'
print(web)

print("\n5. Menghapus Item dari Dictionary")
skill = {
    "utama": "Python",
    "lainnya": ["PHP","Java", "HTML"]
}
print(skill)
del skill["utama"]
print(skill)
skill_2 = {
    "utama": "Rust",
    "lainnya": ["PHP","Java", "HTML"]
}
print(skill_2)
print(skill_2.pop("utama"))
print(skill_2)
print(skill_2.pop("alamat", None))
print(skill_2.pop("lainnya", None))
print(skill_2)

print(web)
web.clear()
print(web)

print("\n6. Menambahkan Item ke Dictionary")
user = {
    "name": "petanikode"
}
print(user)
user.update({"password": "akucintakamu123"})
print(user)
user.update({"name": "peternaklinux"})
print(user)
user["alamat"] = "Bandung"
print(user)
user["password"] = "alaybanget321"
print(user)

print("\n7. Mengambil Panjang Dictionary")
books = {
    "python": "Menguasai Python dalam 2028 jam",
    "java": "Tutorial Belajar untuk Pemula",
    "php": "Membuat aplikasi web dengan PHP"
}
print(f"total buku: {len(books)}")