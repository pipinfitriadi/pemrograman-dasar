# Analisis Penumpang Kereta Antar Kota

**_File_:** `analisis_penumpang_kereta.py`

Sebuah sistem tiket kereta antar kota ingin menganalisis **riwayat perjalanan penumpang** berdasarkan _log_ data yang dikumpulkan setiap hari. Setiap entri _log_ mencatat:

* `nama_penumpang`
* `stasiun_awal`
* `stasiun_tujuan`
* `jumlah_km` (jarak perjalanan)

Manajemen ingin mengetahui:

1. Total **jarak tempuh** setiap penumpang selama periode yang dicatat.
2. Daftar penumpang yang memiliki **total jarak tempuh tertinggi**.
3. Daftar penumpang yang telah **mengunjungi minimal 3 stasiun berbeda** sebagai `stasiun_tujuan`.

## _Input_

* Baris pertama: _integer_ `N` — jumlah _log_ perjalanan
* Diikuti `N` baris data _log_ dengan format:
  `<nama_penumpang>;<stasiun_awal>;<stasiun_tujuan>;<jumlah_km>`

## _Output_

Tiga bagian _output_:

1. Total jarak tempuh per penumpang (diurutkan alfabetis):

    ```
    Jarak tempuh:
    Ali: 220
    Budi: 145
    Cici: 180
    ```

2. Penumpang dengan jarak tempuh maksimum (jika lebih dari satu, tampilkan semuanya):

    ```
    Jarak tempuh tertinggi:
    Ali
    ```

3. Penumpang yang pernah sampai ke 3 `stasiun_tujuan` berbeda atau lebih:

    ```
    Penumpang aktif (>=3 stasiun tujuan):
    Budi
    Cici
    ```

## Contoh

**_Input_:**

```
8
Ali;Bandung;Jakarta;150
Budi;Jakarta;Cirebon;80
Cici;Bandung;Surabaya;180
Ali;Jakarta;Cirebon;70
Budi;Cirebon;Semarang;65
Cici;Surabaya;Yogyakarta;0
Cici;Bandung;Bandung;0
Budi;Semarang;Jakarta;0
```

**_Output_:**

```
Jarak tempuh:
Ali: 220
Budi: 145
Cici: 180

Jarak tempuh tertinggi:
Ali

Penumpang aktif (>=3 stasiun tujuan):
Budi
Cici
```

## Catatan Tambahan

* Beberapa _log_ mungkin memiliki `jumlah_km = 0`, tetap dihitung untuk **kunjungan stasiun**, tapi tidak untuk total jarak.
* `stasiun_tujuan` dihitung unik per penumpang — kunjungan berulang tidak dihitung lebih dari sekali.
