# Pengelompokan Surat Masuk di Kantor Kelurahan

**_File_:** `pengelompokan_surat.py`

Sebuah kantor kelurahan menerima ratusan surat fisik setiap minggunya, dengan berbagai jenis dan prioritas penanganan. Untuk mempermudah proses distribusi, surat-surat tersebut perlu dikelompokkan berdasarkan **jenis surat** dan diurutkan berdasarkan **prioritas penanganan**.

Setiap surat yang masuk memiliki informasi berikut:

* `id_surat` (kode unik)
* `jenis` (misalnya: "Domisili", "Izin Usaha", "Keterangan Ahli Waris", dll)
* `prioritas` (angka dari 1–5, di mana 1 adalah prioritas tertinggi)

Tugas Anda adalah:

1. Membaca data surat masuk.
2. Mengelompokkan surat berdasarkan `jenis`.
3. Mengurutkan setiap kelompok berdasarkan `prioritas` (dari kecil ke besar).
4. Menampilkan seluruh kelompok dalam urutan abjad `jenis`.

## _Input_

* Baris pertama: _integer_ `N` — jumlah surat masuk
* Diikuti `N` baris, masing-masing berisi:
  `<id_surat>;<jenis>;<prioritas>`

## _Output_

Untuk setiap jenis surat (urut abjad), tampilkan:

```
=== [jenis surat] ===
[id_surat_1] prioritas:[n]
[id_surat_2] prioritas:[n]
...
```

Jika tidak ada surat sama sekali (`N=0`), cukup tampilkan:

```
Tidak ada surat masuk
```

## Contoh 1

**_Input_:**

```
6
S001;Domisili;3
S002;Izin Usaha;2
S003;Domisili;1
S004;Izin Usaha;5
S005;Keterangan Ahli Waris;2
S006;Domisili;2
```

**_Output_:**

```
=== Domisili ===
S003 prioritas:1
S006 prioritas:2
S001 prioritas:3

=== Izin Usaha ===
S002 prioritas:2
S004 prioritas:5

=== Keterangan Ahli Waris ===
S005 prioritas:2
```

## Contoh 2

**_Input_:**

```
0
```

**_Output_:**

```
Tidak ada surat masuk
```
