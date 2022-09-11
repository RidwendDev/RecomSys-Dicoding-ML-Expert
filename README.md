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
  <img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/Screenshot%202022-09-11%20072722.png?raw=true'>
  
  Berdasarkan data books tersebut terdapat 271360 entri dan seluruh tipe data dalam kolom books adalah object.
  <img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/judul.png?raw=true'>
  
  Dari data ini dapat kita lihat judul buku paling banyak adalah Selected Poems diikuti Little women dan Wuthering Heights.
  <img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/author.png?raw=true'>
  
  Dari data ini dapat kita lihat pengarang buku paling banyak adalah Agatha Cristie diikuti William Shakespeare dan Stephenn King.
  <img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/pnrbit.png?raw=true'>
  
  Dari data ini dapat kita lihat penerbit buku paling banyak adalah Harlequin diikuti Siihoute dan Pocket.
  
  * Ratings
  <img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/ingporating.png?raw=true'>
  
  Didalam data ratings terdapat 1149780 entri dan terdapat 2 tipe pada data yaitu number(int64) untuk User-ID dan Book-Rating serta object untuk ISBN.<br>
  <img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/vizrating.png?raw=true'>
  
  Terlihat dari visualisasi bahwa range rating ada diantara nilai 0 sampai dengan 10 dan buku paling banyak adalah dengan rating 0 dari user yang sebanyak 716109       buku.
  
* Memeriksa mising value
<img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/msvalue.png?raw=true'>

Terlihat bahwa terdapat beberapa kolom yang memiliki nilai missing value pada data book sedangkan untuk ratings bersih tanpa missing value

## **Data Preparation**
Data preparation ini diperlukan untuk mempersiapkan data agar ketika dilakukan proses pengembangan model kita mendapatkan hasil rekomendasi yang baik. Yang saya lakukan dalam tahap _Data Preparation_ kali ini antara lain:

* Menghapus data yang tidak diperlukan</br>
<img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/sleksifiktur.png?raw=true'>

Sistem rekomendasi yang saya bangun hanya memerlukan data author dan rating sebagai fitur untuk model. Kolom-kolom data seperti `Year-Of-Publication, Publisher, Image-URL-M, Image-URL-L` tidak akan saya gunakan untuk sistem rekomendasi dengan teknik _Content-Based Filtering_.

* Melakukan penggabungan data</br>
<img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/mergingdata.png?raw=true'>

Menggabungkan data buku dan rating menjadi satu sehingga dapat memudahkan dalam proses train modelnya.

* Mendrop duplikasi data</br>
<img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/dropduplikasi.png?raw=true'>

Drop duplikasi data yang dilakukan yaitu data yang memiliki judul buku sama tetapi memiliki ISBN yang berbeda.

* Menangani niali missing value<br/>
Cara yang dilakukan di case kali ini adalah dengan mendrop data yang terdapat missing value karena jika menggunakan _imputation_ cukup rumit padahal data yang missing value hanya sedikit.

* Menyeleksi data</br>
Untuk menghasilkan output rekomendasi yang baik disini saya menyeleksi dengan menggunakan pandas between dimana data yang diolah hanya yang ada di range 50 sampai 100. Untuk angka 100 ini diset guna mengurangi nilai outlier yang jauh seperti terdapat data buku yang memilki ratings 900+

* Melakukan normalisasi data rating</br>
Melakukan transformasi pada data fitur yang akan ditrain oleh model menggunakan library MinMaxScaler dari scikit-learn. Kita akan mentransformasikan fitur dengan scalling fitur ke rentang tertentu, dengan range default antara nol dan satu.

* Split dataset</br>
Membagi dataset menjadi data latih (train) dan data uji (test) merupakan hal yang harus kita lakukan sebelum membuat model.Data latih adalah sekumpulan data yang akan digunakan oleh model untuk melakukan pelatihan. Sedangkan, data uji adalah sekumpulan data yang akan digunakan untuk memvalidasi kinerja pada model yang telah dilatih. Proporsi pembagian yang saya lakukan pada dataset ini menggunakan proporsi pembagian 80:20 yang berarti sebanyak 80% merupakan data latih dan 20% persen merupakan data uji.

## **Modeling and Result**
Dalam proyek kali saya memanfaatkan teknik umum seperti Content-Based Filtering dan Collaborative Filtering. Untuk Content-Based Filtering akan menggunakan metode Cosine Similarity, sedangkan Collaborative Filtering menggunakan metode model based dengan Deep Learning. 

Berikut setiap tahapan yang dilakukan dalam proses modelling:
  
  
  
  
  
  
  
  
  
  
  








