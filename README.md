# Concert Ticket Inventory Guide
**Nama  : Kelvin Saputra**

**NPM   : 2206027186**

**Kelas : PBP F**

**Link  : [Concert Ticket Inventory Adaptable](https://concert-ticket-inventory.adaptable.app/main)**

### To Do List
---
- [x] Membuat sebuah proyek Django baru.
- [x] Membuat aplikasi dengan nama main pada proyek tersebut.
- [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- [x] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    * name sebagai nama item dengan tipe CharField.
    * amount sebagai jumlah item dengan tipe IntegerField.
    * description sebagai deskripsi item dengan tipe TextField.

- [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

### Penjelasan Proses Pembuatan
---
#### Konfigurasi Repositori lokal 
1. Buatlah direktori untuk proyek concert_ticket_inventory.
2. Bukalah terminal lalu Pada terminal, masuk ke dalam folder yang telah dibuat menggunakan perintah <code>cd <nama_directory></code> (change directory). dalam kasus ini direktori saya adalah `concert_ticket_inventory`
3. Selanjutnya buatlah repositori git kosong pada direktori yang digunakan sebagai proyek dengan menuliskan <code>git init</code>.
4. Lakukan konfigurasi *username* dan *email* agar terhubung dengan commit yang dilakukan.

#### Membuat Project Django baru
1. Pada direktori lokal yang dibuat sebelumnya, saya membuat virtual environment dengan menggunakan terminal lalu menuliskan <code>python -m venv env</code> yang bertujuan agar tools yang digunakan pada project ini terisolasi. Sehingga ketika kita melakukan perubahan versi pada tools sewaktu-waktu, project tidak akan mengalami masalah. 
2. Dengan menggunakan terminal, masuk ke dalam virtual environment dengan menggunakan perintah <code>env\Scripts\activate.bat</code> pada windows.
3. Buatlah file `requirements.txt` yang berisikan tools yang akan digunakan dalam project ini termasuk django.
4. Lakukan instalasi pada seluruh library yang terdaftar dalam `requirements.txt` dengan menggunakan perintah <code>pip install -r requirements.txt</code>
5. Setelah django berhasil terinstall, buatlah project baru yang diinginkan dengan menggunakan perintah <code>django-admin startproject <nama_project> .</code> dalam kasus ini nama project saya adalah `concert_ticket_inventory`. tanda titik pada perintah tersebut bertujuan agar project dibuat tanpa membuat direktori baru.
6. Setelah proyek terbentuk, ubah perizinan yang ada pada <code>settings.py</code> dengan menambahkan syntax 
```python
...
ALLOWED_HOSTS = ["*"]
...
```
hal ini memungkinkan project yang kita buat dapat diakses oleh banyak device atau IP.

7. Setelah itu, saya mencoba menjalankan project django pada localhost dengan menggunakan perintah <code>python manage.py runserver</code> selanjutnya buka link berikut http://localhost:8000 jika sudah terlihat animasi roket, maka project dapat berjalan.
8. Selanjutnya buatlah file dengan nama `.gitignore` yang bertujuan agar file-file yang terdaftar pada `.gitignore` tidak ikut di push ke repositori github.

#### Membuat aplikasi dengan nama `main` pada proyek tersebut.
1. Setelah selesai membuat project, masuk ke dalam virtual environment kembali, lalu buatlah app dengan nama `main` dengan menggunakan perintah <code>python manage.py startapp main</code>

#### Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`
1. Setelah membuat aplikasi `main`, agar dapat dijalankan pada level project, perlu dilakukan routing dengan menambahkan aplikasi `main` pada `INSTALLED_APPS` yang berada pada file `settings.py`.
2. Buatlah direktori `Templates` pad direktori `main` yang bertujuan untuk menampung file-file `HTML`.

#### Membuat model pada aplikasi `main` dengan nama Item dan memiliki atribut wajib sebagai berikut.
1. Pada direktori aplikasi `main`, buatlah model `Item` pada `models.py` yang ada pada direktori `main`, lalu selanjutnya menambahkan atribut berupa 
    * `name` dengan tipe `CharField`
    * `amount` dengan tipe `IntegerField`
    * `description` dengan tipe `TextField`
2. Lakukan migrasi tiap kali ada perubahan pada model basis data tersebut

#### Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. Untuk membuat fungsi pada `views.py` saya memanfaatkan fungsi `render` yang berasal dari fungsi `django.shortcut`.
2. Buat suatu fungsi bernama `show_main` dengan parameter berupa `requests`.
3. Isi fungsi tersebut dengan suatu dictionary `context` yang dimana bisa kita ibaratkan seperti variable dimana key merupakan nama dari variable lalu value adalah isi dari variable.
4. Kemudian dengan memanfaatkan fungsi `render` dengan 3 parameter, yaitu `requests`, `'main.html'`, dan `context` yang selanjutnya nanti dapat digunakan pada html agar tampilan dapat lebih dinamis.
5. Pada file html kita dapat mengubah nama yang awalnya statis menjadi lebih dinamis dengan memanfaatkan key dari dictionary hasil return fungsi `show_main` 

#### Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
1. Agar aplikasi `main` dapat dijalankan pada web, diperlukan proses routing dengan cara membuat `urls.py` pada direktori `main`. file `urls.py` pada tingkat apps dapat digunakan sebagai pengatur url pada aplikasi `main`.
2. Buatlah nama unik pada apps agar tidak terjadi konflik pada saat pemanggilan. dalam kasus ini saya memberi nama `main` dengan memasukkannya pada variable `app_name`.
3. dengan memanfaatkan fungsi dari `django.urls`, yaitu `path` untuk membuat `urlpattern` dan memanfaatkan fungsi `show_main` yang sebelumnya kita buat pada direktori `main` khususnya pada file `views.py` pada parameter `path` agar dapat ditampilkan.
4. selanjutnya tambahkan rute url aplikasi `main` pada `urls.py` tingkat proyek agar dapat terhubung pada aplikasi `main` dan dapat ditampilkan pada saat url dipanggil oleh user.

#### Membuat Repositori Github
1. Pada website github kita perlu membuat repositori baru dengan judul proyek sembarang, pada kasus ini saya buat sama dengan repositori lokal, yaitu `concert-ticket-inventory`.
2. Salin url github, lalu melalui terminal lokal pada repositori lokal, buat sebuah branch baru utama yang kita sebut dengan branch main dengan menggunakan code berikut <code>git branch -M main</code>
3. Hubungkan repositori lokal dengan repositori github menggunakan perintah <code>git remote add origin <URL_REPO></code> pada kasus ini <URL_REPO> kita gunakan url yang sudah disalin sebelumnya.
4. Selanjutnya add seluruh pekerjaan yang dilakukan dengan menggunakan perintah <code>git add .</code>.
5. Setelah add seluruh hasil pekerjaan, lakukan commit dan sekaligus comment singkat apa saja yang telah dikerjakan dengan menggunakan perintah <code>git commit -m "<COMMENT_HERE>"</code>.
6. Setelah melakukan commit, periksa kembali file yang akan dikirim ke repositori github dengan menggunakan perintah <code>git status</code>.
7. Jika sudah sesuai, maka push hasil kerjaan ke repositori github dengan menggunakan perintah <code>git push -u origin main</code>. hal ini bertujuan untuk mengunggah hasil pekerjaan ke repositori github pada branch utama, yaitu branch main.

#### Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Pertama buka situs [Adaptable.io](http//adaptable.io) pada web browser dan login menggunakan akun github yang menyimpan hasil pekerjaan sebelumnya.
2. Jika sudah login, silakan tekan tombol `New App`. Pilih `Connect an Existing Repository`.
3. Hubungkan [Adaptable.io](http//adaptable.io) dengan GitHub dan pilih `All Repositories` pada proses instalasi.
4. Pilih repositori proyek `concert_ticket_inventory` sebagai basis aplikasi yang akan di-deploy. Pilih branch yang ingin dijadikan sebagai deployment branch.
5. saya memilih `Python App Template` sebagai template deployment.
6. Pilih `PostgreSQL` sebagai tipe basis data yang akan digunakan.
7. Sesuaikan versi Python dengan spesifikasi aplikasi. Pada kasus ini saya menggunakan python `versi 3.10`
8. Pada bagian Start Command masukkan perintah `python manage.py migrate && gunicorn concert_ticket_inventory.wsgi`.
9. Masukkan nama aplikasi yang juga akan menjadi nama domain situs web aplikasimu.
10. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses deployment aplikasi.

### Bagan request client ke web aplikasi berbasis django
![](img/Tugas2/Tugas2_Flow_Request_Client.png)

### Alasan Penggunaan `Virtual Environment`
Alasan penggunaan `Virtual Environment` adalah bertujuan untuk mengisolasi dependencies yang digunakan dalam pembuatan project ini. dengan menggunakan `Virtual Environment` dapat mengurangi resiko terjadinya konflik antar versi dependencies yang sama pada project yang berbeda. Selain itu, dengan menggunakan `Virtual Environment` Kolaborasi project akan jauh lebih mudah. hal ini disebabkan karena `Virtual Environment` memastikan bahwa semua orang yang terlibat pada project tersebut bekerja dalam 1 lingkungan. hal ini dapat menghindari masalah kompatibilitas antar sistem dan memastikan konsistensi dalam pengembangan. Sebenarnya tanpa perlu menggunakan `Virtual Environment` kita tetap dapat membuat project django. Namun banyak resiko atau masalah yang mungkin saja terjadi kedepannya.

### Perbedaan antara `MVC`, `MTV`, `MVVM`
*Model-View-Control* (MVC), *Model-View-Template* (MVT), *Model-View-View Model* (MVVM) ketiganya merupakan arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi, terutama dalam pengembangan aplikasi berbasis web. ketiga nya sama sama memiliki fungsi dalam memisahkan tampilan dengan logika dari program tersebut.

- MVC memisahkan tanggung jawab dalam tiga komponen utama untuk menghindari ketergantungan langsung antara Model dan View.
- MVT adalah pengembangan dari MVC yang menggantikan Controller dengan View dan Template. Ini memberikan pemisahan antara logika aplikasi dan tampilan.
- MVVM adalah pola yang mirip dengan MVC, tetapi menambahkan View Model sebagai perantara yang kuat antara Model dan View, dengan menggunakan teknik databinding untuk memastikan sinkronisasi otomatis antara keduanya.
