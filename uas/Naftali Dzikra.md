# istem Penilaian Lari Estafet Antar-Kelas

**_File_:** `penilaian_lari_estafet.py`

Dalam acara olahraga antar-kelas, setiap kelas mengikuti lomba **lari estafet**. Setiap tim terdiri dari **4 pelari** yang berlari secara berurutan. Waktu lari masing-masing pelari dicatat dan digunakan untuk menghitung total waktu tim.

Namun, panitia memutuskan sistem penilaian akhir **tidak hanya berdasarkan total waktu**, melainkan juga:

* Jika tim memiliki pelari tercepat dengan waktu ≤ 13.0 detik, mereka mendapatkan pengurangan 5 detik dari total waktu.

Tugas Anda:

1. Membaca daftar tim dan waktu keempat pelari.
2. Menghitung total waktu tim (jumlah waktu semua pelari).
3. Mengurangi 5 detik dari total waktu tim berdasarkan pelari tercepat.
4. Mengurutkan seluruh tim berdasarkan total waktu akhir (semakin kecil, semakin baik).
5. Menampilkan peringkat akhir tim dari juara 1 dan seterusnya.

## _Input_

* Baris pertama: _integer_ `N` — jumlah tim yang berpartisipasi
* Diikuti `N` baris, masing-masing berisi:

  `<nama_tim> <waktu1> <waktu2> <waktu3> <waktu4>`

* Setiap waktu adalah bilangan desimal dalam **detik** (misalnya: `13.2`).

## _Output_

Cetak urutan tim berdasarkan peringkat, dengan format:

```
Juara 1: <nama_tim> (total_waktu_setelah_bonus)
Juara 2: ...
```

Waktu akhir ditampilkan dengan dua angka di belakang koma.

## Contoh 

**_Input_:**

```
3
Alpha 14.0 13.5 15.2 14.3
Bravo 13.0 13.0 13.0 13.0
Charlie 15.5 14.0 14.5 13.0
```

**Perhitungan:**

* **Alpha**:

    Total = 14.0 + 13.5 + 15.2 + 14.3 = 57.0

    Pelari tercepat tidak ada → Total = 57.0 (Tetap)

* **Bravo**:

    Total = 13.0 * 4 = 52.0

    Pelari tercepat = 13.0 (empat orang) → Total = 52.0 - 5 = **47.0**

* **Charlie**:

    Total = 15.5 + 14.0 + 14.5 + 13.0 = 57.0

    Pelari tercepat = 13.0 → Total = 57.0 - 5 = **52.0**

**_Output_:**

```
Juara 1: Bravo (47.00)
Juara 2: Charlie (52.00)
Juara 3: Alpha (57.00)
```
