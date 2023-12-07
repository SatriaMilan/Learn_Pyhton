import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10  # Misalnya interval ukuran per 10 sentimeter

# Menambahkan interval tinggi badan dari 150-190
bins = np.arange(150, 191, interval_size)

# TODO 1: buat fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def kelompokkan_ke_interval(data, interval_size):
    intervals = {}
    for tinggi in data:
        lower_bound = (tinggi // interval_size) * interval_size
        upper_bound = lower_bound + interval_size
        interval = f"{lower_bound}-{upper_bound}"
        if interval in intervals:
            intervals[interval] += 1
        else:
            intervals[interval] = 1
    return intervals

# TODO 2: Menghitung frekuensi tinggi badan dalam interval
frekuensi_interval = kelompokkan_ke_interval(tinggi_badan, interval_size)
print("Frekuensi Tinggi Badan dalam Interval:")
for interval, frekuensi in frekuensi_interval.items():
    print(f"{interval}: {frekuensi}")

# TODO 3: Visualisasi data dalam bentuk histogram
plt.hist(tinggi_badan, bins=bins, edgecolor='black', alpha=0.7, label='Data')

# TODO 4: Menambahkan kurva PDF pada hasil visualisasi data
mean, std_dev = np.mean(tinggi_badan), np.std(tinggi_badan)
x = np.linspace(min(tinggi_badan), max(tinggi_badan), 100)
y = norm.pdf(x, mean, std_dev) * len(tinggi_badan) * interval_size
plt.plot(x, y, label='PDF Distribusi Normal', color='red', linewidth=2)

plt.xlabel('Interval Tinggi Badan')
plt.ylabel('Frekuensi')
plt.title('Histogram Frekuensi Tinggi Badan')
plt.legend()
plt.show()
