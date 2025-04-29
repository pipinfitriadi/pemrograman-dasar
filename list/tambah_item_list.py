buah = ["jeruk", "apel", "mangga", "duren"]
print(buah)

buah.append("manggis") # Tambah item di akhir
print(buah)

buah.insert(0, "anggur") # Tambah item di awal
print(buah)

buah.insert(2, "semangka") # Tambah item di tengah
print(buah)

print("=" * 10)
print("Latihan 2: Membuat Program dengan List")

hobi = []
stop = False
i = 0

while not stop:
    hobi_baru = input(f"Inputkan hobi yang ke-{i}: ")
    hobi.append(hobi_baru)

    i += 1

    tanya = input("Mau isi lagi? (y/t): ")

    if tanya == "t":
        stop = True

print("=" * 10)
print(f"Kamu memiliki {len(hobi)} hobi")

for hb in hobi:
    print(f"- {hb}")
