# Simulasi Sistem Peminjaman Sepeda Kampus

**_File_:** `peminjaman_sepeda.py`

Universitas menyediakan layanan **peminjaman sepeda gratis** untuk mahasiswa di beberapa titik lokasi dalam kampus. Sistem ini harus memproses _log_ peminjaman dan pengembalian sepeda serta melacak status sepeda dan mahasiswa.

Setiap sepeda memiliki ID unik dan hanya boleh dipinjam oleh satu mahasiswa dalam satu waktu.

Setiap mahasiswa hanya boleh **meminjam satu sepeda** dan harus **mengembalikannya sebelum dapat meminjam sepeda lagi**.

✅ Program harus memproses serangkaian perintah berikut:

* `PINJAM <nama_mahasiswa> <id_sepeda>` → Mahasiswa meminjam sepeda
* `KEMBALI <nama_mahasiswa>` → Mahasiswa mengembalikan sepeda
* `STATUS` → Menampilkan daftar sepeda yang sedang dipinjam beserta siapa peminjamnya, diurutkan berdasarkan `id_sepeda`

⛔ Aturan Validasi:

1. Jika sepeda sudah dipinjam → tolak peminjaman, tampilkan:

   `Gagal: Sepeda <id_sepeda> sedang dipinjam`

2. Jika mahasiswa sedang meminjam sepeda → tolak peminjaman, tampilkan:

   `Gagal: <nama_mahasiswa> masih meminjam sepeda`

3. Jika mahasiswa tidak sedang meminjam → tolak pengembalian, tampilkan:

   `Gagal: <nama_mahasiswa> tidak sedang meminjam sepeda`

4. Perintah `STATUS` menampilkan daftar dalam format:

   `<id_sepeda>: <nama_mahasiswa>`

## _Input_

* Baris pertama: `N` — jumlah perintah
* Diikuti `N` baris perintah dalam format seperti di atas

## _Output_

* Cetak output untuk setiap perintah yang menghasilkan respons (baik sukses maupun gagal)
* Untuk perintah `STATUS`, tampilkan daftar sepeda yang sedang dipinjam (jika ada); jika tidak ada, cetak `Tidak ada sepeda yang sedang dipinjam`

## Contoh

**_Input_:**

```
8
PINJAM Andi S001
PINJAM Budi S002
PINJAM Andi S003
KEMBALI Andi
PINJAM Andi S003
PINJAM Cici S002
STATUS
KEMBALI Dedi
```

**_Output_:**

```
Andi meminjam sepeda S001
Budi meminjam sepeda S002
Gagal: Andi masih meminjam sepeda
Andi mengembalikan sepeda S001
Andi meminjam sepeda S003
Gagal: Sepeda S002 sedang dipinjam
S002: Budi
S003: Andi
Gagal: Dedi tidak sedang meminjam sepeda
```
