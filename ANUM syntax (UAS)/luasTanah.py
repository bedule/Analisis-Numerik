#================================ DIAZ =============================
import matplotlib.pyplot as plt

pic = plt.imread ("frame1_red_to_blacknwhite_bg.jpg")
row, col, depth = pic.shape
print("row, col =", row, col)
lebar_gambar = 100 #dalam m
tinggi_gambar = 100 #dalam m
luas_area_total = lebar_gambar * tinggi_gambar
pic = pic.astype(int)
plt.figure(1)
plt.imshow(pic)

#=============================== MARIAM ===========================
m = row * col
print("Jumlah seluruh piksel (m) =", m)
plt.pause(2)

#Hitung jumlah piksel putih dengan integrasi numerik

n = 0
for i in range (0,row):
    for j in range(0,col):
        if pic [i,j,0] + pic [i,j,1] + pic[i,j,2] > 0.9 * (255*3):
            n = n + 1
            print("Piksel","(", i, ",",j,") merupakan elemen objek. Hasil sementara n =",n)


#=============================== YERU ==============================
print("-------------------------------------------------------------------")
print("")

#Hitung Luas Penampang Objek
print("Luas area total =", luas_area_total, "m2.")
print("Jumlah semua piksel (hitam dan putih) =", m ,".")
print("Jumlah piksel objek (putih) =", n, ".")
luas_penampang_objek = (n/m) *luas_area_total
print("LUAS PENAMPANG OBJEK (putih) = ", luas_penampang_objek, "m2.")