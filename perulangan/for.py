# for index in range(5):
#     print(index)

# for index in range(1, 5):
#     print(index)

# for index in range(1, 5, 2):
#     print(index)

# for index in range(-10, 5, 2):
#     print(index)

# for index in range(8, 2, -1):
#     print(index)

# for i in range(8, 2, -1):
#     print(i)

# data = range(8, 2, -1)

# for i in data:
#     print(i)

# for mahasiswa in [
#     "Melisa",
#     "Falen",
#     "Rajan",
#     "Dika"
# ]:
#     print(mahasiswa)

for mahasiswa, nilai in [
    ["Melisa", "A"],
    ["Falen", "A"],
    ["Rajan", "A"],
    ["Dika", "A+"]
]:
    print(f"{mahasiswa} nilai matakuliah adalah {nilai}")

    if mahasiswa == "Rajan":
        break