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
  
### **Content-Based Filtering**
Pada metode ini hal pertama yang dilakukan yaitu _feature engineering_ dengan library TfidfVectorizer dari scikit-learn. Proses yang dilakukan menggunakan library TfidfVectorizer adalah tokenisasi fitur `Book-Author` sebab fitur inilah yang akan kita jadikan acuan utama sistem rekomendasi. Output yang dihasilkan adalah berbentuk matrix categorical. 
<img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/tfid.png?raw=true'>

Lalu, kita akan melakukan penghitungan derajat kesetaraan (similarity degree) antar buku dengan Cosine Similarity. Adapun formulanya seperti berikut ini:<br>
<img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/cosinerums.png?raw=true' width=70%/>

Kemudian, supaya dapat top-N recommendation kita  harus mengambil nilai dengan k tertinggi. Pada proyek ini saya memanfaatkan fungsi argpartition dari numpy untuk mendapatkan top k tertinggi pada similarity data. Lalu sistem yang dibangun dapat menampilkan buku yang direkomendasikan berdasarkan pengarang yang sama dari buku yang telah dibaca sebelumnya. Adapun Teknik Content-Based Filtering ini memiliki kelebihan dan kekurangan-nya sebagai berikut.

* Kelebihan:</br>
    * Model tidak memerlukan data apa pun tentang pengguna lain, karena rekomendasinya khusus untuk pengguna ini. Ini membuatnya lebih mudah untuk menskalakan ke sejumlah besar pengguna.
    * Model dapat menangkap minat khusus pengguna, dan dapat merekomendasikan item khusus yang sangat sedikit diminati pengguna lain.

* Kekurangan:</br>
    * Model hanya dapat membuat rekomendasi berdasarkan minat pengguna yang ada. Dengan kata lain, model memiliki kemampuan terbatas untuk memperluas minat pengguna yang ada.
    * Tidak mampu menentukan secara baik preferensi yang  tepat pada user baru.

Dalam case kali ini saya akan mengambil pengarang William Shakespeare sebagai acuan untuk menentukan top 10 rekomendasi buku berdasarkan pengarang yang sama:</br>

<img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/bukuref.png?raw=true'>

<img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/10bukucbf.png?raw=true'>

Terlihat sistem rekomendasi yang kita buat dengan Content-Based Filtering menghasilkan rekomendasi yang sangat baik dimana top-10 yang direkomendasikan semua pengarangnya sama.


### **Collaborative Filtering**
Pada teknik ini proses pembuatan sistem rekomendasi memanfaatkan model Deep Learning. Langkah yang pertama yaitu dengan menggabungkan data buku dan rating. Setelah itu melakukan penyandian terhadap data `User-ID` dan `ISBN` serta memisahkan data latih dan data validasi dengan ratio 80:20. Kemudian membuat model untuk melakukan training data. Model menggunakan operasi perkalian dot product antara embedding users dan books. Skornya ditetapkan dalam skala 0 sampai 1 dengan fungsi aktivasi sigmoid. Untuk mendapatkan hasil rekomendasi, dipilih `User-ID` secara acak lalu dilakukan penyaringan daftar buku yang belum pernah dibaca oleh user. Pada teknik collaborative filtering kelebihan dan kekurangan-nya antara lain sebagai berikut.
* Kelebihan
    * Tidak memerlukan domain knowladge karena _embeddings systemnya_ akan otomatis _learn by pattern_.
    * Dapat membuat rekomendasi tanpa harus selalu menggunakan dataset yang _large_.
    * Sangat menguntungkan dari segi kecepatan dan skalabilitas.

* Kekurangan
    *  Sulit untuk menyertakan fitur lain untuk melakukan kueri item
    *  Membutuhkan parameter rating/skor,jadi rasanya cukup sulit jika item baru masuk karena sistem tidak akan merekomendasikan item tersebut.

Berikut merupakan hasil rekomendasi buku kepada user dengan ID: 76352</br>

<img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/top10bukucf.png?raw=true'>


## **Evaluation**
Evaluasi yang akan dilakukan pada proyek ini yaitu evaluasi dengan Precision Content untuk Content-Based Filtering serta Root Mean Squared Error (RMSE) untuk Collaborative Filtering.

### **Content-Based Filtering**
Evaluasi pada teknik ini menggunakan metrik precision content untuk menghitung tingkat presisi sistem dari rekomendasi yang dibuat. Cara menghitung metric precision content cukup sederhana yaitu dengan membagikan jumlah rekomendasi yang relevan dan jumlah total rekomendasi yang diberikan oleh sistem lalu akan didapatkan hasil tingkat presisi sisem dalam melakukan rekomendasi. 

Hasil metric Presision:</br>
<img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/bukuref.png?raw=true'>

<img src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/10bukucbf.png?raw=true'><br>

Untuk menentukan hasil dari metrik ini yaitu dengan melakukan analisa pada buku yang akan dijadikan sebagai acuan. Di case ini kita mengambil buku romeo and juliet karangan William Shakespeare dari sini disimpulkan tingkat presisi dari sistem rekomendasi dengan teknik CBF yang kita buat dapat merekomendasikan sampai menembus 100% karena 10/10. Tetapi hal ini sebenarnya tidak lepas pula dengan banyaknya buku yang dikarang oleh William Shakespeare jadi data kita dapat mengenalinya dengan lebih baik.


### **Collaborative Filtering**
Metrik evaluasi yang digunakan untuk mengukur performa dari model ini yaitu dengan menggunakan metrik Root Mean Squared Error (RMSE). Semakin rendah nilai root mean square error juga menandakan semakin baik model tersebut dalam melakukan prediksi. Adapun formula sederhana yang digunakan RMSE adalah sebagai berikut.</br>

<image src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/rmse%20rumus.jpg?raw=true' width=70% /></br>

<image src='https://github.com/RidwendDev/RecomSys-Dicoding-ML-Expert/blob/main/img/vismetriks.png?raw=true' width=70% /></br>

Dari visualisasi model metriks tersebut dapat disimpulkan bahwa nilai konvergen metriks RMSE berada di sekitar angka 0.28 untuk training dan sekitar 0.34 untuk validasi. Jadi nilai tersebut sudah cukup baik untuk sistem rekomendasi.

## **Conslusion**
Dari semua proses pemaparan pembuatan model sampai tahap pengujian kita dapatkan sebuah kesimpulan model yang dibangun untuk sistem rekomendasi sederhana yang kita buat telah memiliki performa yang cukup bagus, baik dalam teknik Content-Based Filtering maupun Collaborative Filtering. Hal ini sesuai dengan tujuan kita yakni guna membangun sistem rekomendasi yang berguna untuk mengenali pattern yang baik sesuai dengan preferensi masyarakat. 

## **Reference**
Adistia, L. D., Akhriza, T. M., &amp; Jatmiko, S. (2019). Sistem Rekomendasi Buku untuk perpustakaan Perguruan tinggi berbasis association rule. Jurnal RESTI (Rekayasa Sistem Dan Teknologi Informasi), 3(2), 304–312. https://doi.org/10.29207/resti.v3i2.971 




  
  
  
  
  
  
  
  
  








