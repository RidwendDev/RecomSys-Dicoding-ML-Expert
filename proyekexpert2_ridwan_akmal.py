# -*- coding: utf-8 -*-
"""ProyekExpert2_Ridwan Akmal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/144HvrrKbrszfXV1dHPelgMtJRuAH7T0W

### **Import Package**
"""

# Commented out IPython magic to ensure Python compatibility.
import zipfile
import pandas as pd
import numpy as np
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.callbacks import EarlyStopping

import matplotlib.pyplot as plt
# %matplotlib inline

from google.colab import files
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split, GridSearchCV

"""berikutnya lakukan instalasi untuk library kaggle"""

!pip install -q kaggle

"""lakukan upload file API Token kagglenya"""

uploaded = files.upload()

"""berikutnya verifikasi kredensial API-nya"""

!chmod 600 /content/kaggle.json

! KAGGLE_CONFIG_DIR=/content/ kaggle datasets download -d arashnic/book-recommendation-dataset

"""### **Extract Data**"""

local_zip = '/content/book-recommendation-dataset.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/content')
zip_ref.close()

"""### **Load dataset**"""

books = pd.read_csv('/content/Books.csv')
ratings = pd.read_csv('/content/Ratings.csv')

"""mengambil 5 data awal di books"""

books.head()

"""mengambil 5 data awal di ratings"""

ratings.tail()

"""# **Data Understanding**

Untuk yang Books
- ISBN:  International Standard Book Number(bersifat unik).
- Book-Title: Judul Buku.
- Book-Author: Nama pengarang buku.
- Year-Of-Publication: Tahun penerbitan buku.
- Publisher: Pihak penerbit buku.
- Image-URL-S: URL yang menautkan ke gambar sampul berukuran kecil.
- Image-URL-M: URL yang menautkan ke gambar sampul berukuran normal.
- Image-URL-L: URL yang menautkan ke gambar sampul berukuran besar.

Untuk yang Ratings
- User-ID: Nomer unik user yang memberikan rating.
- ISBN: Kode pengidentifikasian buku yang bersifat unik.
- Book-Rating: Skor dari rating yang diberikan.=
"""

books.info()

"""Terdapat 271360 entri dan seluruh tipe data dalam kolom books adalah object"""

print('Banyak data judul buku: ', len(books['Book-Title'].unique()))

title_list = books['Book-Title'].value_counts().keys()
jumlah = books['Book-Title'].value_counts()

jum_judul = pd.DataFrame({'Judul': title_list, 'Jumlah': jumlah}).reset_index(drop=True)
jum_judul

"""Dari data ini dapat kita lihat judul buku paling banyak adalah Selected Poems diikuti Little women dan Wuthering Heights."""

print('Banyak data pengarang buku: ', len(books['Book-Author'].unique()))

author_list = books['Book-Author'].value_counts().keys()
jumlah = books['Book-Author'].value_counts()

jum_pengarang = pd.DataFrame({'Pengarang': author_list, 'Jumlah': jumlah}).reset_index(drop=True)
jum_pengarang

"""Dari data ini dapat kita lihat penulis buku paling banyak adalah Agatha Cristie diikuti William Shakespeare dan Stephenn King."""

print('Banyak data penerbit buku: ', len(books['Publisher'].unique()))

pub_list = books['Publisher'].value_counts().keys()
jumlah = books['Publisher'].value_counts()

jum_penerbit = pd.DataFrame({'Penerbit': pub_list, 'Jumlah': jumlah}).reset_index(drop=True)
jum_penerbit

"""Dari data ini dapat kita lihat penulis buku paling banyak adalah Harlequin diikuti Siihoute dan Pocket."""

ratings.info()

list_rating = ratings['Book-Rating'].value_counts().keys()
jumlah = ratings['Book-Rating'].value_counts()

jum_rating = pd.DataFrame({'Ratings': list_rating, 'Jumlah': jumlah}).reset_index(drop=True)
jum_rating

sns.barplot(data=jum_rating, x='Ratings', y='Jumlah')
plt.show()

"""Terlihat dari visualisasi bahwa range rating ada diantara nilai 0 sampai dengan 10 dan buku paling banyak adalah dengan rating 0 dari user yang sebanyak 716109 buku.

### **Memeriksa data kosong(missing value)**
"""

books.isnull().sum()

ratings.isnull().sum()

