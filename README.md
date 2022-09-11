# Project Machine Learning Expert 2-Ridwan Akmal

## **Project Overview**
### **Latar Belakang**
Menurut K. R. P. Dewi and I. N. Sunarta (2021) dalam jurnalnya yang berjudul [“Evaluasi Kebijakan Pemberlakuan Pembatasan Kegiatan 
Masyarakat (PPKM) Darurat Jawa-Bali Dalam Menanggulangi COVID-19 Di Kota 
Denpasar”](jpurnal.umpr.ac.id) menyatakan bahwa sejak virus COVID-19 menyebar ke seluruh penjuru dunia, Indonesia mulai ikut menerapkan kebijakan pembatasan mobilitas untuk masyarakat bernama Pembatasan Sosial 
Berskala Besar (PSBB). Sistem PSBB ini memaksa warga untuk tidak bepergian keluar rumah jika tidak terpaksa. Hal ini membuat banyak orang mendapatkan waktu luang di luar pekerjaan maupun sekolah. Waktu luang ini biasanya dimanfaatkan oleh sebagian orang untuk menikmati hobi mereka, seperti membaca buku ataupun menonton film. Dengan banyaknya jumlah buku maupun film yang beredar saat ini, tidak dipungkiri membuat banyak dari masyarakat kita  kebingungan untuk memilah dan menyaring buku atau film yang sesuai dengan preferensi mereka. Maka dari itu, dibuatlah sistem rekomendasi untuk penikmat buku dan film guna memperluas bacaan maupun tontonan yang sesuai dengan preferensi mereka. <br> Sistem rekomendasi adalah sebuah sistem yang mengacu pada memprediksi sejumlah item atau data untuk pengguna di masa mendatang, kemudian dijadikan rekomendasi item paling teratas. Salah satu alasan mengapa perlu digunakannya Sistem rekomendasi karena pengguna memiliki banyak pilihan untuk digunakan karena prevalensi internet. Meskipun jumlah informasi yang tersedia meningkat, masalah baru muncul karena para pengguna kesulitan memilih item yang ingin mereka lihat. Di sinilah Sistem rekomendasi masuk. <br>
Dari latar belakang tersebut saya akan memaparkan mengapa proyek ini penting untuk diselesaikan. Hal pertama karena sistem rekomendasi yang nantinya dibangun dapat memudahkan masyarakat untuk melihat rekomendasi buku lain ketika misalnya berbelanja di toko buku secara daring maupun langsung(luring). Dengan membaca _pattern_ yang ada pada data, saya rasa kita akan lebih mudah untuk  merekomendasikan buku kepada masyarakat. Selain itu kita dapat membantu masyarakat dalam memberikan referensi buku misalnya saja masyarakat senang dengan pengarang X kita dapat merekomendasikan kepada dia buku lain yang dikarang oleh pengarang X yang nantinya ini akan dijabarkan lebih rinci di teknik _Content-Based Filtering_, di sisi lain  kita juga mendapat keuntungan yang besar yakni dapat meningkatkan minat membaca masyarakat Indonesia yang masih tergolong rendah. 

## **Business Understanding**
### **Problem Statement**
Berdasarkan latar belakang di atas, permasalahan yang akan diselesaikan pada proyek ini adalah sebagai berikut:

* Bagaimana membangun sebuah sistem untuk merekomendasikan buku yang yang sesuai dengan preferensi pengguna dengan teknik _Content-Based Filtering_?
* Bagaimana membangun sebuah sistem untuk merekomendasikan buku yang yang sesuai dengan preferensi pengguna dengan teknik _Collaborative Filtering_?
* Bagaimana cara melakukan pengelolahan data agar menghasilkan sistem rekomendasi yang baik dan relevan bagi masyarakat?

### **Goals**
Tujuan dibuatnya proyek ini adalah sebagai berikut:

* Membangun model machine learning dan deep learning untuk merekomendasikan sebuah buku yang sesuai dengan preferensi pengguna dengan teknik Content-Based Filtering dan Collaborative Filtering.
* Dapat Melakukan pengolahan data yang baik agar model yang dibangun dalam sistem rekomendasi dapat mengenali _pattern_ yang ada dengan baik.



### **Solution Approach**
Solusi yang dapat diterapkan agar goals diatas terpenuhi adalah sebagai berikut:

* Melakukan analisa pada data seperti: Melihat sebaran data, Memeriksa missing value dan duplikasi data.
* Melakukan pemrosesan pada data seperti _Merging_ antara tabel ratings dan books, Normalisasi data rating, Melakukan _Scalling_ dan _Encoding_ agar data dapat dengan mudah di proses oleh model.
* Membangun sistem rekomendasi menggunakan 2 teknik yang telah disebutkan di awal yaitu Content-Based Filtering dan Collaborative Filtering. 


## **Data Understanding**
Dataset yang di gunakan pada proyek machine learning ini merupakan dataset buku dan rating dari user. Dataset dapat di unduh di website kaggle: [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset).

Terdapat 3 file pada dataset, antara lain:
* Books.csv
* Ratings.csv
* Users.csv

Pada proyek ini saya hanya akan memanfaatkan 2 file data, yaitu:
* Books.csv</br>
    File ini memiliki total jumlah 271360 data buku, 8 jumlah kolom. Berikut adalah penjelasan untuk masing-masing variabel:</br>
    * ISBN:  International Standard Book Number(bersifat unik).
    * Book-Title: Judul Buku.
    * Book-Author: Nama pengarang buku.
    * Year-Of-Publication: Tahun penerbitan buku.
    * Publisher: Pihak penerbit buku.
    * Image-URL-S: URL cover berukuran kecil.
    * Image-URL-M: URL cover berukuran normal.
    * Image-URL-L: URL cover berukuran besar.

* Ratings.csv</br>
    File ini memiliki total jumlah 1149780 data rating, 3 jumlah kolom. Berikut adalah penjelasan untuk masing-masing variabel:</br>
    * User-ID: Nomor unik user yang memberikan rating.
    * ISBN:  International Standard Book Number(bersifat unik).
    * Book-Rating: Skor dari rating buku yang diberikan.

Berikutnya kita akan melakukan tahapan EDA, hal-hal yang dilakukan antara lain:
* Memeriksa informasi singkat dari data:
  * Books
  








