from sklearn import svm #method untuk pross perhitungan klasifikasi
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer #method untuk menghitung vsm dan tfidf
from sklearn import metrics #method untuk pembentukan matriks 1x1, 2x2, 3x3, ...
from sklearn.metrics import accuracy_score #method perhitungan akurasi
from sklearn.model_selection import KFold #Method perhitungan K-Fold
import numpy as np #scientific computing untuk array N-dimenesi
import re #re = regular expression

#Razi Aziz Syahputro#
#Universitas Negeri Jakarta
#Pendidikan Teknik Informatika & Komputer#


#CASE FOLDING + LOAD FILE DOKUMEN#
dataSet = []#inisialisasi dataSet untuk menyimpan dokumen teks yang telah di looping
for i in range(1, 267):#file dokumen yg akan di looping
    f = open("dataset/%d.txt" %i, "r+")#proses membuka file
    string = f.read()#proses pembacaan file
    string = re.sub("[^a-zA-Z]", " ", string)#proses membuang karakter selain huruf diganti spasi/sub=substitusi(mereplace semua pola RE)
    string = string.lower()#proses menjadikan kalimat huruf kecil
    dataSet.append(string)#proses memasukan/mengupdate kalimat2 kedalam dataSet
    f.close()#proses menutup file

print("Case Folding: \n", dataSet)
#print("\nCase Folding:")
#print(dataSet[4])
#print(dataSet[1])
#print(dataSet[2])

#LOAD FILE STOPWORDS#
stopword = []#inisialisasi dataSet untuk menyimpan dokumen teks
s = open("id.stopwords.txt", "r+")#proses membuka file
stop = s.read()#proses pembacaan file
stop = re.sub("[^a-zA-Z]", " ", stop)#proses membuang karakter selain huruf diganti spasi/sub=substitusi(mereplace semua pola RE)
stopword.append(stop)#proses memasukan/mengupdate kalimat2 kedalam stopword
#s.close()#proses menutup file
print("\nDaftar Stopword: \n", stopword)

#TOKENIZING DOKUMEN#
bagOfWords = dataSet#insialisasi bank kata(bag of word) yang isinya sama dengan variabel dataSet
for x in range(0, 266):#file dokumen yg akan di looping
    bagOfWords[x] = dataSet[x].split()#isi dari 'variabel dataSet' di pecah2 menjadi satuan kata lalu di copy ke sebuah variabel indeks ke-x
print("\nTokenizing: \n", bagOfWords)
#print("\nTokenizing:")
#print(bagOfWords[4])
#print(bagOfWords[1])
#print(bagOfWords[2])

#TOKENIZING STOPWORDS#
stopwords = stopword#insialisasi bank kata(variabel stopwords) yang isinya sama dengan variabel stopword
for x in range(0,1):#file dokumen yg akan di looping
    stopwords[x] = stopword[x].split()#isi dari 'variabel word' di pecah2 menjadi satuan kata lalu di copy ke sebuah variabel indeks ke-x
print("\nTokenizing Stopwords: \n", stopwords)

#FILTERING#
for x in range(0, 266):#looping pada 266 file dokumen abstrak
    for y in range(0, len(bagOfWords[x])):#looping pada setiap kata per dokumen
        for z in range(0, 780):#looping pada setiap kata stopwords
            if(bagOfWords[x][y] == stopwords[0][z]):#proses membandingkan setiap kata per dokumen dgn setiap kata pada stopword
                bagOfWords[x][y]=''#jika ditemukan kata yang tidak penting maka kata tsb dihapus
print("\nFiltering: \n", bagOfWords)
#print("\nFiltering:")
#print(bagOfWords[4])
#print(bagOfWords[1])
#print(bagOfWords[2])

#KATA BERSIH/Mengembalikan kata2 yg sudah tidak ada kata yg 'tidak penting' menjadi kalimat utuh/dokumen#
for i in range(0, len(bagOfWords)):#looping untuk seluruh kata pada bank kata
    bagOfWords[i] = filter(bool, bagOfWords[i])#menghapus kata yg kosong
    dataSet[i] = ' '.join(bagOfWords[i])#menggabungkan kata demi kata dengan sebuah pemisah spasi per dokumen
print("\nKata Bersih: \n", dataSet)
#print("\nKata Bersih:")
#print(dataSet[4])
#print(dataSet[2])
#print(dataSet[1])

#VSM & TFIDF#
VSM = CountVectorizer().fit_transform(dataSet) #method vector space model dari library scikit learn melakukan perubahan menjadi sebuah vektor
#tfidf = TfidfTransformer() #method tfidf dari library scikit learn di copy ke variabel tfidf
TFIDF = TfidfTransformer().fit_transform(VSM) #method tfidf dari library scikit learn melakukan perubahan menjadi sebuah nilai
#print (CountVectorizer().vocabulary)
print("\nVSM: \n", VSM)
print("\n", VSM.todense())
print("\nTFIDF: \n", TFIDF)
#hhprint(TFIDF.todense())

