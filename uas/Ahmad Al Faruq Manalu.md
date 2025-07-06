# Sistem Rekomendasi Pendanaan Proyek Inovasi

**_File_:** `rekomendasi_pendanaan.py`

Sebuah badan riset nasional ingin membuat sistem untuk merekomendasikan dana pendanaan ke berbagai proyek inovasi. Setiap proyek memiliki sejumlah parameter evaluasi:

* `id_proyek` (integer unik)
* `nilai_inovasi` (0–100)
* `nilai_keberlanjutan` (0–100)
* `nilai_skala` (0–100)
* `anggaran_diminta` (integer dalam juta rupiah)

Tugas sistem:

1. **_Filter_** proyek: hanya ambil yang total skor = `(nilai_inovasi + nilai_keberlanjutan + nilai_skala)` ≥ **210**.
2. Dari hasil _filter_, **urutkan** berdasarkan:

   * skor total (menurun)
   * jika skor sama, urut `anggaran_diminta` (menaik, karena utamakan efisiensi).

3. **Ambil** proyek teratas sampai jumlah anggaran kumulatif ≤ `B` (batas anggaran total), sisakan jika melebihi.
4. Hasil akhir berupa daftar proyek yang direkomendasikan dengan:

   * `id_proyek`, `skor_total`, dan `anggaran_diminta`.

5. Jika tidak ada proyek memenuhi syarat awal, tampilkan `"Tidak ada rekomendasi"`.

## _Input_

* Baris pertama: integer `N` — jumlah proyek
* Baris kedua: integer `B` — total anggaran tersedia (juta rupiah)
* N baris berikutnya: setiap baris berisi 5 angka dipisah spasi:

  ```
  id_proyek nilai_inovasi nilai_keberlanjutan nilai_skala anggaran_diminta
  ```

## _Output_

* Jika ada rekomendasi:

  Setiap baris, urut sesuai kriteria:
  
  ```
  id_proyek skor_total anggaran_diminta
  ```

* Jika tidak ada yang lolos _filter_ awal:

  _Output_ tepat:

  ```
  Tidak ada rekomendasi
  ```

## Contoh 1

**_Input_:**

```
5
300
101 80 70 60 120
102 85 80 50 150
103 60 60 60 100
104 90 70 60 200
105 70 80 70 100
```

**Proses:**

* Hitung skor total:

  * 101 → 210
  * 102 → 215
  * 103 → 180 → dibuang
  * 104 → 220
  * 105 → 220

* Urutkan:

  * (104,220,200), (105,220,100), (102,215,150), (101,210,120)

* Ambil sesuai B=300:

  * Ambil 104: total=200
  * Ambil 105: total=300
  * Tidak cukup sisa untuk proyek berikut (150 > 0)

* Rekomendasi = 104 & 105

**_Output_:**

```
104 220 200
105 220 100
```

## Contoh 2

**_Input_:**

```
3
500
201 60 60 60 100
202 70 50 60 130
203 80 50 70 140
```

**Proses:**
Semua skor <210 → tidak ada yang lolos filter → langsung `"Tidak ada rekomendasi"`.

**_Output_:**

```
Tidak ada rekomendasi
```
