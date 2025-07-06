# Simulasi Pemesanan Tiket Konser

**_File_:** `tiket_konser.py`

Sebuah sistem penjualan tiket konser ingin dibuat untuk menangani antrian pemesanan dari para pelanggan. Konser menyediakan beberapa **kategori tiket** dengan jumlah kursi terbatas di tiap kategori:

* VIP (kapasitas `kv`)
* Reguler (kapasitas `kr`)
* Ekonomi (kapasitas `ke`)

Setiap pemesan hanya boleh **memesan 1 tiket**, dan mereka boleh memilih **urutan preferensi** kategori (misalnya: Reguler → VIP → Ekonomi).

Program Anda harus memproses daftar antrian pemesan dan memberikan tiket sesuai preferensi dan ketersediaan.

Aturan pemrosesan:

1. Pemesan dilayani sesuai urutan antrian.
2. Sistem akan memberikan kategori **tertugas tinggi pertama yang masih tersedia** dari daftar preferensi pemesan.
3. Jika semua pilihan pemesan habis → pemesan tidak mendapatkan tiket.
4. Hasil akhir berupa daftar siapa mendapat kategori apa, dan siapa yang tidak mendapatkan tiket.

## _Input_

* Baris pertama: tiga angka `kv kr ke` — kapasitas awal tiap kategori
* Baris kedua: integer `N` — jumlah pemesan
* N baris berikutnya:

  `nama preferensi1 preferensi2 preferensi3`

Preferensi berupa salah satu dari: `VIP`, `Reguler`, `Ekonomi`, dan urutannya **boleh berbeda-beda antar pemesan**.

## _Output_

N baris sesuai urutan antrian, berisi:

* Jika dapat tiket: `nama mendapat tiket kategori`
* Jika tidak dapat tiket: `nama tidak mendapat tiket`

## Contoh 1

**_Input_:**

```
1 2 2
5
Andi VIP Reguler Ekonomi
Budi VIP Reguler Ekonomi
Cici Reguler Ekonomi VIP
Dewi Ekonomi Reguler VIP
Eka VIP Reguler Ekonomi
```

**_Output_:**

```
Andi mendapat tiket VIP
Budi mendapat tiket Reguler
Cici mendapat tiket Reguler
Dewi mendapat tiket Ekonomi
Eka mendapat tiket Ekonomi
```

## Contoh 2 (jika ada yang tidak kebagian)

**_Input_:**

```
1 1 2
5
Andi VIP Reguler Ekonomi
Budi VIP Reguler Ekonomi
Cici Reguler Ekonomi VIP
Dewi Ekonomi Reguler VIP
Eka VIP Reguler Ekonomi
```

**_Output_:**

```
Andi mendapat tiket VIP
Budi mendapat tiket Reguler
Cici mendapat tiket Ekonomi
Dewi mendapat tiket Ekonomi
Eka tidak mendapat tiket
```
