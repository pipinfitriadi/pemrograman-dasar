def nama():
    print("Hello")

print(nama())
nama_2 = lambda: print("Hello 2")
print(nama_2())

print("-"*50)

def matkul(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

print(matkul(80))

matkul_2 = lambda nilai: (
    "A"
    if nilai >= 80 
    else (
        "B"
        if nilai >= 70
        else (
            "C"
            if nilai >= 60
            else (
                "D"
                if nilai >= 50
                else "E"
            )
        )
    )
)
print(matkul_2(75))

print("-"*50)
def tambah(x, y=10):
    return x + y

print(tambah(5))
tambah_2 = lambda x,y=10: x + y 
print(tambah_2(5))

def cetak_nama(depan, belakang):
    print(f"{depan} {belakang}")

print("-"*50)
cetak_nama_2 = lambda depan, belakang: print(f"{depan} {belakang}")
print(cetak_nama(belakang="Rizkika", depan="Sanda"))
print(cetak_nama_2(belakang="Wulandari", depan="Putri"))
