#=============================== ADI =============================
import matplotlib.pyplot as plt
import numpy as np

#USER ENTRIES
input_dir = 'C:\\Users\\manac\\Documents\\SEMESTER 4\\Analisis Numerik\\UAS\\'
frame_index = 1

print("PREPARATION...")
r_coef = 0.299; g_coef = 0.587; b_coef = 0.114

file_name = "frame" + str(frame_index)
input_path = input_dir + file_name + ".jpg"
pic = plt.imread(input_path)

#============================== ABDUL ============================
# Convert gambar ke putihabu/greyscale
pic_gs = np.uint8(r_coef * pic[:, :, 0] + g_coef * pic[:, :, 1] + b_coef * pic[:, :, 2])

# Menentukan rentang warna merah yang akan dihapus dari gambar
red_lower = 100
red_upper = 255

# Membuat masking biner untuk piksel-piksel merah berdasarkan rentang warna yang ditentukan
mask = np.where((pic[:, :, 0] >= red_lower) & (pic[:, :, 0] <= red_upper) &
                (pic[:, :, 1] <= red_lower) & (pic[:, :, 2] <= red_lower), 255, 0)

# Mengaplikasikan maskingan untuk mengubah piksel-piksel merah menjadi putih pada gambar hasilnya
result = pic.copy()
result[mask == 255] = [255, 255, 255]

#=============================== IQBAL ==============================
# mengatur backgound menjadi hitam
result[~(mask == 255)] = [0, 0, 0]

# Menyimpan gambar hasil manipulasi dengan piksel-piksel merah menjadi putih dan latar belakang hitam
output_path = input_dir + "frame" + str(frame_index) + "_red_to_blacknwhite_bg.jpg"
plt.imsave(output_path, result)

# Menampilkan gambar asli dan hasilnya menggunakan matplotlib
plt.figure("Original Image")
plt.imshow(pic)
plt.figure("Result (Red to White, Black Background)")
plt.imshow(result)

plt.show()