#KONVERSI LABEL#
#Pendidikan = 0, RPL = 1, TKJ = 2, MM = 3#
label_manual =  [1,1,1,2,3,3,1,1,0,2,3,3,1,2, ## data 1 - 14
                 1,1,2,2,0,1,3,3,3,2,2,2,2,2, ## data 15 - 28
                 2,1,1,3,1,1,1,1,1,3,3,0,1,1, ## data 29 - 42
                 1,0,0,0,2,0,1,1,1,1,1,1,1,1, ## data 43 - 56
                 2,2,2,3,0,0,0,1,0,1,1,1,2,2, ## data 57 - 70
                 3,1,1,1,0,0,3,2,1,0,1,3,3,3, ## data 71 - 84
                 3,3,3,3,3,3,1,2,3,3,1,3,3,3, ## data 85 - 98
                 0,3,2,0,3,3,3,1,1,1,2,2,2,1, ## data 99 - 112
                 1,1,1,3,1,0,0,0,3,1,3,3,3,3, ## data 113 - 126
                 3,3,3,3,3,3,3,3,3,3,2,2,2,0, ## data 127 - 140
                 1,3,3,1,1,1,1,1,1,1,1,1,1,1, ## data 141 - 154
                 1,1,1,1,1,1,1,3,3,3,3,3,3,3, ## data 155 - 168
                 1,1,1,1,1,1,1,1,1,1,3,1,1,2, ## data 169 - 182
                 0,0,2,2,1,1,1,2,2,2,2,1,0,3, ## data 183 - 196
                 1,1,3,3,3,3,1,1,1,1,1,2,1,0, ## data 197 - 210
                 1,1,0,0,0,2,2,2,0,0,3,3,3,0, ## data 211 - 224
                 0,0,0,0,0,0,0,0,1,1,1,1,1,1, ## data 225 - 238
                 1,1,1,3,1,1,1,1,1,1,1,1,1,1, ## data 239 - 252
                 1,2,1,1,1,1,1,1,1,3,0,3,3,3] ## data 253 - 266

#METHOD MENGHITUNG RATA2 AKURASI#
akurasi = []
def avg_akurasi(): ## nama fungsi
    total = 0 ## pengosongan variabel
    for i in range(10): ## looping 10x karena ada 10 fold
        total = total + akurasi[i] ## tiap looping nilai total akan ditambahkan dengan nilai akurasi tiap fold
    print("-------------------------------------------------------------------------------------------------------") ## cetak pembatas
    print("Rata-rata akurasi keseluruhan adalah :", total / 10) ## cetak rata-rata akurasi

kFoldCrossValidation = KFold(n_splits=10)#fungsi K-Fold Cross Validation melakukan insialisasi 10x iterasi
for latih, uji in kFoldCrossValidation.split(TFIDF, label_manual):#proses looping yg masing2 pernah jadi data latih maupun uji
    print("-----------------------------------------------------------------------")
    print("Banyak Data Latih: ", len(latih))
    print("Banyak Data Uji: ", len(uji))
    print("\nData Latih: \n", latih)
    print("\nData Uji: \n", uji)

    dataLatih1, dataUji1 = TFIDF[latih], TFIDF[uji]#proses inisialisasi dari masing2 data latih/uji dijadikan nilai tfidf lalu di copy ke variabel dataLatih/Uji1
    label_manual = np.array([1, 1, 1, 2, 3, 3, 1, 1, 0, 2, 3, 3, 1, 2,  ## data 1 - 14
                             1, 1, 2, 2, 0, 1, 3, 3, 3, 2, 2, 2, 2, 2,  ## data 15 - 28
                             2, 1, 1, 3, 1, 1, 1, 1, 1, 3, 3, 0, 1, 1,  ## data 29 - 42
                             1, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1,  ## data 43 - 56
                             2, 2, 2, 3, 0, 0, 0, 1, 0, 1, 1, 1, 2, 2,  ## data 57 - 70
                             3, 1, 1, 1, 0, 0, 3, 2, 1, 0, 1, 3, 3, 3,  ## data 71 - 84
                             3, 3, 3, 3, 3, 3, 1, 2, 3, 3, 1, 3, 3, 3,  ## data 85 - 98
                             0, 3, 2, 0, 3, 3, 3, 1, 1, 1, 2, 2, 2, 1,  ## data 99 - 112
                             1, 1, 1, 3, 1, 0, 0, 0, 3, 1, 3, 3, 3, 3,  ## data 113 - 126
                             3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 0,  ## data 127 - 140
                             1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  ## data 141 - 154
                             1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3,  ## data 155 - 168
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2,  ## data 169 - 182
                             0, 0, 2, 2, 1, 1, 1, 2, 2, 2, 2, 1, 0, 3,  ## data 183 - 196
                             1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 1, 2, 1, 0,  ## data 197 - 210
                             1, 1, 0, 0, 0, 2, 2, 2, 0, 0, 3, 3, 3, 0,  ## data 211 - 224
                             0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,  ## data 225 - 238
                             1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  ## data 239 - 252
                             1, 2, 1, 1, 1, 1, 1, 1, 1, 3, 0, 3, 3, 3])  ## data 253 - 266

    dataLatih2, dataUji2 = label_manual[latih], label_manual[uji]#proses inisialisasi dari masing2 data latih/uji dibentuk ke label untuk proses prediksi lalu di copy ke variabel dataLatih/Uji2
    SVM = svm.SVC(kernel='linear').fit(dataLatih1, dataLatih2)#data latih melakukan proses pelatihan dengan algoritma SVM
    prediksi = SVM.predict(dataUji1)#proses prediksi dari data latih yang sudah tersimpan sebagai model
    print("\nHasil Prediksi: \n", prediksi)
    print("\nConfusion Matrix: \n", metrics.confusion_matrix(dataUji2, prediksi))#proses pembetukan metriks
    akurasi.append(accuracy_score(dataUji2, prediksi))
    print("\nAkurasi: ", accuracy_score(dataUji2, prediksi))
    print()
    label = ['Pendidikan', 'RPL', 'TKJ', 'MM']
    print(metrics.classification_report(dataUji2, prediksi, target_names=label))#proses pembentukan confusin matrix
avg_akurasi()