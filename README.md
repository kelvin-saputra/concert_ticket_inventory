# Concert Ticket Inventory Guide
**Nama  : Kelvin Saputra**

**NPM   : 2206027186**

**Kelas : PBP F**

**Link  : [Concert Ticket Inventory](https://kelvin-saputra-tugas.pbp.cs.ui.ac.id)**

## To Do List TUGAS 2
- [x] Membuat sebuah proyek Django baru.
- [x] Membuat aplikasi dengan nama main pada proyek tersebut.
- [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
- [x] Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    * name sebagai nama item dengan tipe CharField.
    * amount sebagai jumlah item dengan tipe IntegerField.
    * description sebagai deskripsi item dengan tipe TextField.

- [x] Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [x] Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
- [x] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [x] Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
     * Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
     * Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
     * Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
     * Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

### Membuat Project Django
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

## To Do List TUGAS 3
- [x] Membuat input form untuk menambahkan objek model pada app sebelumnya.
- [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
    * Apa perbedaan antara form POST dan form GET dalam Django?
    * Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    * Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    * Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
- [x] Melakukan `add`-`commit`-`push` ke GitHub

### Perbedaan Antara Form `POST` dan Form `GET`
Terdapat beberapa perbedaan antara Form `POST` dan Form `GET`. salah satu perbedaan yang paling kelihatan adalah ketika kita melakukan pengiriman/submit form, pada form dengan metode `POST` dikirim secara sembunyi atau tidak ditampilkan di url web. Sedangkan pada form dengan metode `GET` dikirim sebagai parameter query yang membuatnya terlihat pada url. Berikut perbedaan lebih rinci yang dapat kita ketahui.
- **Limitasi Ukuran Data** 
    * Pada metode `POST`, ukuran data akan terbatas sesuai dengan konfigurasi server.
    * pada metode `GET` karena akan dikirim sebagai parameter query yang ditampilkan pada url sehingga ukuran akan terbatas pada panjang url dan pembatasan server. url yang terlalu panjang dapat menyebabkan masalah/crash.
- **Keamanan**
    * Pada metode `POST`, karena pengiriman tersembunyi sehingga data yang dikirimkan tidak akan ditampilkan dan akan lebih aman karena data-data seperti password dan lain lain akan lebih aman.
    * Pada metode `GET`, karena pengiriman ditampilkan pada url sehingga data-data seperti password dan data krusial lain yang diinput pada form akan terlihat dan berpotensi untuk dicuri
- **Kecepatan**
    * Pada metode `POST` pengiriman lebih lambat karena disisipkan pada body request HTTP
    * Pada metode `GET` pengiriman lebih cepat karena hanya perlu mengekstrak url saja.
- **Penyimpanan Cache**
    * Pada metode `POST` data tidak disimpan dalam cache browser
    * Pada metode `GET` data disimpan dalam cache browser


### Perbedaan Antara `XML`, `JSON`, `HTML` dalam Konteks Pengiriman Data

Perbedaan antara `XML`, `JSON`, dan `HTML` adalah sebagai berikut.
- **Penggunaan**
    * `XML`, biasanya digunakan untuk pertukaran data antar aplikasi.
    * `JSON`, biasanya digunakan untuk pertukaran data antar server atau browser.
    * `HTML`, tidak digunakan sebagai pengiriman data, namun ditujukan untuk membangun tampilan suatu website.
- **Keamanan**
    * `XML`, Lebih aman untuk digunakan dalam pengiriman data yang bersifat krusial dan sensitif karena tidak muncul di url.
    * `JSON`, Kurang aman karena data akan ditampilkan pada url.
    * `HTML`, tidak digunakan dalam pengiriman data.
- **Struktur**
    * `XML`, Menggunakan tag untuk mengelompokkan suatu data sehingga dapat mendukung hierarki yang jauh lebih kompleks
    * `JSON`, Menggunakan pasangan antara `KEY` dan `VALUE` sehingga jauh lebih sederhana dan mudah untuk dibaca oleh orang yang awam
    * `HTML`, Menggunakan tag untuk mendefinisikan elemen tampilan pada suatu website

### Alasan `JSON` Sering Digunakan Dalam Pertukaran Data
`JSON` sering digunakan dalam pertukaran data karena memiliki banyak keuntungan yang bisa didapatkan. Salah satu manfaat yang bisa langsung dirasakan aalah kemudahan dalam membaca file dalam format `JSON`. Hal ini disebabkan karena sintaks `JSON` yang lebih sederhana dan penyajian data dalam bentuk pasangan `'KEY'` dan `'VALUE'`. Hal ini dapat memudahkan pengguna dalam menyimpan data yang kompleks dengan format yang lebih terstruktur. Selain itu, dengan menggunakan `JSON` memungkinkan kita untuk melakukan pertukaran data yang lebih efisien karena `JSON` tergolong dalam format data yang ringan dan penggunaan bandwidth yang lebih sedikit.

### Langkah Dalam Menambahkan Fitur Form dan Melihat Data Tersubmit
#### Membuat Kerangka TEMPLATE untuk project
1. Pertama kita akan buat terlebih dahulu kerangka utama html. Hal ini bertujuan agar pada berbagai template kita dapat langsung fokus ke dalam implementasi body suatu html/content.
2. Buat folder template pada `root` direktori lalu buatlah berkas `base.html` dengan isi sebagai berikut.
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
3. Setelah itu ubah pengaturan pada direktori `concert_ticket_inventory` lalu tambahkan <code>[BASE_DIR / 'templates']</code> pada `TEMPLATES` bagian `DIRS`. hal tersebut bertujuan agar kerangka tersebut dapat dibaca di berbagai aplikasi.

#### Membuat Form Input Data
1. Buatlah berkas `forms.py` pada direktori `main`. Isikan `forms.py` dengan membuat struktur form yang digunakan dalam input data.
2. Isikan file `forms.py` dengan kode berikut.
```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```
3. pada bagian `fields` list merupakan representasi input yang diinginkan dari user. sehingga masukkan seluruh data yang perlu diinput oleh user pada list tersebut. Perlu diingat bahwa model merupakan class yang dapat dibentuk object. namun jika ada perubahan struktur kita perlu untuk melakukan migrasi.

#### Membuat Fungsi Views untuk melihat objek yang ditambahkan
1. Tambahkan beberapa library yang akan digunakan. salah satunya adalah ItemForm yang kita buat sebelumnya pada `forms.py`.
2. Selanjutnya buat fungsi untuk menyimpan data secara otomatis ketika suatu item ditambahkan lewat form. Berikut adalah potongan fungsi yang dapat digunakan.
```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```
3. Penjelasan terkait form tersebut adalah pertama kita akan membuat form baru yang dimasukkan ke dalam variabel `form`. Lalu selanjutnya dilakukan pengecekkan apakah form tersebut valid, jika valid form akan disimpan lalu user akan di redirect.
4. Selanjutnya pada fungsi `show_main` kita perlu menambahkan dictionary dengan isi seluruh object `Item` yang telah dibuat dengan menggunakan kode <code>items = Item.objects.all()</code>. hal ini bertujuan agar kita bisa menampilkan data yang telah diinput pada halaman `main`. Selain itu pada fungsi `show_main` saya tambahkan variable yang menampung jumlah item yang telah ditambahkan.
5. Selanjutnya kita akan membuat halaman sederhana dengan nama `create_item.html` yang digunakan untuk input Form. Dengan kode berikut.
```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Ticket"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
6. Penggunaan kode <code>{% csrf_token %}</code> digunakan untuk token keamanan yang secara otomatis dibuat oleh python dengan tujuan untuk keamanan.
7. Setelah itu saya menambahkan tautan yang mengarah ke halaman `create_item.html` pada `main.html` dalam bentuk button dan saya menambahkan beberapa code berikut yang bertujuan untuk jummlah data yang tersimpan dan data-data tersimpan yang sudah disubmit melalui form tersebut.
```html
<p>"Kamu menyimpan {{count}} item pada aplikasi ini"</p>
    <table>
        <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Description</th>
            <th>Date Added</th>
        </tr>

        {% for ticket in tickets %}
            <tr>
                <td>{{ticket.name}}</td>
                <td>{{ticket.amount}}</td>
                <td>{{ticket.description}}</td>
                <td>{{ticket.date_added}}</td>
            </tr>
        {% endfor %}
    </table>
```
#### Membuat Fungsi Views yang Dapat Digunakan Untuk Menyimpan Data Tersimpan
1. Segala bentuk fungsi perlu kita buat dalam berkas `views.py`. Selanjutnya untuk mendukung pembuatan fungsi tersebut, saya melakukan import library seperti `HttpResponse` yang berfungsi untuk melakukan request http dan `Serializer` yang digunakan untuk konversi data kompleks seperti object python menjadi data yang mudah dikelola oleh klien seperti `JSON` dan `XML`.
2. Selanjutnya saya membuat fungsi `show_xml` dan `show_json` yang sebenernya secara struktur fungsi sama saja prosesnya. Namun terdapat perbedaan pada saat melakukan konversi seperti pada fungsi `show_xml` dikonversi menjadi data `XML` dan `show_json` dikonversi menjadi data `JSON`. kedua method sama sama menerima parameter request agar bisa dijalankan.
3. Selanjutnya buat fungsi serupa, namun perbedaan dengan fungsi sebelumnya adalah fungsi ini menggunakan `id` sebagai parameter. Sehingga data yang ditampilkan bukan data keseluruhan melainkan data yang sesuai dengan `id` yang diminta. fungsi ini saya beri nama `show_xml_by_id` dan `show_json_by_id`. kedua method tersebut sama, namun memiliki perbedaan pada saat konversi data.

#### Melakukan Routing URL
1. Pada bagian ini agar fungsi yang sudah kita buat pada `views.py` dapat digunakan, kita perlu melakukan routing pada `urls.py` yang ada pada direktori `main`.
2. Untuk melakukan routing, tambahkan path url ke dalam urlpatterns yang ada di berkas `urls.py` yang ada di direktori `main`.
3. path url yang perlu ditambahkan sebagai berikut.
    - path('create-item', create_item, name='create_item'),
    - path('xml/', show_xml, name='show_xml'),
    - path('json/', show_json, name='show_json'),
    - path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    - path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    Pada implementasi nanti, int:id akan diisikan dengan id item yang telah didaftarkan.

### Tangkapan Layar Penggunaan 5 Fungsi Views
Menggunakan fungsi `create_item`
![](img/Tugas3/Screenshot(555).png)
Menggunakan fungsi `show_xml`
![](img/Tugas3/Screenshot(556).png)
Menggunakan fungsi `show_json`
![](img/Tugas3/Screenshot(557).png)
Menggunakan fungsi `show_xml_by_id`
![](img/Tugas3/Screenshot(558).png)
Menggunakan fungsi `show_json_by_id`
![](img/Tugas3/Screenshot(559).png)

## To Do List TUGAS 4
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
- [x] Menghubungkan model Item dengan User.
- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
    * Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
    * Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    * Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
    * Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    * Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] Melakukan add-commit-push ke GitHub.

### Apa Itu `UserCreationForm`? 
`UserCreationForm` adalah salah satu built-in form atau form bawaan yang disediakan oleh Django untuk mengelola proses autentikasi user. Form ini digunakan secara khusus untuk membuat atau mendaftarkan user baru ke dalam aplikasi web. 
- **Kelebihan**:
    * Mudah Digunakan karena untuk menggunakan `UserCreationForm` kita hanya butuh untuk melakukan import dan form bisa digunakan langsung tanpa perlu mengatur logika dalam validasi input yang dimasukkan oleh user
    * `UserCreationForm` pada django sudah terintegrasi baik dengan sistem otentikasi bawaan django. sehingga dapat memudahkan kita dalam mengelola pengguna aplikasi yang sudah terdaftar
    * `UserCreationForm` memiliki validasi yang terintegrasi untuk memastikan data yang diinputkan oleh user sudah sesuai dengan persyaratan keamanan yang telah ditetapkan oleh Django.

- **Kekurangan**
    * `UserCreationForm` memiliki input field yang sangat terbatas. sehingga ketika kita membutuhkan field lain selain username dan password perlu menambahkan secara manual.
    * `UserCreationForm` memiliki logika yang terbatas hanya untuk pembuatan atau registrasi user baru ke dalam suatu aplikasi web. sehingga ketika kita ingin melakukan validasi seperti email atau nomor telepon tidak bisa menggunakan `UserCreationForm`.
    * `UserCreationForm` memiliki tampilan default yang kurang menarik dan terkesan terbentuk hanya dengan menggunakan element html saja. sehingga kita membutuhkan untuk pengembangan tampilan lebih lanjut.

### Perbedaan Autentikasi dan Otorisasi Dalam Konteks Django
**Autentikasi** mencakup proses memeriksa dan memastikan/ memverifikasi apakah suatu user yang diinputkan telah terdaftar pada aplikasi web. Sebagai contoh, ketika seseorang mencoba untuk masuk ke dalam akun mereka, autentikasi akan memastikan bahwa informasi seperti nama pengguna dan kata sandi yang mereka berikan benar dan cocok dengan yang ada dalam catatan sistem. Ini adalah lapisan pertama pertahanan website dalam menjaga keamanan sistem, mengidentifikasi siapa yang berusaha melakukan login. Sedangkan **Otorisasi** menentukan apa yang boleh dan tidak boleh dilakukan oleh pengguna atau entitas yang telah diotentikasi. Sebagai contoh, setelah seseorang berhasil masuk ke akun mereka, otorisasi akan menentukan apakah mereka diizinkan untuk melakukan tindakan tertentu, seperti mengedit data, menghapus informasi, atau hanya membaca tanpa mengubahnya pada halaman web. Ini memastikan bahwa akses ke sumber daya dan fungsionalitas web dikontrol sesuai dengan peraturan dan kebijakan yang telah ditetapkan.

### Apa itu `Cookies` dalam konteks aplikasi web? 
`Cookies` adalah suatu data kecil yang disimpan pada server web klien melalui web browser saat user mengunjungi suatu situs web. `Cookies` digunakan untuk menyimpan informasi tertentu yang dapat diakses dan digunakan kembali oleh server web saat user akan membuka website tersebut kembali di lain waktu. 

#### Langkah-langkah Django menggunakan `Cookies` untuk mengelola sesi pengguna
 1. Ketika seorang user pertama kali mengakses aplikasi web Django, server akan membuat sebuah `cookie` sesi baru. `Cookie` ini berisi ID unik yang digunakan untuk mengidentifikasi sesi user yang bersangkutan.
 2. ID sesi ini kemudian disimpan di dalam `cookie` di sisi klien. `Cookie` ini akan terkait dengan domain aplikasi web tertentu dan disimpan dalam web browser user.
 3. Setiap kali user membuat permintaan (request) berikutnya ke aplikasi web, `cookie` sesi ini akan disertakan dalam permintaan tersebut secara otomatis. Ini memungkinkan server untuk mengidentifikasi user yang terkait dengan sesi tertentu.
 4. Django memiliki mekanisme untuk menyimpan data sesi user, seperti informasi login user atau preferensi, di server. Data ini terkait dengan sesi yang sesuai melalui ID yang ada di `cookie`.
 5. Data sesi ini dapat diakses dan dimodifikasi oleh server saat user berinteraksi dengan aplikasi. Selain itu, data sesi digunakan untuk menjaga keadaan sesi user selama interaksi dengan aplikasi. Sebagai contoh, jika seorang user telah masuk ke akunnya, data sesi akan mencatat status login tersebut sehingga user tetap berada dalam kondisi login selama beberapa permintaan.

### Keamanan penggunaan `Cookies` dalam Pengembangan Web
Setiap perkembangan teknologi selalu memiliki celah keamanan yang dapat ditembus sewaktu-waktu. sehingga pada kasus ini, penggunaan `Cookies` belum tentu aman secara default dalam pengembangan web. terdapat beberapa resiko yang perlu diperhatikan sebagai berikut.

- `Cookies` dapat digunakan untuk menyimpan data sensitif, seperti informasi login atau ID pengguna. Sehingga jika tidak diperhatikan data sensitif seperti yang telah disebutkan berpotensi untuk dapat diakses oleh orang tidak bertanggung jawab.

- Melalui `Cookies`, pihak yang tidak bertanggung jawab dapat melacak aktivitas target di berbagai situs web. Hal ini tentu melanggar privasi user dalam internet.

- Keamanan `Cookies` sangat bergantung pada keamanan yang disediakan oleh web browser. Sehingga jika kita menggunakan web browser yang rentan, maka `Cookies` akan sangat rentan juga menjadi target serangan.

- Karena `Cookies` dapat dimodifikasi, jika tidak dilakukan pembersihan data yang baik, maka `Cookies` berpotensi untuk disisipkan script yang dapat membahayakan web.

-  `Cookies` yang digunakan untuk otentikasi rentan terhadap serangan CSRF jika tidak diatur dengan benar. Ini berarti penyerang dapat mencoba memanipulasi tindakan pengguna tanpa izin.

### Langkah dalam menambahkan user
#### Menjadikan aplikasi web dapat diakses jika user sudah login
1. Pertama kita perlu melakukan import method `login_required` yang digunakan untuk membatasi akses ke halaman main hanya kepada pengguna yang sudah login (terautentikasi).
2. sebelum kita menginisiasi method `show_main` kita perlu menambahkan code berikut
```python
@login_required(login_url='/login')
```
#### Implementasi Fungsi **Registrasi**
1. Pertama kali kita perlu untuk melakukan import method `UserCreationForm`.
2. Selanjutnya, buatlah method/fungsi `register` yang menerima parameter requests pada file `views.py` pada aplikasi main.
3. buatlah object form dengan menggunakan `UserCreationForm` yang secara otomatis akan memiliki struktur dan logika form tanpa perlu kita buat dari 0
4. Selanjutnya method akan mengarahkan ke halaman form yang telah kita buat sebelumnya untuk menambahkan user.
5. Namun, jika form yang disubmit oleh user valid, maka akan menampilkan pesan yang telah disesuaikan lalu kembali ke halaman login. 
6. Selain membuat method untuk register, kita perlu membuat file html yang digunakan untuk menampilkan form dan melakukan submisi form dengan nama `register.html`.

#### Implementasi Fungsi **Login**
1. Untuk membuat method/fungsi `login_user`, kita perlu melakukan import `authenticate` dan `login`. Fungsi `authenticate` digunakan untuk memverifikasi kredensial pengguna (username dan password), sedangkan `login` digunakan untuk memasukkan pengguna ke dalam sesi setelah berhasil `autentikasi`.
2. Selanjutnya buatlah method/fungsi `login_user` yang menerima parameter request pada file `views.py` pada aplikasi main yang digunakan untuk mengautentikasi user yang mencoba untuk login
3. Dalam fungsi `login_user`, gunakan fungsi `authenticate` untuk autentikasi pengguna berdasarkan username dan password yang diterima dari permintaan (request) pengguna saat proses login.
4. Selanjutnya kita perlu membuat file html yang digunakan untuk menampilkan tampilan form untuk login dan melakukan pengiriman data dengan nama file `login.html`.

#### Implementasi Fungsi **Logout**
1. Untuk membuat method/fungsi `logout_user`, kita perlu melakukan import method `logout` yang digunakan untuk mengatur proses utama dalam logout.
2. Selanjutnya buatlah method/fungsi `logout_user` yang menerima parameter request pada file `views.py` pada aplikasi main yang digunakan untuk implementasi mekanisme logout dalam aplikasi.
3. didalam fungsi `logout_user` dilakukan pemanggilan fungsi `logout(requests)` yang bertujuan untuk menghapus sesi pengguna yang saat ini masuk.
4. Setelah berhasil melakukan logout, Secara otomatis akan mengembalikan ke halaman user dengan syarat bahwa halaman aplikasi web hanya dapat diakses jika user telah login ke akun yang telah terdaftar
5. Untuk dapat melakukan logout, kita perlu menambahkan button logout pada file `main.html` yang bertujuan untuk mengakses fungsi `logout_user` yang ada di `views.py`

#### Melakukan Routing Fungsi baru pada `views.py`
1. Lakukan import terhadap seluruh fungsi yang sudah kita buat pada `views.py` seperti `register`, `login_user`, `logout_user`.
2. Selanjutnya tambahkan urlpattern dengan path yang bersesuaian dengan fungsi yang kita miliki sebagai berikut.
```python
path('login/', login_user, name='login')
path('register/', register, name='register')
path('logout/', logout_user, name='logout')
```

#### Membuat 2 akun dengan 3 dummy data
1. Selanjutnya untuk membuat akun kita perlu menjalankan web tersebut melalui perintah <code>python manage.py runserver</code>.
2. Selanjutnya kita perlu membuka http://localhost:8000/ yang akan langsugn terhubung ke halaman login.
3. kita perlu membuat akun terlebih dahulu. disini saya akan membuat akun sebagai berikut
    - akun 1
        * username : RodStewart
        * password : lagu1990
    - akun 2
        * username : CharliePuth
        * password : lightswitch
4. Selanjutnya lakukan login dengan menggunakan akun yang telah didaftarkan diatas. 
5. Setelah berhasil login klik tombol `Add New Ticket` untuk menambahkan produk sesuai user yang berhasil login.

#### Menghubungkan Model `Item` dengan `User`
1. Pertama kita perlu melakukan import Model `User`ke dalam berkas `models.py` yang ada pada aplikasi `main`.
2. selanjutnya pada model `Item`, saya menambahkan sebuah atribut baru bernama `user` dimana tiap objek `Item` akan berelasi dengan satu objek `User` dengan ForeignKey.
```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
``` 
3. Lakukan perubahan fungsi `create_item` yang ada dalam berkas `views.py` perubahan ini mencakup code berikut.
```python
item = form.save(commit=False)
item.user = request.user
```
pada line 1 digunakan agar form tidak langsung disimpan ke dalam database
sedangkan pada line 2 kita mengubah pemilik item menjadi user yang terautentikasi/sedang login
4. Terakhir jangan lupa untuk melakukan migrasi karena terdapat perubahan pada model.

#### Menampilkan `Username` user yang sedang login
1. untuk menampilkan username yang sedang login, kita hanya perlu mengubah isi dari dictionary context pada fungsi `show_main` dengan `request.user.username`. Hal ini bertujuan untuk menampilkan username pengguna yang saat ini login pada halaman utama, sehingga pengguna dapat melihat dengan jelas akun yang mereka gunakan.

#### Menampilkan waktu `Last Login` dari user
1. Untuk menampilkan kapan terakhir kali user melakukan login, kita perlu melakukan import `datetime` untuk mengambil waktu.
2. Untuk mengambil informasi waktu kapan terakhir kali user melakukan login, kita perlu melakukan `SET_COOKIE` saat user berhasil melakukan login dengan nama `last_login` dan menambahkannya ke dalam respons. `Cookie` ini akan berisi informasi waktu saat pengguna terakhir kali melakukan login.
3. Pada fungsi `show_main` kita perlu menambahkan variabel tambahan pada `context` sebagai berikut. <code>last_login': request.COOKIES['last_login']</code>
4. Selanjutnya kita perlu set ketika user melakukan logout atau keluar dari aplikasi main, maka kita perlu menghapus `Cookies` `last_login` dengan menggunakan perintah <code>response.delete_cookie('last_login')</code>
5. Terakhir agar informasi last login dapat ditampilkan pada aplikasi main, kita perlu menambahkan elemen baru di `main.html` seperti berikut.
```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

## To Do List TUGAS 5
- [x]Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut
- [x] Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.
- [x] Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card. 
- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder.
    * Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
    * Jelaskan HTML5 Tag yang kamu ketahui.
    * Jelaskan perbedaan antara margin dan padding.
    * Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
    * Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] Melakukan add-commit-push ke GitHub.

### Jelaskan Manfaat dari setiap Elemen Selektor!
Berdasarkan yang saya ketahui, selektor merupakan suatu penanda dalam CSS untuk mengedit suatu blok elemen dalam `HTML`. terdapat beberapa selektor yang dapat terbagi menjadi berikut.
- ***Selektor Universal***
    * Selektor Universal adalah suatu selektor yang dapat mempengaruhi atau merubah seluruh gaya element dalam dokumen `HTML`. Waktu yang tepat untuk menggunakan selektor universal adalah ketika kita ingin menggunakan suatu ketentuan style yang sama dalam dokumen `HTML`. Sebagai contoh adalah padding, margin, font, dll.

- ***Selektor Tag***
    * Selektor Tag adalah suatu selektor yang dapat digunakan untuk mengubah style dari suatu tag HTML. dalam hal ini, misal kita ingin mengubah seluruh style pada tag `<h1>`. Maka kita dapat gunakan selektor tag untuk memberikan style pada seluruh `<h1>`.  kita dapat gunakan selektor tag ini untuk mengubah seluruh gaya pada suatu tag seperti yang dicontohkan sebelumnya.

- ***Selektor ID***
    * Selektor `ID` adalah selektor yang digunakan untuk mengubah style yang ada pada `ID` suatu blok `HTML`. Biasa digunakan untuk memberikan suatu style yang unik pada suatu `ID`.

- ***Selektor Kelas***
    * Selektor kelas adalah selektor yang digunakan untuk mengubah style yang ada pada suatu class. biasa digunakan untuk memberikan style pada suatu element yang memiliki class yang sama.

### Tag-tag HTML5
- `<header></header>`
    * digunakan untuk memberikan header pada halaman web yang didalamnya bisa saja berisi navigasi judul atau logo dari pemilik website tersebut/
- `<nav></nav>`
    * digunakan untuk menampung navigasi bar halaman website
- `<main></main>`
    * digunakan untuk menampung konten utama dari suatu website.
- `<article></article>`
    * Mengelompokkan konten-konten yang secara terpisah dapat diubah-ubah.
- `<aside></aside>`
    * untuk menampung konten tambahan yang ada di samping dari konten utama.
- `<section></section>`
    * Mengelompokkan konten-konten menjadi bagian yang terpisah. Sebenarnya sama saja dengan tag `<article></article` namun tag `<section></section>` lebih meluas ketimbang `<article></article`.
- `<footer></footer>`
    * Digunakan untuk memberikan bagian bawah pada halaman web. seperti informasi hak cipta, informasi pemiliki website, dan beberapa navigasi sederhana.
- `<figure></figure>`
    * digunakan untuk menampilkan gambar atau grafik pada halaman web
- `<canvas></canvas>`
    * digunakan untuk memberikan user suatu ruang untuk menggambar.
- `<form></form>`
    * digunakan untuk mengelompokkan/membuat form pada website yang memungkinkan pengguna untuk mengirimkan data ke server
- `<input></input>`
    * digunakan untuk melengkapi form yang kita buat seperti membuat textfield, checkbox, button, dll
- `<button></button>`
    * digunakan untuk membuat tombol untuk melakukan suatu action.
- `<a></a>`    
    * Digunakan untuk membuat atau menampilkan suatu link/hyperlink kepada user di halaman website.
- `<table></table>`
    * Digunakan untuk membaut table pada halaman website. biasanya dibantu dengan tag-tag lain seperti
        *  `<th></th>` : tag ini digunakan untuk membuat header kolom pada table
        *  `<tr></tr>` : tag ini digunakan untuk membuat row pada table
        *  `<td></td>` : tag ini digunakan untuk membuat nilai-nilai atau value pada table
- `<div></div>`
    * digunakan untuk mengelompokkan sesuatu secara satu kesatuan. secara kasar `<div></div>` dapat diartikan sebagai kontainer pada suatu fitur.
- `<span></span>`
    * digunakan untuk mengubah suatu tulisan secara khusus
- `<video></video>`
    * Digunakan untuk membuat media player video
- `<audio></audio>`
    * Digunakan untuk membuat media player audio

### Perbedaan antara Margin dan Padding
Perbedaan antara `padding` dan margin adalah sebagai berikut.
- Fungsi Utama
    * `Padding` digunakan untuk menberikan ruang kosong antara konten/elemen dengan border dari konten/elemen itu sendiri. Dengan kata lain, `padding` merupakan ruang kosong secara internal atau mengosongkan ruang ke dalam elemen itu sendiri.
    * `Margin` digunakan untuk memberikan ruang kosong antara satu elemen/konten dengan elemen/konten lain. Dengan kata lain, `margin` merupakan ruang kosong secara eksternal atau mengosongkan ruang ke luar dari elemen itu sendiri.
- Posisi
    * `Padding` berada diantara konten elemen dengan border
    * `Margin` berada diantara elemen 1 dengan elemen lainnya.
- Pengaruh Ukuran Total
    * `Padding` dapat mempengaruh ukuran total dari elemen. sehingga ukuran asli dari elemen akan ditambahkan dengan padding.
    * `Margin` tidak mempengaruhi ukuran total dari suatu elemen.
- *Background Color*
    * `Padding` dapat memiliki warna background mengikuti elemen dan konten itu sendiri
    * `Margin` tidak dapat memiliki warna background 

### Perbedaan antara *framework* CSS Tailwind dan Bootstrap
Perbedaan antara Tailwind dan Bootstrap adalah sebagai berikut.
- Kustomisasi
    * `Tailwind` sangat fleksibel dalam hal kustomisasi. Hal ini dapat memungkinkan kita menyesuaikan tampilan dengan sangat detail.
    * `Bootstrap` bisa dikustomisasi namun relative lebih sulit dibandingkan menggunakan `Tailwind`
- Ukuran File
    * `Tailwind` ukuran filenya lebih kecil karena tidak terlalu banyak komponen pra desain sehingga kita perlu melakukan kustomisasi secara mandiri
    * `Bootstrap` ukuran filenya lebih besar dibandingkan tailwind karena banyak komponen pra desain
- Jumlah Kelas
    * pada `Tailwind` kelas bisa ditambahkan langsung ke HTML yang membuat kita dapat lebih mudah untuk mengatur/memiliki kontrol yang lebih besar terhadap tampilan dan element itu sendiri
    * pada `Bootstrap` kelas CSS sudah ditetapkan yang membuat code menjadi lebih bersih namun kontrol yang tidak terlalu besar.
Penggunaan `Tailwind` dan `Bootstrap` bergantung pada beberapa aspek sebagai berikut
- Tailwind
    * Digunakan ketika kita memiliki kemampuan atau ilmu design yang lebih sehingga dapat lebih leluasa dalam melakukan design
    * Digunakan untuk menghasilkan tampilan website yang lebih baik dan sesuai dengan keinginan.
- Bootstrap
    * Digunakan ketika tidak banyak ilmu design yang dimiliki sehingga dapat memanfaatkan banyaknya komponen pra desain pada bootstrap
    * Desain yang diinginkan tidak begitu berbeda jauh dengan komponen pada bootstrap
    * Tidak memiliki waktu yang banyak untuk membuat project 

### Jelaskan Langkah-Langkah dalam memenuhi check list
#### Melakukan importing bootstrap ke dalam projek 
- Sebelum melakukan design/kustomisasi halaman web, hal yang perlu dilakukan adalah menyisipkan static file bootstrap ke dalam template `base.html`. Langkah ini menjadi sangat penting karena bertujuan agar kita dapat menggunakan pra-komponen langsung dari bootstrap.

#### Melakukan Kustomisasi pada halaman login, register, add item, dan edit item.
- Setelah melakukan import, hal yang saya lakukan untuk memodifikasi halaman-halaman tersebut adalah dengan membuat nya menjadi dalam 1 kontainer
- Setelah itu, lakukan pengaturan pada padding dan margin agar sesuai dengan yang diinginkan
- Untuk membuatnya menjadi fokus utama dalam suatu halaman web, saya membuat seluruh elemen menjadi `center`.
- Setelah itu saya menambahkan tombol tindak lanjut dan tombol kembali yang dapat digunakan user untuk membatalkan suatu proses dengan memanfaatkan btn bawaan dari bootstrap.
- Setelah itu saya melakukan modifikasi tata letak form seperti antara label dengan field isi saya buat menjadi atas bawah sehingga kita tidak perlu mengukur padding antar konten.
- Selanjutnya dengan memanfaatkan kelas pada bootstrap, saya dapat dengan mudah untuk mengganti warna tombol tombol yang ada pada halaman web.

#### Melakukan Kustomisasi pada tampilan main
- Pertama saya membuat bar navigasi yang bertujuan untuk memudahkan user untuk memilih menu.
- Untuk sementara saya memasukkan navigasi yang dapat mengarahkan website ke `main`, melakukan `add_ticket`, dan `logout`.
- Tidak lupa saya tambahkan nama user yang login ke dalam bar navigasi.
- Untuk menampilkan inventory yang sudah berhasil di inputkan, saya mengubah tampilan dari yang awalnya menggunakan pendekatan tabel, sekarang saya menggunakan pendekatan card.
- saya memberikan tiap card menu yang dapat digunakan seperti menambahkan dan mengurangkan amount, mengedit data, dan menghapus data.
- Seluruh menu tersebut saya sajikan dalam bentuk button yang diberikan warna yang berbeda dengan bantuan dari framework bootstrap.
Setelah itu saya memberikan tombol-tombol tersebut terhubung dengan logic program yang ada di `views.py` melalui `urls.py` 

## To Do List TUGAS 6
 - [x] Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
    * [x] AJAX GET
        + Ubahlah kode tabel data item agar dapat mendukung AJAX GET.
        + Lakukan pengambilan task menggunakan AJAX GET.

    * [x] AJAX POST
        + Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.
        + Modal di-trigger dengan menekan suatu tombol pada halaman utama. Saat penambahan item berhasil, modal harus ditutup dan input form harus dibersihkan dari data yang sudah dimasukkan ke dalam form sebelumnya.
        + Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.
        + Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.
        + Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.
        + Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.

    * [x] Melakukan perintah collectstatic.
        + Perintah ini bertujuan untuk mengumpulkan file static dari setiap aplikasi kamu ke dalam suatu folder yang dapat dengan mudah disajikan pada produksi.

- [x] Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
    * Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
    * Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    * Jelaskan penerapan asynchronous programming pada AJAX.
    * Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
    * Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Melakukan add-commit-push ke GitHub.

- [x] Melakukan deployment ke PaaS PBP Fasilkom UI dan sertakan tautan aplikasi pada file README.md.

### Perbedaan Antara *Asynchronous Programming* dan *Synchronous Programming*
- Pengertian
    * Asynchronous Programming merupakan salah satu pendekatan dalam pemrograman yang memungkinkan suatu perintah dapat dijalankan secara bersamaan tanpa perlu menunggu perintah lain selesai untuk dieksekusi. dengan kata lain, Asynchronous Programming merupakan teknik dalam pemrograman yang tidak bergantung pada I/O sehingga dapat menjalankan perintah dengan lebih dinamis.
    * Synchronous Programming merupakan salah satu pendekatan dalam pemrograman dimana perintah akan dieksekusi secara sequential atau berdasarkan urutan dan prioritas.
- *Blocking*
    * Pada proses Asynchronous programming tidak terdapat blocking. sehingga untuk tugas-tugas yang memakan waktu lebih lama tetap bisa untuk dijalankan di latar belakang aplikasi sehingga tidak mengganggu proses lainnya.
    * Pada proses Synchronous Programming terdapat blocking. dampak dari adanya blocking adalah ketika terdapat tugas yang memiliki waktu yang lebih lama dapat menghambat proses lain karena perintah dijalankan secara pararel sehingga ketika terdapat proses yang lama maka perintah lain tidak dapat dieksekusi.
- Kecepatan
    * dalam konteks pemrograman berbasis platform ini, kecepatan dari program yang menggunakan pendekatan Asynchronous programming akan lebih cepat ketika website membutuhkan akses ke data ke database.

### Apa itu Paradigma *Event Driven Programming*?
Paradigma *Event Driven Programming* adalah sebuah paradigma pemrograman yang berfokus pada pengendalian(handling) event yang diberikan oleh user. Event tersebut meliputi Mouse Event, Keyboard Event, Form Event. Salah satu penerapan *Event Driven Programming* yang diimplementasikan dalam tugas 6 ini adalah pembuatan menu popup yang dapat digunakan untuk menambahkan item pada inventory dengan menggunakan AJAX.
### Jelaskan penerapan *asynchronous programming* pada AJAX.
Penerapan Asynchronous Programming dalam AJAX berupa teknik dalam pengembangan web yang memungkinkan komunikasi antara peramban web dan server web untuk dilakukan secara asinkron, tanpa harus me-refresh seluruh halaman web. Berikut adalah penjelasan mengenai penerapa Asynchronous Programming dalam AJAX lebih mendalam.
1. Pengiriman Requests HTTP
    Dalam konteks ini, ketika kita melakukan pengiriman permintaan AJAX, kita tidak perlu menahan eksekusi kode sampai respons dari server tiba. Dengan kata lain, kita dapat  mengirimkan permintaan dan melanjutkan dengan eksekusi kode lainnya, sementara notifikasi atau event akan memberitahu kita ketika respons dari server telah siap untuk diproses.
2. Event Handling
    Implementasi ini dapat kita temui ketika  setelah kita mengambil data dari server atau mengirimkan data ke server, sebuah event akan dipicu. Di sini, kita dapat mengonfigurasi event handler untuk merespons data yang kita terima. Ini bisa berarti memperbarui tampilan pengguna dengan data baru atau menjalankan tindakan tertentu berdasarkan respons yang diterima.
3. Callback Function
    Callback functions adalah alat yang sering digunakan dalam AJAX untuk menentukan apa yang harus dilakukan ketika respons dari server telah diterima. Callback function merupakan fungsi JavaScript yang akan dijalankan ketika operasi asinkron selesai. Misalnya kita dapat menggunakan callback function sukses (success) untuk mengelola respons yang berhasil dan callback fungsi error untuk menangani kesalahan jika permintaan AJAX mengalami kegagalan.
4. Promises dan async/await
    Dengan menggunakan Promises,kita dapat menghindari "callback hell" dan membuat kode lebih rapi, sedangkan async/await memungkinkan kita untuk menulis kode yang tampak seperti sinkron meskipun sebenarnya berjalan secara asinkron.

### Perbandingan antara kedua teknologi Fetch API dan Library jQuery

|       | Fetch API | jQuery |
|-------| :-------: | :----: |
| Keberadaan dalam JavaScript | Bagian dari JavaScript modern (ECMAScript) dan tidak perlu download atau pustaka tambahan. | Pustaka JavaScript terpisah yang perlu di download dan masukkan ke dalam proyek. |
| Manajemen Request | Fetch API mengembalikan objek Promise, yang memudahkan untuk mengelola requests dengan cara yang bersih dan terstruktur.|  jQuery menggunakan pendekatan callback-based untuk manajemen requests, yang bisa menjadi kurang bersih dan membingungkan jika terdapat banyak requests bersarang. |
| Flekbilitas | lebih banyak kontrol atas requests HTTP, seperti mengatur header, metode, mode requests (cors, same-origin, dll.). | jQuery menyederhanakan permintaan AJAX sederhana dan tidak memberikan kontrol sebanyak Fetch API. |
| Handling Response | Fetch API menyediakan metode built-in seperti json(), text(), dan lainnya untuk mengelola berbagai jenis respons dengan mudah. | jQuery memiliki metode built-in yang memfasilitasi pengolahan respons, seperti $.getJSON() untuk mengambil data JSON dan $.ajax() untuk pengaturan kustom. | 
| Compatibility | Terbatas di beberapa peramban lama. | Memiliki compatibility yang baik untuk peramban lama. |

Berdasarkan perbandingan yang dijabarkan sebelumnya, menurut saya Fetch API lebih baik digunakan pada masa sekarang. khususnya untuk project project dalam skala yang besar dan kompleks. Selain itu, kita tidak perlu melakukan instalasi dan repot untuk menambahkannya ke dalam projek. Namun, jika kita sedang mengerjakan projek yang kecil dan menggunakan akses dari peramban lama, jQuery akan menjadi pilihan yang baik.

### Jelaskan langkah-langkah dalam memenuhi CheckList
#### Membuat fungsi `get_item_json`
1. Implementasikan fungsi `get_item_json` yang digunakan untuk mengambil seluruh objek `Item` yang telah dibuat sebagai berikut.
```python
def get_item_json(request):
    item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', item))
```
2. Fungsi tersebut akan mengembalikan seluruh objek `Item` yang telah dibuat dengan format yang telah dikonversi menjadi `JSON`

#### Membuat fungsi `add_item_ajax`
1. Implementasikan fungsi `add_item_ajax` yang digunakan untuk membuat item seperti berikut.
```python
@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```
2. Dengan menggunakan `@csrf_exempt`, program akan mengabaikan keamanan dalam pembuatan objek menggunakan AJAX sehingga program akan menjadi jauh lebih sederhana

#### Perubahan pengambilan data item menggunakan AJAX
1. Pertama yang saya lakukan adalah mengubah card item yang terhubung langsung dengan objek `Item` melalui looping menjadi suatu container kosong yang akan menampung `Card Item` tersebut. 
```html
<div class="container" id="item_container">
```
2. Selanjutnya saya akan membuat fungsi asynchronous pada javascript agar proses berjalan pada background dan tidak menunggu proses tersebut selesai.
3. Fungsi asynchronous pertama yang saya buat adalah `getItems` yang berfungsi untuk mengambil semua object `Item` dengan implementasi sebagai berikut.
```javascript
async function getItems() {
        return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
    }
```
4. Selanjutnya dengan memanfaatkan fungsi `getItems` dan id `item_container`, saya membuat fungsi `refreshItem` yang akan meloading seluruh item yang didapatkan melalui pemanggilan `getItems` untuk dimasukkan ke dalam `card` yang selanjutnya akan disisipkan pada innerHTML `item_container`. Berikut adalah implementasi dari fungsi `refreshItem`.
```javascript
async function refreshItem() {
        document.getElementById("item_container").innerHTML = ""
        const items = await getItems()
        let htmlString = `
            <div class="row">`

        items.forEach((item) =>{
            htmlString += `
                <div class="col-md-4 mb-4 my-5" data-item-id="${item.pk}">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">${item.fields.name}</h5>
                            <p class="card-text"><strong>Amount:</strong> ${item.fields.amount}</p>
                            <p class="card-text"><strong>Description:</strong> ${item.fields.description}</p>
                            <p class="card-text"><strong>Date Added:</strong> ${item.fields.date_added}</p>
                        </div>
                        <div class="card-footer">
                            <a href="min_amount/${item.pk}" class="btn btn-danger">MIN</a>
                            <a href="add_amount/${item.pk}" class="btn btn-success">ADD</a>
                            <a href="edit_data/${item.pk}" class="btn btn-info">EDIT</a>
                            <a href="delete_data/${item.pk}" class="btn btn-warning">DELETE</a>
                        </div>
                    </div>
                </div>`
        })
        htmlString += `\n</div>`
        document.getElementById("item_container").innerHTML = htmlString
    }
```
5. `htmlString` merupakan potongan code html yang yang akan disisipkan dalam innerHTML dari id `item_container`.

#### Pembuatan Modal Form menggunakan AJAX POST
1. Untuk membuat model ini saya akan memanfaatkan fungsi `add_item_ajax` yang ada pada file `views.py` agar item yang ditambahkan melalui form dapat disimpan ke dalam database
2. Agar fungsi `add_item_ajax` dapat digunakan dalam file html dan scriptnya, kita perlu melakukan routing dengan cara menambahkan path fungsi tersebut kedalam urlpattern yang ada di `urls.py`
3. selanjutnya tambahkan kode berikut ke dalam file HTML yang kita miliki
```html
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Item</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="amount" class="col-form-label">Amount:</label>
                        <input type="number" class="form-control" id="amount" name="amount"></input>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                </form>
            </div>
            <div c lass="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal" >Add Item</button>
            </div>
        </div>
    </div>
</div>
```
code html tersebut digunakan merupakan kode form yang akan tampil jika suatu button form akan dibuat.
4. Untuk itu kita perlu menambahkan button yang dapat memunculkan popup form tersebut sehingga form tersebut akan muncul ketika kita menekan tombol tersebut.
```html
<button type="button" class="btn btn-primary mx-auto" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Item by AJAX</button>
```
5. selanjutnya kita perlu menghubungkan modal form tersebut dengan suatu fungsi. sehingga ketika kita memasukkan atau melakukan submisi form, data-data yang ada dalam form dapat ditangkap oleh program dan disimpan ke dalam database.
6. Fungsi yang saya buat adalah fungsi `addItem` fungsi ini akan memanggil fungsi `add_item_ajax` yang ada pada file `views.py` sehingga data dapat ditangkap dan disimpan dalam database. Selain itu pada fungsi tersebut saya akan melakukan refresh namun secara asynchronous sehingga tidak seluruh halaman utama di refresh lalu mengosongkan form yang sudah di submit tadi. implementasi code sebagai berikut.
```javascript
function addItem() {
        fetch("{% url 'main:add_item_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshItem)
        
        document.getElementById("form").reset()
        return false
    }
```
7. agar tombol submisi pada form dapat terhubung dengan fungsi tersebut saya akan menambahakn penghubung agar ketika tombol submit di klik, kita akan memanggil fungsi javascript `addItem`. berikut adalah implementasi dari code tersebut
```javascript
document.getElementById("button_add").onclick = addItem
```

#### Melakukan Collectstatic 
1. Untuk melakukan `collectstatic` saya membuka terminal lalu masuk ke dalam direktori project ini berada.
2. Selanjutnya saya masuk ke dalam virtual environment dengan cara memasukkan code berikut ke dalam terminal
```shell
env\Scripts\activate.bat
```
3. Setelah di dalam virtual environment, saya akan mengumpulkan seluruh file static yang ada pada seluruh aplikasi yang saya buat dalam proyek ini, lalu saya kumpulkan ke dalam satu folder khusus dengan menjalankan perintah sebagai berikut.
```shell
python manage.py collectstatic
```