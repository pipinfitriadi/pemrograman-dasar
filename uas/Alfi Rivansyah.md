# Simulasi Penjadwalan Tim Penyelamat Bencana

**_File_:** `penjadwalan_tim.py`

Sebuah lembaga penanggulangan bencana memiliki sejumlah tim penyelamat yang harus dikirim ke berbagai lokasi terdampak bencana. Masing-masing lokasi membutuhkan minimal kapasitas tertentu dan memiliki tingkat urgensi. Sementara itu, setiap tim memiliki kapasitas personel dan hanya dapat dikirim ke **satu lokasi saja**.

Tugas program adalah menentukan **alokasi tim ke lokasi** berdasarkan ketentuan:

1. **Setiap lokasi** hanya bisa ditempati oleh **satu tim**.
2. **Setiap tim** hanya boleh ditugaskan ke **satu lokasi**.
3. Lokasi dengan urgensi lebih tinggi harus diprioritaskan.
4. Hanya tim yang memiliki **kapasitas personel ≥ kebutuhan minimum lokasi** yang bisa dialokasikan ke lokasi tersebut.
5. Jika ada beberapa tim yang bisa masuk ke suatu lokasi, pilih tim dengan kapasitas **terkecil yang masih memenuhi syarat** (agar efisien).
6. Jika lokasi tidak mendapatkan tim, lokasi tersebut dicatat sebagai “Belum tertangani”.

Program harus mencetak hasil alokasi, serta daftar lokasi yang belum tertangani.

## _Input_

* Baris pertama: dua angka `T` dan `L` — jumlah tim dan jumlah lokasi
* `T` baris berikutnya: `id_tim kapasitas_personel`
* `L` baris berikutnya: `id_lokasi kebutuhan_minimal urgensi`

## _Output_

* Baris-baris alokasi dalam format:

  `id_tim -> id_lokasi`

* Diakhiri dengan satu baris kosong
* Lalu cetak daftar lokasi belum tertangani (jika ada) dalam urutan urgensi tertinggi ke terendah:

  ```
  Lokasi belum tertangani:
  id_lokasi1
  id_lokasi2
  ...
  ```

Jika semua lokasi tertangani, cukup tampilkan hasil alokasi tanpa bagian akhir.

## Contoh 1

**_Input_:**

```
4 3
T01 10
T02 8
T03 12
T04 6
L01 8 90
L02 10 95
L03 5 80
```

**_Output_:**

```
T02 -> L01
T01 -> L02
T04 -> L03

```

## Contoh 2 (Lokasi tidak semua tertangani)

**_Input_:**

```
3 4
T01 6
T02 7
T03 5
L01 8 95
L02 5 90
L03 6 85
L04 7 80
```

**_Output_:**

```
T03 -> L02
T01 -> L03
T02 -> L04

Lokasi belum tertangani:
L01
```