"""Terlihat bahwa terdapat beberapa kolom yang memiliki nilai missing value pada data book sedangkan untuk ratings bersih tanpa missing value"""

books.info()

kolom0 = ['Year-Of-Publication', 'Publisher', 'Image-URL-M', 'Image-URL-L']
books.drop(kolom0, axis=1, inplace=True)

"""Untuk melakukan Content Based Filtering kita tidak akan memanfaatkan beberapa kolom seperti yang sudah dimasukkan kedalam wadah yang diinisiasikan dengan nama kolom0"""

books.head()

"""Diatas merupakan tampilan kolom-kolom pada data buku kita yang sudah dilakukan drop beberapa value

### **Merging data buku dan rating**
"""

ratings_baru = ratings.merge(books,on='ISBN')
ratings_baru = ratings_baru.groupby('Book-Title').sum()['Book-Rating'].reset_index()
ratings_baru.rename(columns={'Book-Rating':'Book-Ratings'}, inplace=True)

"""membuat sebuah variabel dengan nama ratings_baru yang kita merging dari rating buku dengan index ISBN, lalu di grouping berdasarkan judul buku."""

buku_baru = pd.DataFrame({'Book-Title': books['Book-Title'].unique()})
buku_baru = pd.merge(buku_baru, ratings_baru, on='Book-Title', how='left')
buku_baru = buku_baru.merge(books, on='Book-Title').drop_duplicates('ISBN')

"""membuat sebuah variabel dengan nama buku_baru dengan memanfaatkan Dataframe pandas membuat key-nya serta memasukkan valuenya dari judul buku dengan unique, serta melakukan merging dengan index judul secara left. Berikutnya menghapus nilai duplikasi pada ISBN.

menghapus duplikasi data yang terdapat di list buku
"""

buku_baru = buku_baru.drop_duplicates('Book-Title').reset_index(drop=True)
len(buku_baru['ISBN'].unique()), len(buku_baru['Book-Title'].unique())

buku_baru.head()

"""Hasil setelah dilakukan pembersihan """

buku_baru.isnull().sum()

"""karena terdapat cukup banyak nilai missing value pada data book ratings kita akan menghapus nilai missing value tsb"""

buku_baru = buku_baru.dropna()
buku_baru.shape

buku_baru.isnull().sum()

"""Oke sudah aman dari nilai missing value

# **Content-Based Filtering**

Yang akan kita lakukan sampai tahap modelling nanti hanya buku dengan skor rating diatas 50 sampai dengan nilai 100
"""

buku = buku_baru[buku_baru['Book-Ratings'].between(50, 100, inclusive = True)]
buku.drop(['ISBN', 'Book-Ratings'], axis=1, inplace=True)
buku

"""# **Modelling**

Tfid Vectorizer
"""

data = buku
data.sample(5)

tfid = TfidfVectorizer(token_pattern=r"(?u)\b\w\w+\b\s+\w+")
tfid.fit(data['Book-Author']) 

tfid.get_feature_names()

"""Transformasi data kedalam bentuk matriks"""

tfidf_matrix = tfid.fit_transform(data['Book-Author']) 
tfidf_matrix.shape

tfidf_matrix.todense()

"""Berikutnya kita akan menghitung Cosine Similarity"""

cosine_sim = cosine_similarity(tfidf_matrix) 
cosine_sim

cosine_sim_df = pd.DataFrame(cosine_sim, index=data['Book-Title'], columns=data['Book-Title'])
cosine_sim_df

"""## **Mendapatkan rekomendasi buku**

Mendapatkan rekomendasi buku berdasarkan pengarang yang sama dengan buku yang telah dibaca oleh user ini adalah pengaplikasian dari CBF yang mudahnya kita dapat membuat rekomendasi berdasarkan kemiripan yang disukai dari user berdasarkan masa lalu.

Akan dibuat fungsi book_recommendations yang diberikan parameter berupa name, similarity_data dengan metoode cosine, serta mengambil items, dan k.
"""

def book_recommendations(book_name, similarity_data=cosine_sim_df, items=data, k=5):
  index = similarity_data[book_name].to_numpy().argpartition(range(-1, -(k+1), -1))[::-1]
  closest = similarity_data.columns[index[:k+1]]
  closest = closest.drop(book_name, errors='ignore')

  return pd.DataFrame(closest).merge(items).head(k)

