def rata_rata(*angka):
    nilai = 0

    for i in angka:
        nilai += i
    
    return nilai / len(angka)

print(rata_rata(1, 2, 3, 4, 5))
print("="*10)

# data = []

# for i in range(4):
#     data.append(int(input("Masukkan data: ")))

# print(rata_rata(*data))
# print("="*10)

def tes(*args, **kwargs):
    print(args, kwargs)
    print(list(args), list(kwargs.items()))
    return args, kwargs

tes()
print("="*10)

tes(True, [2, 4], "Asdfsdf", nama_depan="Doni", nama_belakang="Tabrani")
print("="*10)

tuple_1 = True, [2, 4], "Asdfsdf"
dictionary_1 = {"nama_depan": "Doni", "nama_belakang": "Tabrani"}
variable_1, variable_2 = tes(*tuple_1, **dictionary_1)
print(f"{variable_1=}")
print(f"{variable_2=}")

print(*variable_1)
a, b, c = variable_1
print(a, b, c)
d = variable_1[0]
print(f"{d=}")
e, *f = variable_1
print(f"{e=}")
print(f"{f=}")
print("="*10)
