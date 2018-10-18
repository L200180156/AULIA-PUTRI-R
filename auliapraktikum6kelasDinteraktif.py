Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\auliapraktikum6kelasD.py 
>>> ##Kegiatan 1
>>> nama
'Aulia Putri Rachmadani'
>>> alamat
'jalan muria'
>>> NIM
'L200180156'
>>> asalsekolah
'SMAN 1 mojokerto'
>>> tempatlahir
'bekasi'
>>> tanggallahir
'12 juni 1999'
>>> fakultas
'Komunikasi dan Informatika'
>>> prodi
'Informatika'
>>> kelas
'D'
>>> hobi
'memasak'
>>> 
 RESTART: C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\auliapraktikum6kelasD.py 
>>> namasingkat
'AuliaP.R'
>>> username
'Aulia121999'
>>> password
'Aul1999'
>>> 
 RESTART: C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\auliapraktikum6kelasD.py 
>>> ##Kegiatan 3
>>> Nama = 'Aulia Putri Rachmadani'
>>> NIM = 'L200180156'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type (a)
<class 'int'>
>>> #phyton menampilkan jenis data variabel 'a' yang merupakan integer
>>> type (b)
<class 'int'>
>>> #phyton menampilkan jenis data variabel 'a' yang merupakan integer
>>> a/b
52.54545454545455
>>> #phyton menampilkan data dari hasil operasi pembagian variabel 'a' dengan 'b'
>>> a//b
52
>>> #phyton menampilkan data hasil operasi pembagian variabel 'a' dengan 'b' dengan pembulatan kebawah
>>> 10 * (a-999)
1570
>>> #phyton menampikal data operasi variabel 'a' dikurangi 999 lalu dikalikan 10
>>> b ** 2
484
>>> #phyton menampikal kuadrat data variabel 'b'
>>> a % b
12
>>> #phyton menampilkan sisa hasil bagi data variabel 'a' dengan 'b'
>>> c = 12.5
>>> type (c)
<class 'float'>
>>> #phyton menampikan jenis data dari variabel 'c' yang merupakan sebuh float
>>> a/c
92.48
>>> #phyton menampilkan data dari hasil operasi pembagian variabel 'a' dengan 'c'
>>> a//c
92.0
>>> #phyton menampilkan data dari hasil operasi pembagian variabel 'a' dengan 'c' dengan pembulatan kebawah, karena 'a' merupakan sebuah integer, dan 'c' merupakan float maka hasilnya juga float
>>> a % c
6.0
>>>  #phyton menampilkan sisa hasil bagi data variabel 'a' dengan 'c' , karena 'a' merupakan sebuah integer, dan 'c' merupakan float maka hasilnya juga float
>>> c > b
False
>>> #perintah yang dimasukkan merupakan tipe data bool, maka saat perintah dijalankan phyton akan merespon dengan true/false karena c tidak lebih besar dari b maka pernyataan salah
>>> type (c > b)
<class 'bool'>
>>> #type data 'c>b" merupakan boolean
>>> a > b and b > c
True
>>> #karena a lebih besar dari b dan b lebih dan b lebih besar dari c dan kedua syarat terpenuhi maka jawaban true
>>> a > 1100 or b < 10
True
>>> #a lebih besar sari 1100 tetapi b tidak kurang dari 10, namun karena salah satu syarat terpenuhi (perintah 'or') maka jawabanya adalah true
>>> 
 RESTART: C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\auliapraktikum6kelasD.py 
>>> ##Kegiatan 4
>>>  Nama = 'Aulia Putri Rachmadani'
SyntaxError: unexpected indent
>>> Nama = 'Aulia Putri Rachmadani'
>>> NIM = 156
>>> tinggi = 1.55
>>> berat = 45
>>> tahunlahir = 1999
>>> aku = (tahunlahir, berat, tinggi, NIM, Nama)
>>> data = [tahunlahir, berat, tinggi, NIM, Nama]
>>> type (aku)
<class 'tuple'>
>>> #phyton menampilkan jenis data variabel 'aku' yang merupakan jenis tuple
>>> aku [0]
1999
>>> #phyton menampikal indeks variabel 'aku' anggota pertama yaitu tahun lahir = 1999
>>> a = NIM % 4; aku[a]
1999
>>> #phyton menyimpan variabel 'a' yang didalamnya NIM, lalu menampilkan  indeks variabel 'aku' anggota pertama yaitu tahun lahir = 1999
>>> type (aku[a])
<class 'int'>
>>> #data variabel 'aku' anggota pertama merupakan sebuah integer
>>> aku[a:4]
(1999, 45, 1.55, 156)
>>> #phyton menampilkan slicing variabel 'aku' dari anggota pertama hingga anggota ke 4
>>> type (aku[4])
<class 'str'>
>>> #phyton menampilkan jenis data variabel 'aku' anggota ke 4 (anggota phyton dimulai dari 0)
>>> aku [0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    aku [0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> #pada tuple, anggota tidak bisa dirubah tanda '=' artinya menyimpan sehingga menyimpan anggota pertama yang awalnya tanggal lahirmenjadi 'ok' menjadi eror
>>> type(data)
<class 'list'>
>>> #tipe variabel 'data' adalah list ditandai dengan adanya kuung siku
>>> type (data[4])
<class 'str'>
>>> #tipe data anggota terakhir variabel data adalah nama, yang merupakan string
>>> data[4][5]
' '
>>> #menampilkan data ke 4 dan 5 karena tidak ada maka kosong
>>> data[4][a:6]
'Aulia '
>>> #menampilan anggota ke 4 dari 0 dari anggota pertama hingga ke 6
>>> data[0] = 'ok'
>>> data [0]= 'ok'; data
['ok', 45, 1.55, 156, 'Aulia Putri Rachmadani']
>>> #mengganti anggota data ke 0 dengan 'ok' lalu menampilkan pergantian anggota data yang sudah digati
>>> data[-a]
'ok'
>>> #menampilkan anggota variabel ''data' yaitu 'ok
>>> range(a)
range(0, 0)
>>> #menampilkan hasil dari range a