"""Setelah kita selesai membuat fungsi kita akan melakukan pencarian bukunya dan mengambil judul yang pernah kita baca misalnya, lalu akan ditampilkan pengarang, judul dan url-nya."""

buku_ref = 'Romeo and Juliet'
data[data['Book-Title'].eq(buku_ref)]

"""Berikutnya dengan fungsi tadi  kita akan mendapatkan 10 buku terkait dari buku yang mempunyai pengarang sama dengan yang pernah kita baca sebelumnya."""

book_recommendations(buku_ref, k=10)

"""- Jika dilihat dari hasil tersebut. Tingkat presisi dari sistem rekomendasi dengan teknik CBF yang kita buat dapat kita ketahui melalui seberapa banyak sistem dengan benar merekomendasikan buku berdasarkan pengarangnya. Dari 10 buku yang direkomendasikan semuanya memiliki pengarang yang sama dengan buku Romeo and Juliet. <br> Jadi dapat dikatakan tingkat presisi untuk hasil kita sangatlah baik yaitu 100%. Hal ini dikarenakan buku dengan Pengarang William Shakespeare yang terdapat pada data berjumlah 10. <br>Ini sebenarnya tidak lepas pula dengan banyaknya buku yang dikarang oleh William Shakespeare jadi data kita dapat mengenalinya dengan lebih baik.

# **Collaborative Filtering**

## **Data Preparation**

Melakukan penggabungan data<br>
Tidak seperti pada teknik Content-Based Filtering. Data yang digunakan di teknik Collaborative Filtering kali ini tidak memerlukan data Book-Author, dan Book-Ratings,. Sebab pada teknik ini hanya menggunakan rating sebagai acuan sistem rekomendasi.
"""

df = ratings
df = df.merge(buku_baru, on='ISBN')
df.drop(['Book-Ratings', 'Book-Author'], axis=1, inplace=True)

"""Melakukan penyandian pada fitur User-ID dan Book-Title kedalam bentuk index"""

user_ids = df['User-ID'].unique().tolist()
user2encoded = {x: i for i, x in enumerate(user_ids)}
encoded2user = {i: x for i, x in enumerate(user_ids)}

book_isbns = df['ISBN'].unique().tolist()
book2encoded = {x: i for i, x in enumerate(book_isbns)}
encoded2book = {i: x for i, x in enumerate(book_isbns)}

"""Melakukan encode pada data book dan user"""

df['User-Encoded'] = df['User-ID'].map(user2encoded)
df['Book-Encoded'] = df['ISBN'].map(book2encoded)

"""Melakukan perhitungan jumlah user dan book setelah dilakukan encoding"""

num_users = len(user2encoded)
print(num_users)
 
num_books = len(encoded2book)
print(num_books)

df['Book-Rating'] = df['Book-Rating'].values.astype(np.float32)
 
min_rating = min(df['Book-Rating'])
max_rating = max(df['Book-Rating'])

print(f'Number of User: {num_users}, Number of Books: {num_books}, Min Rating: {min_rating}, Max Rating: {max_rating}')

"""Mengambil 1 sampel berisikan User-ID, ISBN, Book-Rating, Book-Title, Image-URL-S, User-Encoded	serta Book-Encoded."""

df.sample()

"""## **Normalisasi data rating**

Melakukan transformasi data dan reshaping di nilai y nya
"""

x = df[['User-Encoded', 'Book-Encoded']].values
y = df['Book-Rating'].values
y = y.reshape(-1, 1)

from sklearn.preprocessing import MinMaxScaler

"""Setelah memanggil MinMaxScaler kita  mentransformasikan fitur dengan scalling fitur ke rentang tertentu, dengan range default antara nol dan satu."""

scaler = MinMaxScaler()
norm_y = scaler.fit_transform(y)
norm_y = norm_y.reshape(1, -1)[0]

"""## **Split dataset**

Melakukan train test split dengan proporsi train testnya sebesar 80% dan 20%. Lalu akan diberikan random state=123
"""

x_train, x_val, y_train, y_val = train_test_split(x, norm_y, test_size=0.2, random_state=123)

def create_dataset(x, y, batch_size, buffer_size=None, shuffle=True):
  ds = tf.data.Dataset.from_tensor_slices((x, y))

  if shuffle:
    ds = ds.shuffle(buffer_size)

  ds = ds.batch(batch_size).cache().prefetch(tf.data.experimental.AUTOTUNE)

  return ds

