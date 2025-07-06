# Sistem Penilaian Lomba Karya Inovasi Mahasiswa

**_File_:** `penilaian_lomba.py`

Sebuah perguruan tinggi menyelenggarakan lomba karya inovasi mahasiswa. Setiap tim peserta dinilai oleh beberapa juri berdasarkan tiga aspek:

* **Kreativitas** (skor 0–100)
* **Kelayakan Teknis** (skor 0–100)
* **Potensi Dampak Sosial** (skor 0–100)

Masing-masing aspek memiliki bobot penilaian sebagai berikut:

* Kreativitas: 30%
* Kelayakan Teknis: 40%
* Potensi Dampak Sosial: 30%

Setiap juri memberikan satu penilaian per tim. Total skor akhir tim dihitung sebagai **rata-rata tertimbang** dari semua penilaian juri terhadap tim tersebut.

Tugas Anda:

1. Hitung skor akhir untuk setiap tim berdasarkan semua penilaian juri.
2. Urutkan tim dari skor tertinggi ke terendah.
3. Cetak **3 tim terbaik** sebagai pemenang.
4. Jika ada dua tim dengan skor akhir yang **sama** dan memperebutkan peringkat 3, tampilkan keduanya sebagai juara 3 bersama.

## _Input_

* Baris pertama: `N` — jumlah penilaian juri yang diberikan
* N baris berikutnya berformat:

  `id_tim kreativitas teknis dampak`

Setiap `id_tim` adalah string unik.

## _Output_

* Tiga besar pemenang dalam format:

  `Juara X: id_tim (skor akhir)`

* Skor ditampilkan dengan 2 angka di belakang koma
* Jika ada juara 3 bersama, tampilkan keduanya sebagai:

  ```
  Juara 3 (bersama): id_tim1 (skor) dan id_tim2 (skor)
  ```

## Contoh 1

**_Input_:**

```
7
Alpha 80 90 85
Beta 85 88 90
Gamma 78 82 80
Alpha 82 91 87
Beta 88 87 92
Gamma 75 80 77
Delta 90 85 80
```

**_Output_:**

```
Juara 1: Beta (88.25)
Juara 2: Alpha (86.30)
Juara 3: Delta (85.00)
```

## Contoh 2 (Skor Sama)

Jika skor akhir untuk dua tim yang berbeda sama pada posisi ke-3.

**_Input_:**

```
7
Alpha 80 90 85
Beta 85 88 90
Gamma 78 82 80
Alpha 82 91 87
Beta 88 87 92
Gamma 83 91 95
Delta 90 85 80
```

**_Output_:**

```
Juara 1: Beta (88.25)
Juara 2: Alpha (86.30)
Juara 3 (bersama): Delta (85.00) dan Gamma (85.00)
```
