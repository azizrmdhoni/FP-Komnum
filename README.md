### Metode Iterasi Satu Titik Soal No 7

## Kelompok A12 

|    NRP     |          Name         |
| :--------: | :-------------------: |
| 5025241029 | Berwyn Rafif Alvaro   |
| 5025241061 | Ahmad Satrio Arrohman |
| 5025241063 | Ahsin Khuluqil Karim  |
| 5025241071 | Muhamad Aziz Romdhoni |
| 5025241100 | Liem, Alfred Haryanto |

## Import Library
  `import math` 
  - import math: Mengimpor modul matematika standar Python

## Fungsi `ErrorApprox(x_i, x_i_1)`
  ```
  def ErrorApprox(x_i, x_i_1):
    return round(abs((x_i - x_i_1) / x_i) * 100, 2)
  ```
  - Fungsi: Menghitung persentase error aproksimasi antara dua nilai iterasi berturut-turut.
  - Parameter:
    - x_i: Nilai iterasi saat ini.
    - x_i_1: Nilai iterasi sebelumnya.
  - Proses:
    - Menghitung selisih antara nilai saat ini dan sebelumnya (term1 = x_i - x_i_1).
    - Menghitung persentase error terhadap nilai saat ini.
    - round(..., 2) membulatkan hasil ke 2 desimal.
    - abs() menjamin nilai error selalu positif.

## Fungsi `compute_fx(x)`
  ```
  def compute_fx(x):
    x_kuadrat = x**2                  
    bagian_kali1 = -6 * x_kuadrat     
    bagian_kali2 = 19 * x
    pembilang = bagian_kali1 + bagian_kali2 + 84
    penyebut = x_kuadrat
    return round(pembilang / penyebut, 2) if penyebut != 0 else float('nan')
  ```
  - Tujuan: Menghitung nilai fungsi f(x)=(−6x^2 + 19x+84) / x^2
  - Parameter: x (nilai input).
  - Proses:
    - Hitung x^2(x_kuadrat).
    - Hitung −6 * x^2 (bagian_kali1).
    - Hitung 19 * x (bagian_kali2).
    - Jumlahkan hasil langkah 2, 3, dan 8 (pembilang).
    - Bagi pembilang dengan x^2 (penyebut).
    - Bulatkan hasil bagi hingga 2 desimal (round(..., 2)).
    - Jika penyebut = 0 (pembagian nol), kembalikan NaN (float('nan')).

## Fungsi `printIterasi(x_prev, Iterasi)`
  ```
  def printIterasi(x_prev, Iterasi):
    x_current = compute_fx(x_prev)
    
    print(f"Iterasi {Iterasi}:")
    print(f"x{Iterasi-1} = {x_prev:.2f}")
    
    x_kuadrat = x_prev**2
    
    print(f"Iterasi {Iterasi}:")
    print(f"x{Iterasi-1} = {x_prev:.2f}")
    print(f"x{Iterasi} = ((-6)*({x_prev:.2f})² + 19 * ({x_prev:.2f}) + 84) / ({x_prev:.2f})²")
    print(f"   = ((-6) * {x_kuadrat:.2f} + {19*x_prev:.2f} + 84.00) / {x_prev**2:.2f}")
    print(f"   = ({-6*x_kuadrat:.2f} + {19*x_prev:.2f} + 84.00) / {x_prev**2:.2f}")
    print(f"   = {(-6*x_prev**2 + 19*x_prev + 84):.2f} / {x_prev**2:.2f}")
    print(f"x{Iterasi} = {x_current:.2f}")
    
    if Iterasi > 0:
        error = ErrorApprox(x_current, x_prev)
        print(f"Ea: {error}%")
    print()
    
    return x_current
  ```  
  - Tujuan: Mencetak detail perhitungan tiap iterasi dan error (jika ada).
  - Parameter:
    - x_prev: Nilai x dari iterasi sebelumnya.
    - iterasi: Nomor iterasi saat ini.
  - Output:
    - Header Iterasi: Iteration {n}:.
    - Nilai Awal: x_{n-1} = nilai.
    - Proses:
     - Hitung x_current menggunakan compute_fx(x_prev).
     - Cetak informasi iterasi (Iterasi ke-n).
     - Cetak nilai sebelumnya (x_prev).
     - Hitung x^2 (x_kuadrat).
     - Cetak langkah-langkah perhitungan fungsi secara eksplisit:
      - Rumus fungsi.
      - Substitusi nilai x.
      - Perhitungan perkalian dan penjumlahan.
      - Hasil akhir pembagian.
  - Hitung dan cetak Ea dari iterasi > 0.
  - Kembalikan x_current untuk iterasi berikutnya.

## Fungsi `fixed_point_iterasi(initial_x, iterasii)`
  ```
  def fixed_point_iterasi(initial_x, itersii):
    print("Metode Itersi Satu Titik:")
    x = initial_x
    for i in range(1, itersii + 1):
        x = printIterasi(x, i)
  ```
  - Tujuan: Menjalankan metode iterasi titik tetap dari nilai awal tertentu.
  - Parameter:
    - initial_x: Nilai awal x (contoh: 3.0).
    - iterasii: Jumlah iterasi (contoh: 5).
  - Proses:
    - Inisialisasi:
      - Cetak judul metode.
      - Set nilai awal x = initial_x.
      - Loop Iterasi:
        - Untuk setiap iterasi i dari 1 hingga iterasii:
        - Panggil printIterasi(x, i) untuk menghitung dan mencetak hasil.
        - Update nilai x dengan nilai baru dari printIteration.
          
## Python A12_ProgramKomnum_07.py 
  ```
  fixed_point_iterasi(3.0, 5)
  ```