batch_size = 128
buffer_size = len(x)

train_ds = create_dataset(x_train, y_train, batch_size, buffer_size)
val_ds = create_dataset(x_val, y_val, batch_size, shuffle=False)

"""## **Membangun Model**

Di sini, saya membuat class RecommenderNet dengan keras Model class seperti yang ada pada materi di kelas dicoding. Kode class RecommenderNet ini juga terinspirasi dari tutorial dalam situs Keras dengan beberapa adaptasi sesuai case yang kita pecahkan
"""

class RecommenderNet(tf.keras.Model):
  def __init__(self, num_users, num_books, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)

    self.num_users = num_users
    self.num_books = num_books
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding(
        num_users,
        embedding_size,
        embeddings_initializer='he_normal',
        embeddings_regularizer=keras.regularizers.l2(1e-3),
    )
    self.user_bias = layers.Embedding(num_users, 1)
    self.books_embedding = layers.Embedding(
        num_books,
        embedding_size,
        embeddings_initializer='he_normal',
        embeddings_regularizer=keras.regularizers.l2(1e-3),
    )
    self.books_bias = layers.Embedding(num_books, 1)

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:, 0])
    user_bias = self.user_bias(inputs[:, 0])
    books_vector = self.books_embedding(inputs[:, 1])
    books_bias = self.books_bias(inputs[:, 1])

    dot_user_books = tf.tensordot(user_vector, books_vector, 2)

    x = dot_user_books + user_bias + books_bias

    return tf.nn.sigmoid(x)

embedding_size = 32

model = RecommenderNet(num_users, num_books, embedding_size)
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = tf.keras.optimizers.Adam(),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""Model kita ini menggunakan Binary Crossentropy untuk menghitung loss function, Adam (Adaptive Moment Estimation) sebagai optimizer, dan root mean squared error (RMSE) sebagai metrics evaluationnya.

## **Train Model**
"""

history = model.fit(
  train_ds,
  epochs = 20,
  validation_data = val_ds,
  verbose=1,
)

books_df = buku_baru.drop(['Book-Ratings', 'Book-Author'], axis=1)
df = pd.read_csv('/content/Ratings.csv')
 
user_id = df['User-ID'].sample(1).iloc[0]
buku_pilihan_user = df[df['User-ID'] == user_id]

book_no_choosen = books_df[~books_df['ISBN'].isin(buku_pilihan_user['ISBN'].values)]['ISBN']
book_no_choosen = list(
    set(book_no_choosen).intersection(set(book2encoded.keys())))
 
book_no_choosen = [[book2encoded.get(x)] for x in book_no_choosen]
user_encoder = user2encoded.get(user_id)
user_book_array = np.hstack(
    ([[user_encoder]] * len(book_no_choosen), book_no_choosen))

"""Melakukan flatten dan melihatkan rekomendasi untuk user"""

ratings = model.predict(user_book_array).flatten()
 
top_ratings = ratings.argsort()[-10:][::-1]
recommended_books_ids = [
    encoded2book.get(book_no_choosen[x][0]) for x in top_ratings
]
 
print(f'Showing recommendations for users: {user_id}')
print('===' * 10)
print('Books with high ratings from user')
print('===' * 10)
 
top_book_user = (
    buku_pilihan_user.sort_values(
        by = 'Book-Rating',
        ascending=False
    )
    .head(5)['ISBN'].values
)
 
books_df_rows = books_df[books_df['ISBN'].isin(top_book_user)]
for row in books_df_rows.itertuples():
    print(f'{row[1]} ({row[3]})')
 
print('----' * 10)
print('Top 10 book recommendation')
print('----' * 10)
 
recommended_book = books_df[books_df['ISBN'].isin(recommended_books_ids)]
for row in recommended_book.itertuples():
    print(f'{row[1]} ({row[3]})')

"""**Visualisasi dari metriknya**"""

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('Metriks Model')
plt.ylabel('RMSE')
plt.xlabel('epoch')
plt.legend(['RMSE', 'VAL_RMSE'])
plt.show()

"""Dari visualisasi model metriks tersebut dapat disimpulkan bahwa nilai konvergen metriks RMSE berada di sekitar angka 0.28 untuk training dan sekitar 0.34 untuk validasi  """