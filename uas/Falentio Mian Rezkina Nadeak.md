# Sistem Penjadwalan Ronda Warga

**_File_:** `jadwal_ronda.py`

Sebuah kompleks perumahan akan menyusun **jadwal ronda malam** untuk para warga selama sebulan. Setiap warga hanya boleh bertugas **sekali dalam seminggu**, dan tiap hari membutuhkan **minimal 2 orang ronda**.

Panitia telah mencatat data berikut:

* Daftar warga yang tersedia setiap hari dalam seminggu (Senin s.d. Minggu)
* Jumlah minggu dalam bulan tersebut (`M` minggu)

Program yang Anda buat harus:

1. Menyusun jadwal ronda untuk **M minggu ke depan** berdasarkan ketersediaan warga.
2. Memastikan setiap hari terdapat **minimal 2 warga** yang dijadwalkan.
3. Memastikan setiap warga hanya bertugas **1 kali per minggu**, dan hanya di hari yang mereka tersedia.
4. Jika suatu hari kekurangan warga → tampilkan hari tersebut dalam laporan kekurangan.

Program tidak perlu mengoptimalkan jumlah total warga yang bertugas, cukup memenuhi semua syarat di atas.

## _Input_

* Baris pertama: integer `M` — jumlah minggu
* 7 baris berikutnya mewakili hari Senin hingga Minggu, masing-masing berisi:

  ```
  HARI: nama1 nama2 nama3 ...
  ```

* Contoh:

    ```
    3
    Senin: Ali Budi Dedi
    Selasa: Budi Cici Dedi
    Rabu: Ali Dedi
    Kamis: Budi Cici
    Jumat: Ali Budi Cici
    Sabtu: Dedi
    Minggu: Cici Dedi
    ```

## _Output_

* Cetak jadwal dalam format berikut untuk setiap minggu

* Contoh:

    ```
    Minggu ke-1:
    Senin: Ali, Budi
    Selasa: Cici, Dedi
    ...
    Minggu: Dedi, Cici

    Minggu ke-2:
    ...

    Hari kekurangan petugas:
    Sabtu (Minggu ke-1)
    Sabtu (Minggu ke-2)
    ```

    Jika **tidak ada kekurangan petugas**, bagian akhir tidak perlu ditampilkan.

## Catatan Teknis

* Urutan warga dalam satu hari bebas, asal valid.
* Jika tersedia lebih dari dua warga di hari tertentu, pilih acak atau sembarang dua orang.
* Warga hanya boleh bertugas **1 kali per minggu**, meskipun tersedia di beberapa hari.
* Warga **boleh bertugas di minggu-minggu berikutnya**.

---

## Contoh (parsial, ringkas)

**_Input_:**


```
1
Senin: Ali Budi Dedi
Selasa: Budi Cici Dedi
Rabu: Ali Dedi
Kamis: Budi Cici
Jumat: Ali Budi Cici
Sabtu: Tono
Minggu: Emir Tono
```

**_Output_:**

```
Minggu ke-1:
Senin: Ali, Budi
Selasa: Cici, Dedi
Rabu: -
Kamis: -
Jumat: -
Sabtu: Tono, -
Minggu: Emir, -

Hari kekurangan petugas:
Rabu (Minggu ke-1)
Kamis (Minggu ke-1)
Jumat (Minggu ke-1)
Sabtu (Minggu ke-1)
Minggu (Minggu ke-1)
```
