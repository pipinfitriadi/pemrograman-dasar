# Statistik Laporan Gangguan Jaringan

**_File_:** `statistik_gangguan_jaringan.py`

Sebuah perusahaan penyedia layanan internet menerima laporan gangguan jaringan dari pelanggannya setiap hari. Setiap laporan mencakup:

* Nama pelanggan
* Tanggal laporan
* Jenis gangguan (misalnya: *Putus Total*, *Lambat*, *Intermiten*, dll)

Manajemen ingin membuat rekap statistik gangguan berdasarkan data tersebut, untuk tujuan pemantauan kualitas layanan.

**Tugas Program**:

1. Hitung total laporan gangguan **per jenis gangguan**.
2. Hitung jumlah laporan **yang dibuat oleh tiap pelanggan**.
3. Tampilkan jenis gangguan yang **paling sering dilaporkan**.
4. Tampilkan daftar pelanggan yang **melaporkan lebih dari satu jenis gangguan**.

## _Input_

* Baris pertama: _integer_ `N` — jumlah laporan yang diterima
* Diikuti `N` baris, masing-masing berisi:
  `<nama_pelanggan>;<tanggal (YYYY-MM-DD)>;<jenis_gangguan>`

## _Output_

Cetak dalam urutan bagian berikut:

1. Total laporan per jenis gangguan (urut alfabetis):

    ```
    Laporan per jenis gangguan:
    Intermiten: 2
    Lambat: 6
    Putus Total: 1
    ```

2. Jumlah laporan per pelanggan (urut alfabetis):

    ```
    Laporan per pelanggan:
    Ahmad: 3
    Budi: 2
    Cici: 4
    ```

3. Jenis gangguan paling sering dilaporkan:

    ```
    Jenis gangguan terbanyak:
    Lambat
    ```

4. Pelanggan yang melaporkan lebih dari satu jenis gangguan (urut alfabetis):

    ```
    Pelanggan dengan variasi gangguan:
    Ahmad
    Cici
    ```

    Jika tidak ada pelanggan yang melaporkan lebih dari satu jenis gangguan, cukup tampilkan:

    ```
    Pelanggan dengan variasi gangguan:
    (Tidak ada)
    ```

## Contoh

**_Input_:**

```
9
Ahmad;2025-07-01;Lambat
Budi;2025-07-01;Lambat
Cici;2025-07-01;Putus Total
Cici;2025-07-02;Lambat
Ahmad;2025-07-03;Intermiten
Ahmad;2025-07-03;Lambat
Cici;2025-07-04;Intermiten
Cici;2025-07-04;Lambat
Budi;2025-07-04;Lambat
```

**_Output_:**

```
Laporan per jenis gangguan:
Intermiten: 2
Lambat: 6
Putus Total: 1

Laporan per pelanggan:
Ahmad: 3
Budi: 2
Cici: 4

Jenis gangguan terbanyak:
Lambat

Pelanggan dengan variasi gangguan:
Ahmad
Cici
```
